from groq import Groq

client = Groq(api_key="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")

completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
      {
        "role": "system",
        "content": "Você é um especialista em desenvolvimento de software, focado em Java. Sua tarefa é gerar testes automáticos para o código Java fornecido. Os testes devem cobrir casos comuns e casos de borda, garantindo que o código seja robusto e confiável."
      },
      {
        "role": "user",
        "content": "Considere o método em Java: public boolean isPrime(int n){ if(n <= 1) return false; for(int i = 2; i < n; i++){for(int i = 2; i < n; i++){ if(n % i == 0) return false; } return true; } Gere testes automáticos para este código, junto com a documentação e mensagem de commitp para o método de teste."
      }
    ],
    temperature=1,
    max_completion_tokens=2042,
    top_p=1,
    stream=True,
    stop=None
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")