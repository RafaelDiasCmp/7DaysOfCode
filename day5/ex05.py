frutas = []
laticinios = []
doces = []
congelados = []

while True:
    adicionar_mais = input("Você deseja adicionar uma comida na lista de compras? Responda 'sim' ou 'não': ").strip().lower()

    while adicionar_mais not in ["sim", "não"]:
        print("Operação não reconhecida!")
        adicionar_mais = input("Você deseja adicionar uma comida na lista de compras? Responda 'sim' ou 'não': ").strip().lower()

    if adicionar_mais == "não":
        break

    comida = input("Qual comida você deseja inserir? ").strip()
    categoria = input("Em qual categoria essa comida se encaixa: 'frutas', 'laticínios', 'doces' ou 'congelados'? ").strip().lower()

    if categoria == "frutas":
        frutas.append(comida)
    elif categoria == "laticínios":
        laticinios.append(comida)
    elif categoria == "doces":
        doces.append(comida)
    elif categoria == "congelados":
        congelados.append(comida)
    else:
        print("Essa categoria não foi pré-definida.")

print(f"\nLista de compras:\n  Frutas: {', '.join(frutas)}\n  Laticínios: {', '.join(laticinios)}\n  Doces: {', '.join(doces)}\n  Congelados: {', '.join(congelados)}")
