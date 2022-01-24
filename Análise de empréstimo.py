nome = input('Digite seu nome: ')
renda = float(input('Digite a sua renda: R$ '))
idade = int(input('Digite a sua idade: '))
porcent = renda * 0.3

if renda >= 1300 and idade >= 18:
    print(f'Seu empréstimo pré aprovado é de {porcent}. Para contratar, procure o gerente.')
elif renda <= 1299 and idade <= 17:
    print('Seu empréstimo precisa ser analisado pelo gerente da sua conta. ')
else:
    print('Infelizmente seu empréstimo não será aprovado.')