# UCP-IA-2026

## Exercício 1 

### 1.1)
Exercício foi a análise de um código Java que realizava uma divisão:

```java
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

```java
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

```java
public boolean isPrime(int n){
    if(n <= 1) return false;
    for(int i = 2; i < n;i++){
        if(n % i == 0)
            return false;
    }
    return true;
}
```
### 3.1)
O Qwen realizou testes automatizados usando diversos números e parâmetros (números primos e não primos, pequenos, grandes}, enquanto o StarCoder se mostrou mais suscinto em suas respostas, apenas explicando o que o código faz

### 3.2)
Em ambos os casos não houve geração de documentação, eu não sei o que eu fiz de errado
-------------------------------
# Rodando via API

## Exercício 1
O exercício foi uma repetição do 1°, porém replicando o experimento usando uma LLM via API
```text
The provided Java code has a few issues:

1. **Division by Zero Error**: The code does not handle the case where `b` is zero. In Java, attempting to divide by zero will throw an `ArithmeticException`.
To fix this, you should add a check to ensure that `b` is not zero before performing the division.
2. **Integer Division**: The code performs integer division, which means that any fractional part of the result will be truncated.
If you want to perform floating-point division, you should cast one or both of the operands to a floating-point type (such as `double`).
3. **Missing Exception Handling**: The code does not include any exception handling mechanisms.
In a real-world application, you would want to handle potential exceptions that may occur during the execution of the code.
4. **Syntax Error**: The code has a syntax error due to an extra semicolon (`;`) at the end of the return statement.
The corrected return statement should be `return a / b;`
```
### 1.1) 
Apontou corretamente o problema no caso de b = 0. Apontou também outros problemas de performance como no caso de divisão de números decimais ou inteiros.

### 1.2)
```java
public int divide(int a, int b) {
    if (b == 0) {
        throw new ArithmeticException("Cannot divide by zero");
    }
    return a / b;
}
```

Alternatively, you can use a try-catch block to handle the ´ArithmeticException`:

```java
public int divide(int a, int b) {
    try {
        return a / b;
    } catch (ArithmeticException e) {
        System.out.println("Error: " + e.getMessage());
        return 0; // or some other default value
    }
}
```
## Exercício 2
Repetição do exercício 2 da primeira parte, porém, utilizando do Llama via API

### 1.1) 
```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
```
Testes automatizados do código foram gerados.

### 1.2)
### Documentação para o Método `isPrime`

```java
/**
 * Verifica se um número inteiro é primo.
 * 
 * Um número é considerado primo se for maior que 1 e não tiver divisores além de 1 e ele mesmo.
 * 
 * @param n o número a ser verificado
 * @return true se o número for primo, false caso contrário
 */
public boolean isPrime(int n) {
    // Implementação corrigida
}
```
Documentação do código gerada, apontando como o código funciona.

### 1.3)
### Mensagem de Commit

```
Ajuste e otimização do método isPrime

* Corrigido loop interno desnecessário e variável repetida
* Implementado testes automáticos para casos comuns e de borda
* Adicionada documentação Javadoc para o método isPrime
```
Mensagem de Commit gerada após a correção do código feita pela IA
