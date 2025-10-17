# Variável global para armazenar os dados dos alunos
AlunosCadastrados = {
    "Nomes": [], 
    "1ºNota": [], 
    "2ºNota": [], 
    "3ºNota": []
}

def calcula_status(media):
    if media >= 7:
        return "Aprovado"
    elif 5 <= media < 7:
        return "Recuperação"
    else:
        return "Reprovado"

def cadastro():
    qntCadastro = int(input("Escolha quantos alunos serão cadastrados: "))
    for i in range(qntCadastro):
        nome = input(f"Digite o nome do {i+1}º aluno: ")
        
        nota_Um = float(input("Digite a 1º nota do aluno: "))
        nota_Dois = float(input("Digite a 2º nota do aluno: "))
        nota_Treis = float(input("Digite a 3º nota do aluno: "))

        AlunosCadastrados["Nomes"].append(nome)
        AlunosCadastrados["1ºNota"].append(nota_Um)
        AlunosCadastrados["2ºNota"].append(nota_Dois)
        AlunosCadastrados["3ºNota"].append(nota_Treis)

        media = (nota_Um + nota_Dois + nota_Treis) / 3
        status = calcula_status(media)
        print(f"{nome} - {status}")

def Alunos():
    print("\nLista de Alunos Cadastrados:")
    if len(AlunosCadastrados["Nomes"]) == 0:
        print("Nenhum aluno cadastrado até o momento.")
    else:
        print("="*70)
        print(f"{'Nome':<20} | {'1ª Nota':^7} | {'2ª Nota':^7} | {'3ª Nota':^7} | {'Média':^7} | {'Status':<12}")
        print("-"*70)

        for i in range(len(AlunosCadastrados["Nomes"])):
            nome = AlunosCadastrados["Nomes"][i]
            nota_1 = AlunosCadastrados["1ºNota"][i]
            nota_2 = AlunosCadastrados["2ºNota"][i]
            nota_3 = AlunosCadastrados["3ºNota"][i]
            media = (nota_1 + nota_2 + nota_3) / 3
            status = calcula_status(media)

            print(f"{nome:<20} | {nota_1:^7.2f} | {nota_2:^7.2f} | {nota_3:^7.2f} | {media:^7.2f} | {status:<12}")
        print("="*70)

def main():
    while True:
        print(
            """
              ======================
              1 - Visualizar Alunos
              2 - Cadastro de Aluno
              3 - Sair
              ======================
              """
        )
        choose = int(input("Escolha uma opção (1, 2 ou 3): "))

        if choose == 1:
            Alunos()
        elif choose == 2:
            cadastro()
        elif choose == 3:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente!")

# Rodar o programa
if __name__ == "__main__":
    main()