# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.read_csv('C:/Users/Raifran/Downloads/resultado.csv')
dados = (pd.read_csv('C:/Users/Raifran/Downloads/resultado.csv'))


geral = dados
Ensino_PRIVADO = (geral[geral.RedeEnsino == "PRIVADA"])
Ensino_PE = (geral[geral.RedeEnsino == "PÚBLICA ESTADUAL"])
Ensino_PF = (geral[geral.RedeEnsino == "PÚBLICA FEDERAL"])
Ensino_PM = (geral[geral.RedeEnsino == "PÚBLICA MUNICIPAL"])
Outro = (geral[geral.RedeEnsino == "OUTRO"])

TOTAL = dados.RedeEnsino.count()
EP = Ensino_PRIVADO.RedeEnsino.count()
EPE = Ensino_PE.RedeEnsino.count()
EPF = Ensino_PF.RedeEnsino.count()
EPM = Ensino_PM.RedeEnsino.count()
O = Outro.RedeEnsino.count()

y_axis = [EP,EPE,EPF,EPM,O]
x_axis = ['Privado','Estadual','Federal','Municipal','Outros']
width_n = 0.8
bar_color = 'black'

plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
plt.show()
    

print(f"""
        Ensino Privado - {EP}
        Ensino Público Estadual - {EPE}
        Ensino Público Federal - {EPF}
        Ensino Público Municipal - {EPM}
        Outros - {O}
        --------------------------------
        Total - {TOTAL}
          """)
    
opcao = int(input("""
      Escolha uma opção
------------------------------
      [1]  - TERESINA - CENTRAL
      [2]  - TERESINA - ZONA SUL
      [3]  - CORRENTE
      [4]  - OEIRAS  
      [5]  - VALENÇA
      [6]  - FLORIANO
      [7]  - PICOS
      [8]  - SÃO JOÃO DO PIAUÍ
      [9]  - PIRIPIRI
      [10] - PARNAÍBA
      [11] - COCAL
      [12] - ANGICAL
      [13] - PEDRO II
      [14] - CAMPO MAIOR
      [15] - PAULISTANA
      [16] - URUÇUÍ
------------------------------
\n\n"""))


if opcao == 1:
    Teresina_Central = (dados[dados.Unidade == "TERESINA - CENTRAL"])
    Ensino_PRIVADO = (Teresina_Central[Teresina_Central.RedeEnsino == "PRIVADA"])
    Ensino_PE = (Teresina_Central[Teresina_Central.RedeEnsino == "PÚBLICA ESTADUAL"])
    Ensino_PF = (Teresina_Central[Teresina_Central.RedeEnsino == "PÚBLICA FEDERAL"])
    Ensino_PM = (Teresina_Central[Teresina_Central.RedeEnsino == "PÚBLICA MUNICIPAL"])
    Outro = (Teresina_Central[Teresina_Central.RedeEnsino == "OUTRO"])
    
    TOTAL = Teresina_Central.RedeEnsino.count()
    EP = Ensino_PRIVADO.RedeEnsino.count()
    EPE = Ensino_PE.RedeEnsino.count()
    EPF = Ensino_PF.RedeEnsino.count()
    EPM = Ensino_PM.RedeEnsino.count()
    O = Outro.RedeEnsino.count()
    
    y_axis = [EP,EPE,EPF,EPM,O]
    x_axis = ['Privado','Estadual','Federal','Municipal','Outros']
    width_n = 0.8
    bar_color = 'red'
    
    plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
    plt.show()
    
    print(f"""
        Ensino Privado - {EP}
        Ensino Público Estadual - {EPE}
        Ensino Público Federal - {EPF}
        Ensino Público Municipal - {EPM}
        Outros - {O}
        --------------------------------
        Total - {TOTAL}
          """)
    
