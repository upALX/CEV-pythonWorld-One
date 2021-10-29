# Escreva um programa que pergunta qual o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Salários inferiores ou iguais, aumento de 15%.

salaryValue = float(input('Olá, por favor informe o seu sálario: '))
salaryValueTen = (salaryValue + salaryValue * 0.10)
salaryValueFifteen = (salaryValue + salaryValue * 0.15)

if salaryValue > float(1.250):
    print('Você recebeu um aumento de 10%, seu salário que era R${:.2f} passa a valer R${:.2f}, uma diferença de R${:.2f}.'.format(salaryValue, salaryValueTen, (salaryValueTen - salaryValue )))
else:
    print('Você recebeu um aumento de 15%, seu salário que era R${:.2f} passa a valer R${:.2f}, uma diferença de R${:.2f}.'.format(salaryValue, salaryValueFifteen, (salaryValueFifteen - salaryValue)))
