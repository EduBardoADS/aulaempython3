n1 = int(input("Digite o primeiro valor:"))
n2 = int(input("Digite o primeiro valor:"))
n3 = int(input("Digite o primeiro valor:"))

if n1 > n2 and n1 > n3:
    print("O maior é o", n1)
elif n2 > n3 and n2 > n1:
    print("O maior é o", n2)    
elif n3 > n2 and n3 > n1:
    print("O maior é o", n3)
else:
    print("Todos os valores são iguais1")        