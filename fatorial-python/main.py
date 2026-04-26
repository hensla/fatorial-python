n = -1
 
while n < 0:
    n = int(input("Digite o número que deseja ver o fatorial: "))
 
if n == 0 or n == 1:
    print(f"O fatorial de {n}! = 1")
 
else:
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    print(f"O fatorial de {n}! = {resultado}")