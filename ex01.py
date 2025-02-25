numero_um = 1
string_um = '1'
numero_trinta = 30
string_trinta = '30'
numero_dez = 10
string_dez = '10'

if numero_um == int(string_um) and type(numero_um) != type(string_um):
    print('As variáveis numero_um e string_um têm o mesmo valor, mas tipos diferentes')
else:
    print('As variáveis numero_um e string_um não têm o mesmo valor')

if numero_trinta == int(string_trinta) and type(numero_trinta) == type(string_trinta):
    print('As variáveis numero_trinta e string_trinta têm o mesmo valor e mesmo tipo')
else:
    print('As variáveis numero_trinta e string_trinta não têm o mesmo tipo')

if numero_dez == int(string_dez) and type(numero_dez) != type(string_dez):
    print('As variáveis numero_dez e string_dez têm o mesmo valor, mas tipos diferentes')
else:
    print('As variáveis numero_dez e string_dez não têm o mesmo valor')
