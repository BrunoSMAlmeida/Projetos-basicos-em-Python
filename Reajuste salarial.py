salario = float(input('Qual é o salário do funcionário?: R$ '))
porcent_aumento = float(input('De quantos por cento será o reajuste: '))
valor_aumento = salario * porcent_aumento/100
novo_salario = valor_aumento + salario
print(f'O reajuste foi de {porcent_aumento}% que deu {valor_aumento} a mais no salário, totalizando {novo_salario} como novo salário.')
