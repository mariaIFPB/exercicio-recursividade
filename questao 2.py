#escreva uma função recursiva que retorna a soma de n até zero
n = int(input("informe o valor a ser somado: "))
def soma(n):
  if (n==0):
    return n
  return soma(n-1)+n
  
print("a soma de todos os valores até",n, "é: ",soma(n))
