# UCP-IA-2026

## Exercício 1 

### 1.1)
Exercício foi a análise de um código Java que realizava uma divisão:

java
```
public int divide(int a, int b){
       return a / b;
}
```
usando o prompt "Analyze the following Java code and point out any issues, correcting them as well:", o Qwen respondeu com precisão, apontando o erro caso a variável b fosse igual a 0, causando um ArithmeticException, bem como outras possíveis melhorias: entre elas a mudança do tipo das variáveis para "double" para maior precisão.

Tendo em vista que o StarCoder é um modelo de AutoComplete de um code ele não gerou uma análise do texto 

---------------------------------------------
### 1.2)
A segunda parte do exercício foi a correção do código

A correção feita por ambas as IA's estão corretas, consertando o problema no caso de b=0, porém o Qwen utilizou do math.ceil() e de variáveis "double" para arrendondar para retornar o valor, enquanto o Starcoder usou return(a/b), sendo mais direto ao ponto.

----------------------------------------------
## Exercício 2 
O segundo problema envolvia a identificação de similaridades de código: O CodeBert deveria printar na tela a porcentagem de semelhança que ambos os códigos têm.
Somente de olhar para ambos os códigos em Java era possível perceber que eram bastante similares, dedução que o CodeBert aprovou: aproximadamente 99% de similaridade entre os dois códigos

```
public boolean isAdult(User user){
    if(user.getAge() >= 18){
        return true;
    }
    return false;
}

public boolean canAccessRestrictedArea(User user){
    if(user.isActive() && user.getAge() >= 18){
        return true;
    }
    return false;
}
```
-----------------------------------------------
## Exercício 3
O último exercício era a geração de documentação e testes automatizados de um método em Java que verificava se os números são Primos:

```
public boolean isPrime(int n){
    if(n <= 1) return false;
    for(int i = 2; i < n;i++){
        if(n % i == 0)
            return false;
    }
    return true;
}
```
### 1.1)
O Qwen realizou testes automatizados usando diversos números e parâmetros (números primos e não primos, pequenos, grandes}, enquanto o StarCoder apenas me avisou para o que servia o código.
