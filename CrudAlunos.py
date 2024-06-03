name_list = []
nome = ""

def create (nome):
    
    comparador = []

    if name_list == []:
        name_list.append(nome.strip())
        print("\nAluno cadastrado com sucesso!\n")
    
    else:

        for i in name_list:
            comparador.append(i.lower())

        if (nome.lower() in comparador):
            print("\nEsse nome de aluno já está cadastrado!\nTente outro nome")

        elif(nome.lower() not in comparador):      
            name_list.append(nome.strip())
            print("\nAluno cadastrado com sucesso!\n")
        
        else:
            print("Erro inesperado")
            
def remove (nome):

    comparador = []

    if name_list == []:
        print("\nNenhum aluno cadastrado\n")
   
    else:
    
        for i in name_list:
            comparador.append(i.lower())    

        if (nome.lower() in comparador):
            name_list.remove(nome)
            print("\nNome removido com sucesso!")   
        
        elif(nome.lower() not in comparador):      
            print("\nAluno não encontrado\n")

        else:
            print("Erro inesperado")

def update (nome):

    comparador = []

    if name_list == []:
        print("\nNenhum aluno cadastrado\n")
    
    else:
        
        for i in name_list:
            comparador.append(i.lower())

        if (nome.lower() in comparador):

            i = 0

            for item in name_list:

                if (item.lower() == nome.lower()):

                    nome = input("Insira o novo aluno:\n")
                    name_list[i] = nome
                    print("\nNome atualizado com sucesso!")

                else:
                    i += 1

        elif(nome.lower() not in comparador):      
            print("\nAluno não encontrado\n")
        
        else:
            print("Erro inesperado")

def read ():

    for i in name_list:
        print(i)

while True:

    print("""|-------Crud Alunos-------|
Escolha uma função:
1 - Adicionar nome de aluno
2 - Remover nome de aluno
3 - Atualizar nome de aluno
4 - Listar todos os alunos
9 - Encerrar sessão
|-------------------------|""")

    opt = int(input())

    if (opt == 1):

        print("|----Adicionar Aluno----|\n")

        nome = input("Escreva o nome do Aluno:\n")
        create(nome)
        

    if (opt == 2):

        print("|----Remover Aluno----|\n")

        nome = input("Escreva o nome do Aluno:\n")
        remove(nome)

    if (opt == 3):

        print("|----Atualizar Aluno----|\n")

        nome = input(f"Alunos:{name_list}\nEscreva o nome do aluno que deseja atualizar:\n")
        update(nome)

    if (opt == 4):

        print("|----Listar Alunos----|\n")

        read()

    if (opt == 9):

        print("Encerrando.....")
        break