elif opcao == 2:
    Teresina_Sul = (dados[dados.Unidade == "TERESINA - ZONA SUL"])
    Ensino_PRIVADO = (Teresina_Sul[Teresina_Sul.RedeEnsino == "PRIVADA"])
    Ensino_PE = (Teresina_Sul[Teresina_Sul.RedeEnsino == "PÚBLICA ESTADUAL"])
    Ensino_PF = (Teresina_Sul[Teresina_Sul.RedeEnsino == "PÚBLICA FEDERAL"])
    Ensino_PM = (Teresina_Sul[Teresina_Sul.RedeEnsino == "PÚBLICA MUNICIPAL"])
    Outro = (Teresina_Sul[Teresina_Sul.RedeEnsino == "OUTRO"])
    
    
    TOTAL = Teresina_Sul.RedeEnsino.count()
    EP = Ensino_PRIVADO.RedeEnsino.count()
    EPE = Ensino_PE.RedeEnsino.count()
    EPF = Ensino_PF.RedeEnsino.count()
    EPM = Ensino_PM.RedeEnsino.count()
    O = Outro.RedeEnsino.count()
    
    y_axis = [EP,EPE,EPF,EPM,O]
    x_axis = ['Privado','Estadual','Federal','Municipal','Outros']
    width_n = 0.8
    bar_color = 'red'
    
    plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
    plt.show()

    print(f"""
        Ensino Privado - {EP}
        Ensino Público Estadual - {EPE}
        Ensino Público Federal - {EPF}
        Ensino Público Municipal - {EPM}
        Outros - {O}
          --------------------------------
        Total - {TOTAL}
          """)
    
elif opcao == 3:
    CORRENTE = (dados[dados.Unidade == "CORRENTE"])
    Ensino_PRIVADO = (CORRENTE[CORRENTE.RedeEnsino == "PRIVADA"])
    Ensino_PE = (CORRENTE[CORRENTE.RedeEnsino == "PÚBLICA ESTADUAL"])
    Ensino_PF = (CORRENTE[CORRENTE.RedeEnsino == "PÚBLICA FEDERAL"])
    Ensino_PM = (CORRENTE[CORRENTE.RedeEnsino == "PÚBLICA MUNICIPAL"])
    Outro = (CORRENTE[CORRENTE.RedeEnsino == "OUTRO"])
    
    
    TOTAL = CORRENTE.RedeEnsino.count()
    EP = Ensino_PRIVADO.RedeEnsino.count()
    EPE = Ensino_PE.RedeEnsino.count()
    EPF = Ensino_PF.RedeEnsino.count()
    EPM = Ensino_PM.RedeEnsino.count()
    O = Outro.RedeEnsino.count()
    
    y_axis = [EP,EPE,EPF,EPM,O]
    x_axis = ['Privado','Estadual','Federal','Municipal','Outros']
    width_n = 0.8
    bar_color = 'red'
    
    plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
    plt.show()

    print(f"""
        Ensino Privado - {EP}
        Ensino Público Estadual - {EPE}
        Ensino Público Federal - {EPF}
        Ensino Público Municipal - {EPM}
        Outros - {O}
        --------------------------------
        Total - {TOTAL}
          """)

elif opcao == 4:
    OEIRAS = (dados[dados.Unidade == "OEIRAS"])
    Ensino_PRIVADO = (OEIRAS[OEIRAS.RedeEnsino == "PRIVADA"])
    Ensino_PE = (OEIRAS[OEIRAS.RedeEnsino == "PÚBLICA ESTADUAL"])
    Ensino_PF = (OEIRAS[OEIRAS.RedeEnsino == "PÚBLICA FEDERAL"])
    Ensino_PM = (OEIRAS[OEIRAS.RedeEnsino == "PÚBLICA MUNICIPAL"])
    Outro = (OEIRAS[OEIRAS.RedeEnsino == "OUTRO"])
    
    
    TOTAL = OEIRAS.RedeEnsino.count()
    EP = Ensino_PRIVADO.RedeEnsino.count()
    EPE = Ensino_PE.RedeEnsino.count()
    EPF = Ensino_PF.RedeEnsino.count()
    EPM = Ensino_PM.RedeEnsino.count()
    O = Outro.RedeEnsino.count()
    
    y_axis = [EP,EPE,EPF,EPM,O]
    x_axis = ['Privado','Estadual','Federal','Municipal','Outros']
    width_n = 0.8
    bar_color = 'red'
    
    plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
    plt.show()

    print(f"""
        Ensino Privado - {EP}
        Ensino Público Estadual - {EPE}
        Ensino Público Federal - {EPF}
        Ensino Público Municipal - {EPM}
        Outros - {O}
        --------------------------------
        Total - {TOTAL}
          """)

