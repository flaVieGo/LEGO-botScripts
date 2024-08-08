# func_linha[0] = ID             func_linha[1] = SET           func_linha[2] = TEMA
# func_linha[3] = NOME           func_linha[4] = ESPECIAL      func_linha[5] = TOTAL_PECAS
# func_linha[6] = CONDICAO       func_linha[7] = EMBALAGEM     func_linha[8] = INSTRUCOES
# func_linha[9] = CONDICAO_PECAS func_linha[10] = PECAS_ESPEC  func_linha[11] = MINIFIGURES
# func_linha[12] = MF_ESPEC      func_linha[13] = ANO          func_linha[14] = CORRENCIA
# func_linha[15] = VALOR         func_linha[16] = QTDE         func_linha[17] = OBS
# func_linha[18] = LINK


def lojinha(func_linha, arquivo):
   caminho = (fr'C:\Users\Flavio\_Flavio\LEGO\anuncios\{arquivo}.txt')            #casa
   # caminho = (fr'C:\Users\r323741\Desktop\projetin\anuncios\{arquivo}.txt')     #trabalho
   
   with open(caminho, 'w') as texto:
      texto.write(f'\n\n\nDescrição para ML\n\n')

      texto.write(f'{int(func_linha[1])} LEGO®: {func_linha[2]} - {func_linha[3]}')
      if func_linha[4] == 'GWP':
         texto.write(f' [GWP]')
      if func_linha[4] == 'Polybag':
         texto.write(f' [Polybag]')

      texto.write(f'\n\nSet: {int(func_linha[1])}\n')
      texto.write(f'Tema: {func_linha[2]}\n')
      texto.write(f'Peças: {int(func_linha[5])}\n\n')

      texto.write(f'Condição: {func_linha[6]}\n')

      if func_linha[6] == 'Usado':
         texto.write(f'Embalagem: {func_linha[7]} [obs]\n')
         texto.write(f'Instruções: {func_linha[8]} [obs]\n')
         if func_linha[9] == 'Completo':
            texto.write(f'Peças: {func_linha[10]}\n')
         else:
            texto.write(f'Vide observações abaixo.\n')
      
      if func_linha[11] != 'N/A':
         texto.write(f'\nMinifiguras: {int(func_linha[11])}\n')
         texto.write(f'Mf do SET: {func_linha[12]}\n')

      texto.write(f'\nAno de Lançamento: {int(func_linha[13])}\n')
      texto.write(f'Comercialização: {func_linha[14]}\n\n')

      texto.write(f'Obs.:\n')


def whatsApp(func_linha, arquivo):
   caminho = (fr'C:\Users\Flavio\_Flavio\LEGO\anuncios\{arquivo}.txt')            #casa
   # caminho = (fr'C:\Users\r323741\Desktop\projetin\anuncios\{arquivo}.txt')     #trabalho
   
   with open(caminho, 'a') as texto:
    texto.write(f'Descrição para WhatsApp\n\n')
    texto.write(f'#{int(func_linha[1])}\n\n')

    texto.write(f'Set: {func_linha[3]}\n')
    texto.write(f'Linha: {func_linha[2]}\n')
    texto.write(f'Condição: {func_linha[6]}\n')
    texto.write(f'Peças: {int(func_linha[5])}\n')
    texto.write(f'Ano: {int(func_linha[13])}\n')
    if (func_linha[11]) == 'N/A':
        texto.write(f'Minifiguras: N/A\n')
    else:
        texto.write(f'Minifiguras: {int(func_linha[11])}\n')
    
    if func_linha[6] == 'Usado':
         texto.write(f'\nEmbalagem: {func_linha[7]} [obs]\n')
         texto.write(f'Instruções: {func_linha[8]} [obs]\n')
         if func_linha[9] == 'Completo':
            texto.write(f'Peças: {func_linha[10]}\n')
         else:
            texto.write(f'Vide observações abaixo.\n')
    
    texto.write(f'\nPreço: R${func_linha[15]:.2f}\n')
    texto.write(f'Qtde. Disponível: {int(func_linha[16])}\n\n')

    texto.write(f'Link: {func_linha[17]}\n')