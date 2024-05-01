# quando vamos pedir entrada de dados <> tipo string, precisamos que converter o TIPO de dado que será inserido

# variavel = tipo(input ("Solicitaçao ao usuario"))
codigo = int(input ("Insira o codigo desejado: "))

# nesse caso o dado é tipo string, entao n eh necessario
nome = input("Diga o nome do funcionario: ")

# mesmo modelo da primeira variavel
salario = float(input ("Qual o salario dele? "))

# declaracao de valor booleano
ativo = True

# impressao de resultados
print("Codigo: %d " % codigo)
print("Nome: %s " % nome)
print("Salario: %.2f " % salario)
print("Ativo: %r " % ativo)
