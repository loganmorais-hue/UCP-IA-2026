from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F

tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
model = AutoModel.from_pretrained("microsoft/codebert-base")

code1 = "public boolean isAdult(User user){if(user.getAge() >= 18) return true; else return false;}"
code2 = "public boolean canAccessRestrictedArea(User user){if(user.IsActive() && user.getAge() >= 18) return true;} else return false;}"

inputs1 = tokenizer(code1, return_tensors="pt", truncation=True)
inputs2 = tokenizer(code2, return_tensors="pt", truncation=True)

with torch.no_grad():
    outputs1 = model(**inputs1)
    outputs2 = model(**inputs2)

embeddings1 = outputs1.last_hidden_state[:, 0, :]  
embeddings2 = outputs2.last_hidden_state[:, 0, :]

similarity = F.cosine_similarity(embeddings1, embeddings2)

print(similarity.item())