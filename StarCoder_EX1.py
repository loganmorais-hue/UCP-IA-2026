from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "bigcode/starcoder2-3b"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

prompt = """// Refactor this Java code to prevent division by zero:
// Original:
// public int divide(int a, int b){
//     return a/b;
// }
//
// Refactored Java code:
public int divide(int a, int b) {
"""

inputs = tokenizer(prompt, return_tensors="pt")

outputs = model.generate(**inputs, max_length=80)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
