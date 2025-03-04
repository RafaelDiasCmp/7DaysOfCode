// Funções para as operações
function soma(a, b) {
    return a + b;
}

function subtracao(a, b) {
    return a - b;
}

function multiplicacao(a, b) {
    return a * b;
}

function divisao(a, b) {
    if (b === 0) {
        return "Erro: Divisão por zero!";
    }
    return a / b;
}

// Função principal para a calculadora
function calculadora() {
    let operacao;
    
    while (true) {
        operacao = prompt("Escolha uma operação: soma, subtração, multiplicação, divisão ou sair:");

        if (operacao === "sair") {
            alert("Até a próxima!");
            break;
        }

        if (operacao !== "soma" && operacao !== "subtração" && operacao !== "multiplicação" && operacao !== "divisão") {
            alert("Operação inválida. Tente novamente.");
            continue;
        }

        let numero1 = parseFloat(prompt("Digite o primeiro número:"));
        let numero2 = parseFloat(prompt("Digite o segundo número:"));

        let resultado;

        if (operacao === "soma") {
            resultado = soma(numero1, numero2);
        } else if (operacao === "subtração") {
            resultado = subtracao(numero1, numero2);
        } else if (operacao === "multiplicação") {
            resultado = multiplicacao(numero1, numero2);
        } else if (operacao === "divisão") {
            resultado = divisao(numero1, numero2);
        }

        alert(`O resultado de ${operacao} é: ${resultado}`);
    }
}

// Inicia a calculadora
calculadora();
