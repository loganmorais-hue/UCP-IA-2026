from transformers import AutoTokenizer, AutoModelForCausalLM
model_name = "Qwen/Qwen2.5-1.5B-Instruct"

HF_TOKEN = "seu_token"

Tokenizer = AutoTokenizer.from_pretrained(model_name, token=HF_TOKEN)

Model = AutoModelForCausalLM.from_pretrained(model_name, token=HF_TOKEN)

code = '''
public boolean isPrime(int n){
    if(n <= 1) return false;
    for(int i = 2; i < n;i++){
        if(n % i == 0)
            return false;
    }
    return true;
}
'''
prompt = f"Generate automatic tests for this Java code:\n{code}"

inputs = Tokenizer(prompt, return_tensors="pt")

outputs = Model.generate(**inputs, max_new_tokens=200)

print(Tokenizer.decode(outputs[0], skip_special_tokens=True))
