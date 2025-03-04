# Funções para as operações
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

# Função principal para a calculadora
def calculadora():
    while True:
        operacao = input("Escolha uma operação: soma, subtração, multiplicação, divisão ou sair: ").strip().lower()

        if operacao == "sair":
            print("Até a próxima!")
            break

        if operacao not in ["soma", "subtração", "multiplicação", "divisão"]:
            print("Operação inválida. Tente novamente.")
            continue

        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))

        if operacao == "soma":
            resultado = soma(numero1, numero2)
        elif operacao == "subtração":
            resultado = subtracao(numero1, numero2)
        elif operacao == "multiplicação":
            resultado = multiplicacao(numero1, numero2)
        elif operacao == "divisão":
            resultado = divisao(numero1, numero2)

        print(f"O resultado de {operacao} é: {resultado}")

# Inicia a calculadora
calculadora()
