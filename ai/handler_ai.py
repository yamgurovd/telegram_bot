from transformers import GPTNeoXForCausalLM, AutoTokenizer
import torch
import torch.nn.functional as F
import numpy as np

model = GPTNeoXForCausalLM.from_pretrained(
    "EleutherAI/pythia-70m-deduped",
    revision="step143000",
    cache_dir="./pythia-70m-deduped/step143000",
)

tokenizer = AutoTokenizer.from_pretrained(
    "EleutherAI/pythia-70m-deduped",
    revision="step143000",
    cache_dir="./pythia-70m-deduped/step143000"
)

def output_ai(textinput: str):
    inputs = tokenizer(
        textinput,
        return_tensors="pt"
    )
    tokens = model.generate(
        **inputs,
        do_sample=True,
        max_new_tokens=150,
        top_p = 0.9,
        top_k = 50,
        temperature = 1,
        pad_token_id=tokenizer.eos_token_id
    )
    output = tokenizer.decode(tokens[0])
    output_ = output[len(textinput):]  # - textinput
    return output_

def tail_free_sampling(logits, tail_free_threshold=0.9, temperature=1.0):
    # Применяем масштабирование температуры
    logits = logits / temperature

    # Преобразуем логику в вероятности с помощью softmax
    probs = F.softmax(logits, dim=-1)

    # Сортируем вероятности по убыванию
    sorted_probs, sorted_indices = torch.sort(probs, descending=True)

    # Преобразуем вероятности в массив NumPy
    sorted_probs = sorted_probs.numpy()
    sorted_indices = sorted_indices.numpy()

    # Рассчитываем первую и вторую производные
    first_derivative = np.diff(sorted_probs)
    second_derivative = np.diff(first_derivative)
    abs_second_derivative = np.abs(second_derivative)

    # Нормализуем вторую производную
    normalized_second_derivative = abs_second_derivative / np.sum(abs_second_derivative)

    # Находим минимальное подмножество производных, которое превышает порог
    cumulative_sum = np.cumsum(normalized_second_derivative)
    cutoff_index = np.searchsorted(cumulative_sum, tail_free_threshold, side='right')

    # Оставляем только токены до индекса обрезки
    if cutoff_index < len(sorted_probs):
        sorted_indices = sorted_indices[:cutoff_index + 1]
        sorted_probs = sorted_probs[:cutoff_index + 1]
    else:
        sorted_indices = sorted_indices[:1]
        sorted_probs = sorted_probs[:1]

    # Переопределяем вероятности
    normalized_probs = sorted_probs / np.sum(sorted_probs)

    # Выбираем следующий токен на основе нормализованных вероятностей
    next_token = np.random.choice(sorted_indices, p=normalized_probs)

    return next_token


def generate_text(input_text, max_length=100, temperature=1.0, tail_free_threshold=0.9):
    tokens = tokenizer(
        input_text,
        return_tensors="pt"
    ).input_ids.squeeze().tolist()

    for _ in range(max_length):
        input_ids = torch.tensor(tokens).unsqueeze(0).to(
            model.device)  # Добавляем размерность батча и перемещаем на устройство модели

        with torch.no_grad():
            next_token_logits = model(input_ids).logits[:, -1, :]

        next_token = tail_free_sampling(next_token_logits[0], tail_free_threshold=tail_free_threshold)
        tokens.append(next_token)

    return tokenizer.decode(tokens)


def output_2(textinput: str, max_length: int = 60,
             temperature: float = 0.1, tail_free_threshold: float = 0.98):
    output = generate_text(
        textinput + "\nPythia:",
        max_length=max_length,
        temperature=temperature,
        tail_free_threshold=tail_free_threshold
    )
    output_ = output[len(textinput):]  # - textinput
    return " " + output_[1:]
