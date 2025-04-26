dict_1 = {
  "nome": ["Amanda Costa", "Bruno Ribeiro", "Camila Ferreira", "Diego Martins", "Eduarda Lima"],
  "email": ["amanda.costa@techconf.com", "bruno.ribeiro@techconf.com", "camila.ferreira@techconf.com", "diego.martins@techconf.com", "eduarda.lima@techconf.com"],
  "enviado": ["true", 'false', "true", 'false', 'false']
}

dict_2 = {
  "nome": ["Felipe Alves", "Gustavo Silva", "Helena Souza", "Igor Fernandes", "Juliana Castro"],
  "email": ["felipe.alves@businessconf.com", "gustavo.silva@businessconf.com", "helena.souza@businessconf.com", "igor.fernandes@businessconf.com", "juliana.castro@businessconf.com"],
  "enviado": ['false', 'true', 'false', 'true', 'false']
}

lista_1 = list(zip(dict_1["nome"], dict_1["email"], dict_1["enviado"]))
lista_2 = list(zip(dict_2["nome"], dict_2["email"], dict_2["enviado"]))

lista_3 = lista_1 + lista_2

email = [email for nome, email, enviado in lista_3 if enviado == 'false']
print(email)

email_pendente = [email for nome, email, enviado in lista_3 if enviado == 'true']
print(email_pendente)

for nome, email, enviado in lista_3:
    if enviado == 'false':
        print(f"{nome} precisa receber o e-mail ({email})")

