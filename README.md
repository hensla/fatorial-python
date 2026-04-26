➗ fatorial-calculator
Ferramenta simples em Python que calcula o fatorial de um número inteiro não negativo digitado pelo usuário.
📋 Descrição
fatorial-calculator solicita um número ao usuário e exibe o resultado do seu fatorial. Caso o número seja negativo, solicita novamente até receber um valor válido.
🚀 Como usar
bashpython main.py
Exemplo de execução:
Digite o número que deseja ver o fatorial: 5
O fatorial de 5! = 120
Digite o número que deseja ver o fatorial: -3
Digite o número que deseja ver o fatorial: 0
O fatorial de 0! = 1
🐛 Código
pythonn = -1

while n < 0:
    n = int(input("Digite o número que deseja ver o fatorial: "))

if n == 0 or n == 1:
    print(f"O fatorial de {n}! = 1")

else:
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    print(f"O fatorial de {n}! = {resultado}")
💡 Como funciona

Fica em loop enquanto o número digitado for negativo, garantindo uma entrada válida.
Se n for 0 ou 1, retorna 1 diretamente (caso base do fatorial).
Caso contrário, multiplica todos os inteiros de 2 até n usando um laço for.
Exibe o resultado formatado no terminal.

📁 Estrutura do projeto
fatorial-calculator/
└── main.py   # Script principal
🛠️ Requisitos

Python 3.x
Nenhuma biblioteca externa necessária

📄 Licença MIT
