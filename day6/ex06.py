frutas = []
laticinios = []
doces = []
congelados = []

while True:
    if not frutas and not laticinios and not doces and not congelados:
        adicionar_mais = input("Você deseja adicionar uma comida na lista de compras? Responda 'sim' ou 'não': ").strip().lower()
    else:
        adicionar_mais = input("Você deseja adicionar uma comida na lista de compras? Responda 'sim', 'não' ou 'remover': ").strip().lower()

    while adicionar_mais not in ["sim", "não", "remover"]:
        print("Operação não reconhecida!")
        adicionar_mais = input("Você deseja adicionar uma comida na lista de compras? Responda 'sim', 'não' ou 'remover': ").strip().lower()

    if adicionar_mais == "não":
        break

    if adicionar_mais == "sim":
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

    elif adicionar_mais == "remover":
        if not frutas and not laticinios and not doces and not congelados:
            print("A lista está vazia!")
        else:
            print("\nLista de compras:")
            print(f"  Frutas: {', '.join(frutas)}")
            print(f"  Laticínios: {', '.join(laticinios)}")
            print(f"  Doces: {', '.join(doces)}")
            print(f"  Congelados: {', '.join(congelados)}\n")
            
            remover = input("Qual produto você deseja remover? ").strip()

            if remover in frutas:
                frutas.remove(remover)
                print(f"O item {remover} foi removido com sucesso!")
            elif remover in laticinios:
                laticinios.remove(remover)
                print(f"O item {remover} foi removido com sucesso!")
            elif remover in doces:
                doces.remove(remover)
                print(f"O item {remover} foi removido com sucesso!")
            elif remover in congelados:
                congelados.remove(remover)
                print(f"O item {remover} foi removido com sucesso!")
            else:
                print("Não foi possível encontrar o item dentro da lista!")

print("\nLista final de compras:")
print(f"  Frutas: {', '.join(frutas)}")
print(f"  Laticínios: {', '.join(laticinios)}")
print(f"  Doces: {', '.join(doces)}")
print(f"  Congelados: {', '.join(congelados)}")
