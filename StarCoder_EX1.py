from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "bigcode/starcoder2-3b"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

prompt = """
Analyze the following Java code and point if there are any problems with it and correct them.
public int divide(int a, int b){
    return a/b;
}
"""

inputs = tokenizer(prompt, return_tensors="pt")

outputs = model.generate(**inputs, max_length=80)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))