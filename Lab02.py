print("***** Pyhton Calculator *****\n\n")

print("Selecione o número da operação desejada:\n\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n\n")

opcao = int(input("Digite sua opção (1/2/3/4): "))

primeiro_num = input("Digite o primeiro número: ")
segundo_num = input("Digite o segundo número: ")
x = float(primeiro_num)
y = float(segundo_num)

if opcao == 1:
    
    soma = lambda x,y: x+y
    print(soma(x,y))

elif opcao == 2:

    subtracao = lambda x,y: x-y
    print(subtracao(x,y))

elif opcao == 3:
    
    multiplicacao = lambda x,y: x*y
    print(multiplicacao(x,y)) 

elif opcao == 4:

    divisao = lambda x,y: x/y
    print(divisao(x,y)) 

else:
    print("Opção inválida")