elif opcao == 5:
    VALENCA = (dados[dados.Unidade == "VALENÇA"])
    Ensino_PRIVADO = (VALENCA[VALENCA.RedeEnsino == "PRIVADA"])
    Ensino_PE = (VALENCA[VALENCA.RedeEnsino == "PÚBLICA ESTADUAL"])
    Ensino_PF = (VALENCA[VALENCA.RedeEnsino == "PÚBLICA FEDERAL"])
    Ensino_PM = (VALENCA[VALENCA.RedeEnsino == "PÚBLICA MUNICIPAL"])
    Outro = (VALENCA[VALENCA.RedeEnsino == "OUTRO"])
    
    
    TOTAL = VALENCA.RedeEnsino.count()
    EP = Ensino_PRIVADO.RedeEnsino.count()
    EPE = Ensino_PE.RedeEnsino.count()
    EPF = Ensino_PF.RedeEnsino.count()
    EPM = Ensino_PM.RedeEnsino.count()
    O = Outro.RedeEnsino.count()
    
    y_axis = [EP,EPE,EPF,EPM,O]
    x_axis = ['Privado','Estadual','Federal','Municipal','Outros']
    width_n = 0.8
    bar_color = 'red'
    
    plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
    plt.show()

    print(f"""
        Ensino Privado - {EP}
        Ensino Público Estadual - {EPE}
        Ensino Público Federal - {EPF}
        Ensino Público Municipal - {EPM}
        Outros - {O}
        --------------------------------
        Total - {TOTAL}
          """)

elif opcao == 6:
    C_FLORIANO = (dados[dados.Unidade == "FLORIANO"])
    Ensino_PRIVADO = (C_FLORIANO[C_FLORIANO.RedeEnsino == "PRIVADA"])
    Ensino_PE = (C_FLORIANO[C_FLORIANO.RedeEnsino == "PÚBLICA ESTADUAL"])
    Ensino_PF = (C_FLORIANO[C_FLORIANO.RedeEnsino == "PÚBLICA FEDERAL"])
    Ensino_PM = (C_FLORIANO[C_FLORIANO.RedeEnsino == "PÚBLICA MUNICIPAL"])
    Outro = (C_FLORIANO[C_FLORIANO.RedeEnsino == "OUTRO"])
    
    
    TOTAL = C_FLORIANO.RedeEnsino.count()
    EP = Ensino_PRIVADO.RedeEnsino.count()
    EPE = Ensino_PE.RedeEnsino.count()
    EPF = Ensino_PF.RedeEnsino.count()
    EPM = Ensino_PM.RedeEnsino.count()
    O = Outro.RedeEnsino.count()
    
    y_axis = [EP,EPE,EPF,EPM,O]
    x_axis = ['Privado','Estadual','Federal','Municipal','Outros']
    width_n = 0.8
    bar_color = 'red'
    
    plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
    plt.show()

    print(f"""
        Ensino Privado - {EP}
        Ensino Público Estadual - {EPE}
        Ensino Público Federal - {EPF}
        Ensino Público Municipal - {EPM}
        Outros - {O}
        --------------------------------
        Total - {TOTAL}
          """)

