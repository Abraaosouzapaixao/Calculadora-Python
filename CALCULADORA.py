# Função para adição
def add(x, y):
    return x + y

# Função para subtração
def subtract(x, y):
    return x - y

# Função para multiplicação
def multiply(x, y):
    return x * y

# Função para divisão
def divide(x, y):
    return x / y

while True:
    # Exibição das opções de operações
    print("Selecione a operação.")
    print("1.Adicionar")
    print("2.Subtrair")
    print("3.Multiplicar")
    print("4.Dividir")
    print("5.Sair")

    # Solicitação de entrada do usuário
    choice = input("Digite a sua opção (1/2/3/4/5): ")

    # Verifica se o usuário deseja sair
    if choice == '5':
        break

    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    # Execução da operação com base na escolha do usuário
    if choice == '1':
        print(num1,"+",num2,"=", add(num1,num2))

    elif choice == '2':
        print(num1,"-",num2,"=", subtract(num1,num2))

    elif choice == '3':
        print(num1,"*",num2,"=", multiply(num1,num2))

    elif choice == '4':
        print(num1,"/",num2,"=", divide(num1,num2))
    else:
        print("Opção inválida")
        
