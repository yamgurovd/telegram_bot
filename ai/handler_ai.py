from transformers import GPTNeoXForCausalLM, AutoTokenizer
from src.randomizers import randomizer_text

model = GPTNeoXForCausalLM.from_pretrained(
    "EleutherAI/pythia-70m-deduped",
    revision="step3000",
    cache_dir="./pythia-70m-deduped/step3000",
)

tokenizer = AutoTokenizer.from_pretrained(
    "EleutherAI/pythia-70m-deduped",
    revision="step3000",
    cache_dir="./pythia-70m-deduped/step3000",
)

def output_():
    textinput = randomizer_text.generate_text(size_text=200,)
    inputs = tokenizer(
        textinput,
        return_tensors="pt"
    )
    tokens = model.generate(
        **inputs,
        max_new_tokens=50
    )
    output = tokenizer.decode(tokens[0])  # - textinput
    output_ = output[len(textinput):]
    return output_


print()

# tokenizer.decode(model.generate(**tokenizer(
#     "Is Artyom a young baboon? ",
#     return_tensors="pt",
#     max_length=512
# ))[0])