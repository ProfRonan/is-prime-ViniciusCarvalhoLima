num = int(input("Digite um Numero:\n"))
if num <= 0:
    print("Número inválido")
if num > 1:
 
    for i in range(2, num):
 
      
        if (num % i) == 0:
            print("Não primo")
            break
    else:
        print("Primo")
 
else:
    print("Não primo")