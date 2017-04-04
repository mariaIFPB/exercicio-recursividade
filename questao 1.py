#escreva uma função recursiva que imprima de um numero x até um número y.
n = int(input("informe o número a ser exibido: "))
def exibir(n):
  if (n<=n and n>=0):
    print(n)
    return exibir(n-1)

exibir(n)
