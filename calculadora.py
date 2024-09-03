from soma import somar
from subtracao import subtrair
from multiplicacao import multiplicar
from divisao import dividir
from resto_divisao import resto_divisao
from mostrar_historico import mostrar_historico

def main():
    historico = []
    while True:
        print("\nBem vindo a Calculadora Proz!")
        print("\nEscolha uma das operações/ações no menu abaixo:")
        print("\n1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Resto da divisão")
        print("6. Mostrar histórico")
        print("7. Sair")

        escolha = input("\nEscolha uma opção: ")

        if escolha == '7':
            print("Obrigado por usar a Calculadora Proz! Até a próxima!")
            break

        if escolha in ['1', '2', '3', '4', '5']:
            try:
              num1 = float(input("Digite o primeiro número: "))
              num2 = float(input("Digite o segundo número: "))

              if escolha == '1':
                  resultado = somar(num1, num2)
                  operacao = f"Soma: {num1} + {num2} = {resultado}"
              elif escolha == '2':
                  resultado = subtrair(num1, num2)
                  operacao = f"Subtração: {num1} - {num2} = {resultado}"
              elif escolha == '3':
                  resultado = multiplicar(num1, num2)
                  operacao = f"Multiplicação: {num1} * {num2} = {resultado}"
              elif escolha == '4':
                  resultado = dividir(num1, num2)
                  operacao = f"Divisão: {num1} / {num2} = {resultado}"
              elif escolha == '5':
                  resultado = resto_divisao(num1, num2)
                  operacao = f"Resto da divisão: {num1} % {num2} = {resultado}"

              print(operacao)
              historico.append(operacao)

            except ValueError:
              print("Por favor, insira números válidos.")
            
            except Exception as e:
              print(f"Erro Inesperado: {e}")

        elif escolha == '6':
            mostrar_historico(historico)

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
