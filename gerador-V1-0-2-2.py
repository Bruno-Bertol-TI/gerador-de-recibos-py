import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime

def gerar_recibo(nome_beneficiado, nome_pagador, valor, descricao_1, descricao_2 , data, nome_arquivo, n_recibo):
    
    largura, altura = A4

    c = canvas.Canvas(nome_arquivo, pagesize=A4)
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(largura / 2, altura - 50, "RECIBO DE PAGAMENTO")

    c.drawString

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, altura - 50, f"RECIBO N°: {n_recibo}")

    c.setFont("Helvetica", 12)
    c.drawString(50, altura - 100, f"Eu, {nome_beneficiado}. ")

    c.drawString(50, altura - 120, f"Declaro que estou recebendo de: {nome_pagador},")

    c.drawString(50, altura - 140, f"a importancia da quantia de: R$ {valor}") 

    c.drawString(50, altura - 160, f"por ter prestado o(s) serviço(s) de: {descricao_1}") 

    if (descricao_2 and descricao_2.strip()):
        c.drawString(50, altura - 180, f"{descricao_2}") 
        c.drawString(50, altura - 200, f"na data: {data}")
    else:
        c.drawString(50, altura - 180, f"na data: {data}")

    c.drawString(50, altura - 250, f"Local: ________________________________________, na data: _____/___________/_____.")
    c.drawString(50, altura - 300, f"Assinatura:____________________________________")

    c.save()
    print(f"recibo salvo como: {nome_arquivo}")

def coleta_informacao(qtd_rep):

    i = 1
    for i in range(1, qtd_rep + 1, 1):

        os.system('cls')

        n_recibo = i
        if n_recibo > 99:
            n_recibo = f"{n_recibo}"
        elif 9 < n_recibo < 99:
            n_recibo = f"0{n_recibo}"
        else:
            n_recibo = f"00{n_recibo}"

        print(f"Coleta de informações para recibo N°: {n_recibo}\n")


        nome_beneficiado = str(input("Digite o nome de quem está recebendo: "))
        print(f"{nome_beneficiado} --> salvo!\n")
        nome_pagador = str(input("Digite o nome de quem está pagando: "))
        print(f"{nome_pagador} --> salvo!\n")
        quantia_paga = float(input("Digite o valor recebido, sem ponto e sem virgulas!: "))
        print(f"{quantia_paga} --> salvo!\n")
        
        descricao = str(input("Descreva o serviço prestado: "))
        descricao_1 = ''
        descricao_2 = ''
        if len(descricao) < 59:
            k = 0
            for k in range(0, 59, 1):
                descricao_1 += descricao[k]
        elif len(descricao) > 59:
            j = 59
            for j in range(59, len(descricao), 1):
                descricao_2 += descricao[j]
        print(f"Descrição salva e formatada com sucesso\n")
        
        data_recibo = input("Digite a data do recibo no formato (DD/MM/AAAA): ")
        try:
            data_recibo_formatada = datetime.strptime(data_recibo, "%d/%m/%Y")
            print(f"Data Válida: {data_recibo_formatada.strftime('%d/%m/%Y')}")
            data_recibo_formatada_print = data_recibo_formatada.strftime('%d/%m/%Y')
            print(f"{data_recibo_formatada_print} --> salvo!\n")
        except ValueError:
            print("Formato de data inválido. por favor, use DD/MM/AAAA")

        nome_arquivo = f'recibo_{nome_pagador}_{n_recibo}.pdf'
        print(f"Recibo n°: {n_recibo} --> salvo! --> nome do arquivo: {nome_arquivo}\n")

        gerar_recibo(nome_beneficiado, nome_pagador, quantia_paga, descricao_1, descricao_2, data_recibo_formatada_print, nome_arquivo, n_recibo)

        print(f"Recibo N°: {n_recibo} criado")

    print("Recibos criados!")
                
def main():

    while True:
        os.system('cls')
        print("Gerador de Recibos V1.0.2.2")
        print("Selecione uma das opções abaixo:")
        print()
        print("[1] CADASTRAR VARIOS")
        print("[2] CADASTRAR UM")
        print("[3] SAIR")
        opcao_selecionada = int(input("Escolha uma das opções: "))
        os.system('cls')
        qtd_recibos = 0

        if opcao_selecionada != 1 and opcao_selecionada != 2:
            break
        elif opcao_selecionada == 2:
            print("Vamos cadastrar seu recibo: ")
            qtd_recibos = 1
            coleta_informacao(qtd_recibos)
        else:
            print("Você escolheu gerar varios recibos!")
            print("Digite um numero inteiro!")
            qtd_recibos = int(input("Digite a quantidade de recibos que deseja cadastrar: "))
            coleta_informacao(qtd_recibos)


        break

if (__name__ == '__main__'):

    main()