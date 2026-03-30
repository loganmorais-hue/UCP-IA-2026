from transformers import AutoTokenizer, AutoModelForCausalLM
model_name = "Qwen/Qwen2.5-1.5B-Instruct"

HF_TOKEN = "seu_token"

Tokenizer = AutoTokenizer.from_pretrained(model_name, token=HF_TOKEN)

Model = AutoModelForCausalLM.from_pretrained(model_name, token=HF_TOKEN)

code = '''
public int divide(int a, int b){
    return a/b;
}
'''
prompt = f"Refactor this Java code and point out any issues, correcting them as well:\n{code}"

inputs = Tokenizer(prompt, return_tensors="pt")

outputs = Model.generate(**inputs, max_new_tokens=200)

print(Tokenizer.decode(outputs[0], skip_special_tokens=True))
