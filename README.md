# UCP-IA-2026

## Exercício 1 ------

### 1.1)
Exercício foi a análise de um código Java que realizava uma divisão:
public int divide(int a, int b){
       return a / b;
}

usando o prompt "Analyze the following Java code and point out any issues, correcting them as well:", o Qwen respondeu com precisão, apontando o erro caso a variável b fosse igual a 0, causando um ArithmeticException, bem como outras possíveis melhorias: entre elas a mudança do tipo das variáveis para "double" para maior precisão.

Tendo em vista que o StarCoder é um modelo de AutoComplete de um code ele não gerou uma análise do texto 
---------------------------------------------
### 1.2)
A segunda parte do exercício foi a correção do código

A correção feita por ambas as IA's estão corretas, consertando o problema no caso de b=0, porém o Qwen utilizou do math.ceil() e de variáveis "double" para arrendondar para retornar o valor, enquanto o Starcoder usou return(a/b), sendo mais direto ao ponto.

----------------------------------------------
## Exercício 2 
