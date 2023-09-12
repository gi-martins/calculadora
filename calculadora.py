import os #biblioteca para limpeza de terminal
import platform #biblioteca para pegar tipo do sistema operacional


def exibir_resultado(num1: float, num2: float, operacao: str, total: float) -> None:
    print(f"{num1} {operacao} {num2} = {total}\n")


def somar(n1: float, n2: float) -> None:
    total = n1 + n2
    exibir_resultado(n1, n2, "+", total)


def subtrair(n1: float, n2: float) -> None:
    total = n1 - n2
    exibir_resultado(n1, n2, "-", total)


def multiplicar(n1: float, n2: float) -> None:
    total = n1 * n2
    exibir_resultado(n1, n2, "*", total)


def dividir(n1: float, n2: float) -> None:
    total = n1 / n2 
    exibir_resultado(n1, n2, "/", total)


def exibir_menu() -> None:
    print("Qual operação deseja realizar?")
    print("1 - adição")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")
    print("0 - sair do programa")


def limpar_terminal() -> None:
    sistema_operacional = platform.system()
    if sistema_operacional == "Windows": 
        os.system("cls")
    else:
        os.system("clear")    


if __name__ == "__main__":
    print("Calculadora")

    while True: 
        exibir_menu()
        
        operacao = input("Operação: ")

        limpar_terminal()

        if operacao == "0": 
            print("Fechando Programa")
            break
        elif operacao not in ("1", "2", "3", "4"): 
            print("Opção inválida")
            continue

        primeiro_num = float(input("Digite o primeiro número da operação: "))
        segundo_num = float(input("Digite o segundo número da operação: "))

        if operacao == "1":
            somar(primeiro_num, segundo_num)
        elif operacao == "2":
            subtrair(primeiro_num, segundo_num)
        elif operacao == "3":
            multiplicar(primeiro_num, segundo_num)            
        elif operacao == "4":
            dividir(primeiro_num, segundo_num)
