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

def coleta_informacao(qtd_rep, repetir):

    os.system('cls')
    if repetir != 's':
        gerar_recibo_identicos(qtd_rep, repetir)
    else:
        gerar_recibo_diferentes(qtd_rep)
        
    print("Recibos criados!")

def gerar_recibo_diferentes(qtd_rep):
        for i in range(1, qtd_rep + 1):
            os.system('cls')
            print(f"Coleta de informações para o recibo N°: {padronizar_numero_recibo(i)} \n")
            receber, pagar, valor, descricao_1, descricao_2 = coleta_basica_informacao()
            dia = input("Digite o dia do recibo: ")
            mes = input("Digite o mes do recibo: ")
            ano = input("Digite o ano do recibo: ")
            data = f"{dia}/{mes}/{ano}"
            n_recibo = padronizar_numero_recibo(i)
            nome_arquivo = f"recibo_{pagar}_{n_recibo}.pdf"
            gerar_recibo(receber, pagar, valor, descricao_1, descricao_2, data, nome_arquivo, n_recibo)

def gerar_recibo_identicos(qtd_rep, repetir):
        dias, meses, anos = coleta_datas_recibos_identicos(qtd_rep, repetir)
        receber, pagar, valor, descricao_1, descricao_2 = coleta_basica_informacao()
        for i in range(1, qtd_rep + 1):
            n_recibo = padronizar_numero_recibo(i)
            data = f"{dias[i-1]}/{meses[i-1]}/{anos[i-1]}"
            nome_arquivo = f"recibo_{pagar}_{n_recibo}.pdf"
            gerar_recibo(receber, pagar, valor, descricao_1, descricao_2, data, nome_arquivo, n_recibo)

def coleta_basica_informacao():
    os.system('cls')
    receber = str(input("Digite o nome de quem está recebendo: "))
    print(f"{receber} --> salvo!\n")

    pagar = str(input("Digite o nome de quem está pagando: "))
    print(f"{pagar} --> salvo!\n")

    valor = float(input("Digite o valor recebido, sem ponto e sem virgulas!: "))
    print(f"{valor} --> salvo!\n")

    descricao = str(input("Descreva o serviço prestado: "))
    descricao_1 = ''
    descricao_2 = ''
    if len(descricao) <= 59:
        descricao_1 = descricao
    elif len(descricao) <= 118:
        descricao_1 = descricao[:59]
        descricao_2 = descricao[59:]
    else:
        descricao_1 = descricao[:59]
        descricao_2 = descricao[59:138]  
        print("⚠️ Descrição maior que 138 caracteres. Parte final foi truncada.")

    return receber, pagar, valor, descricao_1, descricao_2

def coleta_datas_recibos_identicos(qtd_rep, repetir): 
    if repetir != 's':
        os.system('cls')

        data_recibo_inicial = input("Digite o mes e ano do inicio do periodo que deseja, no formato (MM/AAAA): ")
        try:
            mes, ano = map(int, data_recibo_inicial.split('/'))
            if 1 <= mes <= 12 and ano > 0:
                print(f"Data Válida: {mes}/{ano}")
        except ValueError:
            print("Formato de data inválido. Por favor, use MM/AAAA")
            return coleta_informacao(qtd_rep, repetir)

        dias, meses, anos = [], [], []

        i = 1
        for i in range(1, qtd_rep + 1):
            os.system('cls')
            print(f"Coleta de informações para o recibo N°: {padronizar_numero_recibo(i)} referente ao mes {mes}/{ano} \n")
            dia = input("Digite o dia de todos os recibos: ")
            dias.append(dia)
            meses.append(mes)
            anos.append(ano)

            print(f"Dia {dia} do mes {mes}/{ano} salvo!\n")

            if mes == 12:
                mes = 1
                ano += 1
            else:
                mes += 1
            
        print("Datas coletadas com sucesso!\n")
        return dias, meses, anos
        
def padronizar_numero_recibo(n_recibo):
    if n_recibo > 99:
        return f"{n_recibo}"
    elif 9 < n_recibo < 99:
        return f"0{n_recibo}"
    else:
        return f"00{n_recibo}"

def sub_menu_cadastrar_varios():
    os.system('cls')
    print("Submenu: Cadastrar Vários Recibos")
    qtd_recibos = int(input("Digite a quantidade de recibos que deseja cadastrar: "))

    if qtd_recibos <= 0:
        print("Quantidade inválida. Por favor, insira um número maior que zero.")
        return sub_menu_cadastrar_varios()

    os.system('cls')
    print(f"Você escolheu cadastrar {qtd_recibos} recibos\n")

    print("Iniciando a coleta de informações...\n")

    print("Deseja repetir a coleta de informações para cada recibo? (s/n): ")
    repetir = input().strip().lower()
    if repetir == 's':
        print("Repetindo a coleta de informações para cada recibo...\n")
    else:
        print("Coletando informações apenas uma vez para todos os recibos...\n")

    coleta_informacao(qtd_recibos, repetir)

def menu_principal():
    os.system('cls')
    print("Gerador de Recibos V1.0.2.2")
    print("Selecione uma das opções abaixo: \n")
    print("[1] CADASTRAR VARIOS")
    print("[2] CADASTRAR UM")
    print("[3] SAIR")
    opcao_selecionada = int(input("Escolha uma das opções: "))
    
    if opcao_selecionada == 1:
        sub_menu_cadastrar_varios()
    elif opcao_selecionada == 2:
        coleta_informacao(1, 'n')
    else:
        print("Saindo do programa...")
           
def main():

    while True:
        menu_principal()
        continuar = input("Deseja continuar? (s/n): ").strip().lower()

        if continuar != 's':
            print("Obrigado por usar o Gerador de Recibos!")
            break
        else:
            os.system('cls')
            print("Reiniciando o Gerador de Recibos...\n")
            continue

if (__name__ == '__main__'):

    main()