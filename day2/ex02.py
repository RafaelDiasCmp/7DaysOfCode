nome = input('\nQual seu nome? ')
idade = input('\nQuantos anos você tem? ')
linguagem = input('\nQual linguagem de porgramação você está estudando? ')

print(f'\nOlá {nome}, você tem {idade} anos e já está aprendendo {linguagem}!')

gosto_linguagem = int(input(f'\nVocê gosta da linguagem {linguagem}? 1 para SIM // 2 para NÃO '))

if gosto_linguagem == 1:
    print(f'\nMuito bom {nome}! Continue estudando e você terá muito sucesso')
else:
    print(f'\nAhh que pena {nome}... Já tentou aprender outras linguagens?')