elif opcao == 7:
    PICOS = (dados[dados.Unidade == "PICOS"])
    Ensino_PRIVADO = (PICOS[PICOS.RedeEnsino == "PRIVADA"])
    Ensino_PE = (PICOS[PICOS.RedeEnsino == "PÚBLICA ESTADUAL"])
    Ensino_PF = (PICOS[PICOS.RedeEnsino == "PÚBLICA FEDERAL"])
    Ensino_PM = (PICOS[PICOS.RedeEnsino == "PÚBLICA MUNICIPAL"])
    Outro = (PICOS[PICOS.RedeEnsino == "OUTRO"])
    
    
    TOTAL = PICOS.RedeEnsino.count()
    EP = Ensino_PRIVADO.RedeEnsino.count()
    EPE = Ensino_PE.RedeEnsino.count()
    EPF = Ensino_PF.RedeEnsino.count()
    EPM = Ensino_PM.RedeEnsino.count()
    O = Outro.RedeEnsino.count()
    
    y_axis = [EP,EPE,EPF,EPM,O]
    x_axis = ['Privado','Estadual','Federal','Municipal','Outros']
    width_n = 0.8
    bar_color = 'red'
    
    plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
    plt.show()

    print(f"""
        Ensino Privado - {EP}
        Ensino Público Estadual - {EPE}
        Ensino Público Federal - {EPF}
        Ensino Público Municipal - {EPM}
        Outros - {O}
        --------------------------------
        Total - {TOTAL}
          """)

elif opcao == 8:
    SJ_PIAUI = (dados[dados.Unidade == "SÃO JOÃO DO PIAUÍ"])
    Ensino_PRIVADO = (SJ_PIAUI[SJ_PIAUI.RedeEnsino == "PRIVADA"])
    Ensino_PE = (SJ_PIAUI[SJ_PIAUI.RedeEnsino == "PÚBLICA ESTADUAL"])
    Ensino_PF = (SJ_PIAUI[SJ_PIAUI.RedeEnsino == "PÚBLICA FEDERAL"])
    Ensino_PM = (SJ_PIAUI[SJ_PIAUI.RedeEnsino == "PÚBLICA MUNICIPAL"])
    Outro = (SJ_PIAUI[SJ_PIAUI.RedeEnsino == "OUTRO"])
    
    
    TOTAL = SJ_PIAUI.RedeEnsino.count()
    EP = Ensino_PRIVADO.RedeEnsino.count()
    EPE = Ensino_PE.RedeEnsino.count()
    EPF = Ensino_PF.RedeEnsino.count()
    EPM = Ensino_PM.RedeEnsino.count()
    O = Outro.RedeEnsino.count()
    
    y_axis = [EP,EPE,EPF,EPM,O]
    x_axis = ['Privado','Estadual','Federal','Municipal','Outros']
    width_n = 0.8
    bar_color = 'red'
    
    plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
    plt.show()

    print(f"""
        Ensino Privado - {EP}
        Ensino Público Estadual - {EPE}
        Ensino Público Federal - {EPF}
        Ensino Público Municipal - {EPM}
        Outros - {O}
        --------------------------------
        Total - {TOTAL}
            """)
    
elif opcao == 9:
    PIRIPIRI = (dados[dados.Unidade == "PIRIPIRI"])
    Ensino_PRIVADO = (PIRIPIRI[PIRIPIRI.RedeEnsino == "PRIVADA"])
    Ensino_PE = (PIRIPIRI[PIRIPIRI.RedeEnsino == "PÚBLICA ESTADUAL"])
    Ensino_PF = (PIRIPIRI[PIRIPIRI.RedeEnsino == "PÚBLICA FEDERAL"])
    Ensino_PM = (PIRIPIRI[PIRIPIRI.RedeEnsino == "PÚBLICA MUNICIPAL"])
    Outro = (PIRIPIRI[PIRIPIRI.RedeEnsino == "OUTRO"])
    
    
    TOTAL = PIRIPIRI.RedeEnsino.count()
    EP = Ensino_PRIVADO.RedeEnsino.count()
    EPE = Ensino_PE.RedeEnsino.count()
    EPF = Ensino_PF.RedeEnsino.count()
    EPM = Ensino_PM.RedeEnsino.count()
    O = Outro.RedeEnsino.count()
    
    y_axis = [EP,EPE,EPF,EPM,O]
    x_axis = ['Privado','Estadual','Federal','Municipal','Outros']
    width_n = 0.8
    bar_color = 'red'
    
    plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
    plt.show()
    
    print(f"""
        Ensino Privado - {EP}
        Ensino Público Estadual - {EPE}
        Ensino Público Federal - {EPF}
        Ensino Público Municipal - {EPM}
        Outros - {O}
        --------------------------------
        Total - {TOTAL}
          """)

