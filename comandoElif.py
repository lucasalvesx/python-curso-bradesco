# existe tambem o comando ELIF, que avalia as expressoes intermediarias que vem antes do comando ELSE

idade = int (input("Qual a sua idade: "))
if idade >=18:
    print ("Eh adulto")
elif idade >16:
    print ("Eh adolescente etc")
else:
    print ("Crianca")