# adição, subtração, multiplicação e divisão
if __name__ == "__main__":
    print("inicio do projeto")

    primeiro_num = float(input("Digite o primeiro número da operação:"))
    segundo_num = float(input("Digite o segundo número da operação:"))


    print("Qual operação deseja realizar? Entre as opçôes + - * / ")
    print("1 - adição(+)")
    print("2 - subtração(-)")
    print("3 - multiplicação(*)")
    print("4 - divisão(/)")
    print("0 - sair do programa")

    operacao = input()
    print(operacao)

    if operacao == "1":
        total = primeiro_num + segundo_num
        print(f"{primeiro_num} + {segundo_num} = {total}")
    elif operacao == "2":
        print(primeiro_num - segundo_num)
    elif operacao == "3":
        print(primeiro_num * segundo_num)
    elif operacao == "4":
        print(primeiro_num / segundo_num)
    elif operacao != "0": 
        print("Erro - Valor digitado diferente das opções válidas")    
    else:
        print("Fechando programa")
