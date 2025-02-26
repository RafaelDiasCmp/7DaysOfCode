# 🧠 Desafio #7DaysOfCode - Dia 1: Comparações de Variáveis em JavaScript e Python

Este repositório contém a solução do desafio **#7DaysOfCode** da Alura, abordando temas essenciais na programação.

## 1º Dia **Comparações de Variáveis**.  
## 🔍 Descrição do Desafio

No primeiro dia, o foco foi entender como o **JavaScript** e o **Python** tratam a igualdade entre variáveis, com ênfase nas diferenças entre:
- `==` (igualdade de valor com conversão implícita de tipo) e 
- `===` (igualdade estrita de valor e tipo) em JavaScript.
- Comparações com `==` em Python, que consideram valor e tipo.  

O desafio mostrou como essas sutilezas podem gerar comportamentos inesperados, como nos exemplos:  
```js
console.log(false == '0');  // true
console.log(null == undefined);  // true
console.log(" \t\r\n" == 0);  // true
console.log(' ' == 0);  // true
```

### 💡 O que Aprendi  
- As diferenças fundamentais entre `==` (igualdade de valor com conversão implícita de tipo) e `===` (igualdade estrita de valor e tipo) em **JavaScript**.  
- Como evitar problemas de conversão implícita de tipo em **JavaScript**, utilizando `===` e `!==`.  
- Em **Python**, o operador `==` já compara valor e tipo, mas é importante usar conversões explícitas com `int()` ou `str()` para garantir comparações corretas.  
- A importância de entender como cada linguagem trata os **tipos de variáveis** para evitar bugs inesperados e escrever códigos mais confiáveis.

## 2º Dia **Entrada e Saída de dados com Variáveis**.  
## 🔍 Descrição do Desafio  

O desafio propôs criar um script que utilizasse **inputs do usuário** para gerar uma experiência interativa. No **Python**, isso é feito com `input()`, enquanto no **JavaScript** utilizamos `prompt()`.  
O código também precisava utilizar um **controle de fluxo** com `if...else` para personalizar a resposta com base na opinião do usuário sobre a linguagem de programação escolhida. 

```js
const prompt = require('prompt-sync')();

const nome = prompt('\nQual seu nome? ');
const idade = prompt('\nQuantos anos você tem? ');
const linguagem = prompt('\nQual linguagem de programação você está estudando? ');

console.log(`\nOlá ${nome}, você tem ${idade} anos e já está aprendendo ${linguagem}!`);

const gosto_linguagem = parseInt(prompt(`\nVocê gosta da linguagem ${linguagem}? 1 para SIM // 2 para NÃO `));

if (gosto_linguagem === 1) {
    console.log(`\nMuito bom ${nome}! Continue estudando e você terá muito sucesso`);
} else {
    console.log(`\nAhh que pena ${nome}... Já tentou aprender outras linguagens?`);
}
---

### 📚 Referências  
- [Documentação do JavaScript (MDN)](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)  
- [Documentação do Python](https://docs.python.org/3/)  
- [#7DaysOfCode da Alura](https://www.alura.com.br/challenges)  

