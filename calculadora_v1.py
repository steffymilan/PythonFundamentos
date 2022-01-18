# Calculadora em Python


print("\n******************* Python Calculator *******************")


print("\nSelecione o número da operação desejada: ")

print("\n1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operação = int(input('\nDigite sua opção (1/2/3/4): '))

if operação == 1:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    soma = a + b

    print('O resultado é: %s' %(soma))

elif operação == 2:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    subt = a - b
    print('O resultado é: %s' %(subt))

elif operação == 3:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    mult = a * b
    print('O resultado é: %s' %(mult))

elif operação == 4:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    div = a // b
    print('O resultado é: %s' %(div))

else: 
    print("Opção Inválida!")