elif opcao == 10:
    PARNAIBA = (dados[dados.Unidade == "PARNAÍBA"])
    Ensino_PRIVADO = (PARNAIBA[PARNAIBA.RedeEnsino == "PRIVADA"])
    Ensino_PE = (PARNAIBA[PARNAIBA.RedeEnsino == "PÚBLICA ESTADUAL"])
    Ensino_PF = (PARNAIBA[PARNAIBA.RedeEnsino == "PÚBLICA FEDERAL"])
    Ensino_PM = (PARNAIBA[PARNAIBA.RedeEnsino == "PÚBLICA MUNICIPAL"])
    Outro = (PARNAIBA[PARNAIBA.RedeEnsino == "OUTRO"])
    
    
    TOTAL = PARNAIBA.RedeEnsino.count()
    EP = Ensino_PRIVADO.RedeEnsino.count()
    EPE = Ensino_PE.RedeEnsino.count()
    EPF = Ensino_PF.RedeEnsino.count()
    EPM = Ensino_PM.RedeEnsino.count()
    O = Outro.RedeEnsino.count()
    
    y_axis = [EP,EPE,EPF,EPM,O]
    x_axis = ['Privado','Estadual','Federal','Municipal','Outros']
    width_n = 0.8
    bar_color = 'red'
    
    plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
    plt.show()

    print(f"""
        Ensino Privado - {EP}
        Ensino Público Estadual - {EPE}
        Ensino Público Federal - {EPF}
        Ensino Público Municipal - {EPM}
        Outros - {O}
        --------------------------------
        Total - {TOTAL}
          """)

elif opcao == 11:
    COCAL = (dados[dados.Unidade == "COCAL"])
    Ensino_PRIVADO = (COCAL[COCAL.RedeEnsino == "PRIVADA"])
    Ensino_PE = (COCAL[COCAL.RedeEnsino == "PÚBLICA ESTADUAL"])
    Ensino_PF = (COCAL[COCAL.RedeEnsino == "PÚBLICA FEDERAL"])
    Ensino_PM = (COCAL[COCAL.RedeEnsino == "PÚBLICA MUNICIPAL"])
    Outro = (COCAL[COCAL.RedeEnsino == "OUTRO"])
    
    
    TOTAL = COCAL.RedeEnsino.count()
    EP = Ensino_PRIVADO.RedeEnsino.count()
    EPE = Ensino_PE.RedeEnsino.count()
    EPF = Ensino_PF.RedeEnsino.count()
    EPM = Ensino_PM.RedeEnsino.count()
    O = Outro.RedeEnsino.count()
    
    y_axis = [EP,EPE,EPF,EPM,O]
    x_axis = ['Privado','Estadual','Federal','Municipal','Outros']
    width_n = 0.8
    bar_color = 'red'
    
    plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
    plt.show()

    print(f"""
        Ensino Privado - {EP}
        Ensino Público Estadual - {EPE}
        Ensino Público Federal - {EPF}
        Ensino Público Municipal - {EPM}
        Outros - {O}
        --------------------------------
        Total - {TOTAL}
          """)

