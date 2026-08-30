horas_trabalahadas = float(input("Digite o quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor por hora: "))
desconto = float(input("Digite o percentual de desconto: "))
numero_dependentes = float(input("Digite o numero de dependentes:"))
salario_bruto = horas_trabalahadas*valor_por_hora
valor_com_desconto = (salario_bruto*desconto)/100 
salario_liquido = salario_bruto - valor_com_desconto
dependentes = numero_dependentes*100
Salario_final = salario_liquido+dependentes
print("Salario a receber: ", Salario_final)

