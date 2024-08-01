import xlwings
import functions as func

print('Descriptions Make, Vers. 2.3\n')

entradas = input('Informe os IDs para criação de anúncios (primeiro e último apenas): ') 
rangeNumeros = [int(numero) for numero in entradas.split()]

ID = list(range(rangeNumeros[0], rangeNumeros[1] + 1))

xl = xlwings.App(visible=False)
# arquivoXL = xl.books.open(r"C:\Users\r323741\Desktop\projetin\LEGO.xlsm")   #trabalho
arquivoXL = xl.books.open(r"C:\Users\Flavio\_Flavio\LEGO\LEGO.xlsm")          #casa
planilha = arquivoXL.sheets["Anuncios"]

for i in ID:
    for celula in planilha.range(f'B6:B1000'):
        if(celula.value) == i:
            dadosLinha = planilha.range(celula.row, 2).expand('right').value
            break
        else:
            dadosLinha = None

    if dadosLinha:
        nomeArquivo = (f'[{int(dadosLinha[0])}] {int(dadosLinha[1])}')

        func.whatsApp(dadosLinha, nomeArquivo)
        func.lojinha(dadosLinha, nomeArquivo)

        print(f"Informações do anúncio {i} salvas em {nomeArquivo}.txt")
    else:
        print(f"ID {i} não encontrado na planilha.")

input("qualquer tecla para fechar...")


arquivoXL.close()
xl.quit()

# pyinstaller --onefile meu_programa.py