elif opcao == 12:
    ANGICAL = (dados[dados.Unidade == "ANGICAL"])
    Ensino_PRIVADO = (ANGICAL[ANGICAL.RedeEnsino == "PRIVADA"])
    Ensino_PE = (ANGICAL[ANGICAL.RedeEnsino == "PÚBLICA ESTADUAL"])
    Ensino_PF = (ANGICAL[ANGICAL.RedeEnsino == "PÚBLICA FEDERAL"])
    Ensino_PM = (ANGICAL[ANGICAL.RedeEnsino == "PÚBLICA MUNICIPAL"])
    Outro = (ANGICAL[ANGICAL.RedeEnsino == "OUTRO"])
    
    
    TOTAL = ANGICAL.RedeEnsino.count()
    EP = Ensino_PRIVADO.RedeEnsino.count()
    EPE = Ensino_PE.RedeEnsino.count()
    EPF = Ensino_PF.RedeEnsino.count()
    EPM = Ensino_PM.RedeEnsino.count()
    O = Outro.RedeEnsino.count()
    
    y_axis = [EP,EPE,EPF,EPM,O]
    x_axis = ['Privado','Estadual','Federal','Municipal','Outros']
    width_n = 0.8
    bar_color = 'red'
    
    plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
    plt.show()

    print(f"""
        Ensino Privado - {EP}
        Ensino Público Estadual - {EPE}
        Ensino Público Federal - {EPF}
        Ensino Público Municipal - {EPM}
        Outros - {O}
        --------------------------------
        Total - {TOTAL}
          """)

elif opcao == 13:
    PEDRO_II = (dados[dados.Unidade == "PEDRO II"])
    Ensino_PRIVADO = (PEDRO_II[PEDRO_II.RedeEnsino == "PRIVADA"])
    Ensino_PE = (PEDRO_II[PEDRO_II.RedeEnsino == "PÚBLICA ESTADUAL"])
    Ensino_PF = (PEDRO_II[PEDRO_II.RedeEnsino == "PÚBLICA FEDERAL"])
    Ensino_PM = (PEDRO_II[PEDRO_II.RedeEnsino == "PÚBLICA MUNICIPAL"])
    Outro = (PEDRO_II[PEDRO_II.RedeEnsino == "OUTRO"])
    
    
    TOTAL = PEDRO_II.RedeEnsino.count()
    EP = Ensino_PRIVADO.RedeEnsino.count()
    EPE = Ensino_PE.RedeEnsino.count()
    EPF = Ensino_PF.RedeEnsino.count()
    EPM = Ensino_PM.RedeEnsino.count()
    O = Outro.RedeEnsino.count()
    
    y_axis = [EP,EPE,EPF,EPM,O]
    x_axis = ['Privado','Estadual','Federal','Municipal','Outros']
    width_n = 0.8
    bar_color = 'red'
    
    plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
    plt.show()

    print(f"""
        Ensino Privado - {EP}
        Ensino Público Estadual - {EPE}
        Ensino Público Federal - {EPF}
        Ensino Público Municipal - {EPM}
        Outros - {O}
        --------------------------------
        Total - {TOTAL}
          """)

elif opcao == 14:
    CAMPO_MAIOR = (dados[dados.Unidade == "CAMPO MAIOR"])
    Ensino_PRIVADO = (CAMPO_MAIOR[CAMPO_MAIOR.RedeEnsino == "PRIVADA"])
    Ensino_PE = (CAMPO_MAIOR[CAMPO_MAIOR.RedeEnsino == "PÚBLICA ESTADUAL"])
    Ensino_PF = (CAMPO_MAIOR[CAMPO_MAIOR.RedeEnsino == "PÚBLICA FEDERAL"])
    Ensino_PM = (CAMPO_MAIOR[CAMPO_MAIOR.RedeEnsino == "PÚBLICA MUNICIPAL"])
    Outro = (CAMPO_MAIOR[CAMPO_MAIOR.RedeEnsino == "OUTRO"])
    
    
    TOTAL = CAMPO_MAIOR.RedeEnsino.count()
    EP = Ensino_PRIVADO.RedeEnsino.count()
    EPE = Ensino_PE.RedeEnsino.count()
    EPF = Ensino_PF.RedeEnsino.count()
    EPM = Ensino_PM.RedeEnsino.count()
    O = Outro.RedeEnsino.count()
    
    y_axis = [EP,EPE,EPF,EPM,O]
    x_axis = ['Privado','Estadual','Federal','Municipal','Outros']
    width_n = 0.8
    bar_color = 'red'
    
    plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
    plt.show()

    print(f"""
        Ensino Privado - {EP}
        Ensino Público Estadual - {EPE}
        Ensino Público Federal - {EPF}
        Ensino Público Municipal - {EPM}
        Outros - {O}
        --------------------------------
        Total - {TOTAL}
          """)

