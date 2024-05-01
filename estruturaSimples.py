# pedindo ao usuario para atribuir valores as variaveis
A = input("Atribua um valor à variavel A: ")
B = input("Atribua um valor à variavel B: ")

# condicoes - importante se atentar a identacao 

if (A > B): #se o valor inserido para A for maior que o para B,
    aux = A;    
    A = B;  
    B = aux;    
    
    # uma técnica comum para trocar os valores de duas variáveis sem precisar de uma 
    # variável temporária adicional. O valor de A é armazenado temporariamente em aux, 
    # então o valor de A é substituído pelo valor de B e, finalmente, o valor de aux 
    # (que é o valor original de A) é atribuído a B.
    
    # aux eh a variavel auxiliar

print("O valor de A agora eh: ", A)
print("O valor de B agora eh: ", B)
