import xlwings
import functions as func

print('Descriptions Make, Vers. 2.1\n\n')

entradas = input('Informe os IDs para criação de anúncios: ')                           #ID recebe os números dos anúncios a serem criados
ID = [int(numero) for numero in entradas.split()]

xl = xlwings.App(visible=False)
arquivoXL = xl.books.open(r"C:\Users\r323741\Desktop\projetin\LEGO.xlsm")
planilha = arquivoXL.sheets["Anuncios"]

for i in ID:
    for celula in planilha.range(f'B6:B1000'):
        if(celula.value) == i:
            dadosLinha = planilha.range(celula.row, 2).expand('right').value
            break
        else:
            dadosLinha = None

    if dadosLinha:
        nomeArquivo = (f'{int(dadosLinha[1])}_{int(dadosLinha[0])}')

        func.whatsApp(dadosLinha, nomeArquivo)
        func.lojinha(dadosLinha, nomeArquivo)

        print(f"Informações do anúncio {i} salvas em {nomeArquivo}.txt")
    else:
        print(f"ID {i} não encontrado na planilha.")

input("qualquer tecla para fechar...")


arquivoXL.close()
xl.quit()

# pyinstaller --onefile meu_programa.py