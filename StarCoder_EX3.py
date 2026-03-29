from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "bigcode/starcoder2-3b"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

prompt = """ // Generate automatic tests for this Java code:
public boolean isPrime(int n){
    if(n <= 1) return false;
    for(int i = 2; i < n;i++){
        if(n % i == 0)
            return false;
    }
    return true;
}
"""

inputs = tokenizer(prompt, return_tensors="pt")

outputs = model.generate(**inputs, max_length=150)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))