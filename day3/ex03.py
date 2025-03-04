area = input("Você quer seguir para área de 'Front-End' ou de 'Back-End'? Digite o nome da área: ").strip()
linguagem = ""

if area.lower() == "front-end":
    linguagem = input("Você quer aprender React ou Vue? ").strip()
elif area.lower() == "back-end":
    linguagem = input("Você quer aprender C# ou Java? ").strip()
else:
    print("Você não inseriu uma área válida!")

especialidade_ou_fullstack = input("Digite 1 para seguir se especializando na área escolhida ou 2 para seguir se desenvolvendo para se tornar Fullstack: ").strip()

if especialidade_ou_fullstack == "1":
    print(f"Continue se especializando em {linguagem} para dominar a área de {area}!")
elif especialidade_ou_fullstack == "2":
    print(f"Chegou a hora de começar a aprender outras linguagens além de {linguagem} se você quer se tornar Fullstack!")
else:
    print("Você não inseriu um valor válido!")

msg = input("Tem mais alguma tecnologia que você gostaria de aprender? Digite 'ok' em caso positivo: ").strip().lower()
while msg == "ok":
    nova_tecnologia = input("Qual? ").strip()
    print(f"{nova_tecnologia} é realmente uma tecnologia muito legal!")
    msg = input("Tem mais alguma tecnologia que você gostaria de aprender? Digite 'ok' em caso positivo: ").strip().lower()

print("Bons estudos!")
