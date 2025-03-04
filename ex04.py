import random

numero_adivinhacao = random.randint(0, 10)
acertou = False

for _ in range(3):
    chute = int(input("Tente adivinhar o número de 0 a 10: "))
    if chute == numero_adivinhacao:
        print(f"Parabéns, você acertou! O número era {numero_adivinhacao}.")
        acertou = True
        break
    print("Errado!")

if not acertou:
    print(f"Infelizmente, você não acertou. O número era {numero_adivinhacao}!")
print("Fim do jogo!")