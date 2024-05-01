# exemplo usando estrutura de decisao composta

# variaveis pedindo para user atribuir valor
# variavel = tipo(input("texto"))
NotaA = float(input("Informe a primeira nota"))
NotaB = float(input("Informe a segunda nota"))

# processamento ---- calcular a media
mediafinal = (NotaA + NotaB / 2)

# verificacao de condicao
if mediafinal >= 7.0 :
    print("A media %.1f - Aprovado, parabens!" % mediafinal)
else:
    print("A media %.1f - Insuficiente, está de recuperação " % mediafinal)
    
    

