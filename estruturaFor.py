# usamos a estrutura FOR quando sabemos quantas vezes o laço de programação deverá ser executado

#contar de 0 a 10
for n in range (10):
    print(n)
    
# a variavel N eh inicialmente ajustada com o valor 0 (padrao)
# enquanto n for menor do que 10 (condicao), o comando PRINT eh executado

# essa condicao eh adicionada com o comando RANGE 

# a variavel N eh adicionada com 1 (valor padrao) e vai testando na 
# execucao se o novo valor ainda eh menor que 10

# isso se repete ate que o valor de N seja >= 10

# quando isso acontece, o laço eh encerrado e o algoritmo segue as
# instrucoes do bloco de repeticao (no caso PRINT (N))

# agora veremos diferente, determinando um valor inicial fora do padrao
for n in range(5, 16):
    print(n)
# vai contar de 5 ate 15.

# tambem podemos fazer o DECREMENTO, que eh contar no inverso
for n in range(10,0,-1):
    print(n)
# vai contar de 10 ate 1

