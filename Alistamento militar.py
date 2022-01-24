from datetime import date
atual = date.today().year
nome = input('Digite seu nome: ')
anonasc = int(input('Digite seu ano de nascimento: '))
idade = atual - anonasc
print(f'Quem nasceu em {anonasc} tem {idade} no anos de idade.')

if idade == 18:
    print('Você deve se alistar imediatamente, pois pra você é obrigatório!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para você se alistar!')
elif idade > 18:
    saldo = idade - 18
    print(f'Você deveria ter se alistado a {saldo} anos.')