elif opcao == 15:
    PAULISTANA = (dados[dados.Unidade == "PAULISTANA"])
    Ensino_PRIVADO = (PAULISTANA[PAULISTANA.RedeEnsino == "PRIVADA"])
    Ensino_PE = (PAULISTANA[PAULISTANA.RedeEnsino == "PÚBLICA ESTADUAL"])
    Ensino_PF = (PAULISTANA[PAULISTANA.RedeEnsino == "PÚBLICA FEDERAL"])
    Ensino_PM = (PAULISTANA[PAULISTANA.RedeEnsino == "PÚBLICA MUNICIPAL"])
    Outro = (PAULISTANA[PAULISTANA.RedeEnsino == "OUTRO"])
    
    
    TOTAL = PAULISTANA.RedeEnsino.count()
    EP = Ensino_PRIVADO.RedeEnsino.count()
    EPE = Ensino_PE.RedeEnsino.count()
    EPF = Ensino_PF.RedeEnsino.count()
    EPM = Ensino_PM.RedeEnsino.count()
    O = Outro.RedeEnsino.count()
    
    y_axis = [EP,EPE,EPF,EPM,O]
    x_axis = ['Privado','Estadual','Federal','Municipal','Outros']
    width_n = 0.8
    bar_color = 'red'
    
    plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
    plt.show()

    print(f"""
        Ensino Privado - {EP}
        Ensino Público Estadual - {EPE}
        Ensino Público Federal - {EPF}
        Ensino Público Municipal - {EPM}
        Outros - {O}
        --------------------------------
        Total - {TOTAL}
          """)
    
elif opcao == 16:
    URUCUI = (dados[dados.Unidade == "URUÇUÍ"])
    Ensino_PRIVADO = (URUCUI[URUCUI.RedeEnsino == "PRIVADA"])
    Ensino_PE = (URUCUI[URUCUI.RedeEnsino == "PÚBLICA ESTADUAL"])
    Ensino_PF = (URUCUI[URUCUI.RedeEnsino == "PÚBLICA FEDERAL"])
    Ensino_PM = (URUCUI[URUCUI.RedeEnsino == "PÚBLICA MUNICIPAL"])
    Outro = (URUCUI[URUCUI.RedeEnsino == "OUTRO"])
    
    
    TOTAL = URUCUI.RedeEnsino.count()
    EP = Ensino_PRIVADO.RedeEnsino.count()
    EPE = Ensino_PE.RedeEnsino.count()
    EPF = Ensino_PF.RedeEnsino.count()
    EPM = Ensino_PM.RedeEnsino.count()
    O = Outro.RedeEnsino.count()
    
    y_axis = [EP,EPE,EPF,EPM,O]
    x_axis = ['Privado','Estadual','Federal','Municipal','Outros']
    width_n = 0.8
    bar_color = 'red'
    
    plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
    plt.show()

    print(f"""
        Ensino Privado - {EP}
        Ensino Público Estadual - {EPE}
        Ensino Público Federal - {EPF}
        Ensino Público Municipal - {EPM}
        Outros - {O}
        --------------------------------
        Total - {TOTAL}
          """)