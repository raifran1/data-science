import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.read_csv('resultado.csv')
dados = (pd.read_csv('resultado.csv'))

opcao = int(input("""
      Escolha uma opção Para descobrir a quantidade de pessoas do sexo Masculino
      e Feminino das Redes de Ensino
------------------------------
      [1]  - Ensino Privado
      [2]  - Ensino Publico Municipal
      [3]  - Ensino Publico Estadual
      [4]  - Outros

------------------------------
      [0] - SAIR
------------------------------
\n\n"""))


ensino_PRIVADO = (dados[dados.RedeEnsino == "PRIVADA"])
ensino_publico_mun = (dados[dados.RedeEnsino == "PÚBLICA MUNICIPAL"])
ensino_publico_est = (dados[dados.RedeEnsino == "PÚBLICA ESTADUAL"])
outros = (dados[dados.RedeEnsino == "OUTRO"])

if opcao == 1:
    ensino_privado_masc= (ensino_PRIVADO[ensino_PRIVADO.Sexo == "Masculino"])
    ensino_privado_fem = (ensino_PRIVADO[ensino_PRIVADO.Sexo == "Feminino"])

    ens_pv_masc = ensino_privado_masc.Sexo.count()
    ens_pv_fem = ensino_privado_fem.Sexo.count()

    y_axis = [ens_pv_masc,ens_pv_fem]
    
    x_axis = ['Homens','Mulheres']
    width_n = 0.9
    bar_color = 'red'
    
    plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
    plt.show()

elif opcao == 2:
    ensino_publico_municipal_masc = (ensino_publico_mun[ensino_publico_mun.Sexo == "Masculino"])
    ensino_publico_municipal_fem = (ensino_publico_mun[ensino_publico_mun.Sexo == "Feminino"])

    ens_pb_mun_masc = ensino_publico_municipal_masc.Sexo.count()
    ens_pb_mun_fem = ensino_publico_municipal_fem.Sexo.count()

    y_axis = [ens_pb_mun_masc,ens_pb_mun_fem]
    
    x_axis = ['Homens','Mulheres']
    width_n = 0.9
    bar_color = 'red'
    
    plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
    plt.show()

elif opcao == 3:
    ensino_publico_estadual_masc = (ensino_publico_est[ensino_publico_est.Sexo == "Masculino"])
    ensino_publico_estadual_fem = (ensino_publico_est[ensino_publico_est.Sexo == "Feminino"])

    ens_pb_est_masc = ensino_publico_estadual_masc.Sexo.count()
    ens_pb_est_fem = ensino_publico_estadual_fem.Sexo.count()

    y_axis = [ens_pb_est_masc,ens_pb_est_fem]
    
    x_axis = ['Homens','Mulheres']
    width_n = 0.9
    bar_color = 'red'
    
    plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
    plt.show()

elif opcao == 4:
    outros_masc = (outros[outros.Sexo == "Masculino"])
    outros_fem = (outros[outros.Sexo == "Feminino"])

    outros_m = outros_masc.Sexo.count()
    outros_f = outros_masc.Sexo.count()

    y_axis = [outros_m,outros_f]
    
    x_axis = ['Homens','Mulheres']
    width_n = 0.9
    bar_color = 'red'
    
    plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
    plt.show()









