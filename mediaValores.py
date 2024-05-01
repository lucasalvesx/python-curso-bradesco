qtd = 0
soma = 0
media = 0
valor = float(input("Insira o valor: "))

while (valor > 0.0 ):
    soma = soma + valor
    qtd = qtd + 1
    # entrada de valores 
    valor = float(input("Insira um valor: "))
    
# se o valor for negativo o laco encerra
media = soma / qtd 
print("\nTotal da soma: ", soma )
print("\n Quantidade d valores digitados: ", qtd)
print("\nMedia dos valores: ", media)

# um algoritmo para voce inserir numeros, que vao ser somados
# dizer quantos valores vc inseriu (geralmente 3, ne)
# e calcular a media desses numeros ae