lista = ["318.594.220-70","827.153.910-60","043.287.650-21",'612.470.330-32','701.259.410-05',
         '456.127.980-19',"173.658.240-84",'592.471.830-57',"830.126.470-41","248.305.690-12","173.658.240-84"
         ]

#  fazer a entrega em ordem crescente
lista.sort()
cpf_unicos = set()
# limpeza e validação nos CPFs 
    # (remover ponto e traço

for cpf in lista:
    cpf_formatado = cpf.replace(".", "").replace("-","")

    #  verificar se tem 11 dígitos
    if len(cpf_formatado) == 11:
    #  e não deixar valores duplicados)        
        if cpf_formatado in cpf_unicos:
          print(f"O cpf {cpf_formatado} já existe! duplicado")  
        else:
            cpf_unicos.add(cpf_formatado)
            print(f"o cpf {cpf_formatado} está valido e foi adicionado")
    else:
         print(f"O CPF {cpf_formatado} é inválido! (não tem 11 dígitos)")
        

