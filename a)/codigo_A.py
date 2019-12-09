import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random


pd.read_csv('C:/Users/Raifran/Desktop/Eduilson-Data Science/resultado-2015_2.csv')
dados = (pd.read_csv('C:/Users/Raifran/Desktop/Eduilson-Data Science/resultado-2015_2.csv'))


def grafico(x,y):
    colors = ['Navy','Purple','Red','Magenta','Lime','Gray']
    
    while True:
        cor_1 = random.choice(colors)
        #print(colors.index(cor_1))
        cor_2 = random.choice(colors)
        #print(colors.index(cor_2))
        if colors.index(cor_1) == colors.index(cor_2):
            pass
        else:
            break

    cor_1 = cor_1
    cor_2 = cor_2

    # coordenadas primeira barra
    y_axis_masc = [x]
    x_axis_masc = ['Homens']

    # coordenadas segunda barra
    y_axis_fem = [y]
    x_axis_fem = ['Mulheres']
                

    # configurações da barra 
    width_n = 0.7
    bar_color_h = cor_1
    bar_color_m = cor_2
    
    # configurações da legenda
    red_patch_h = mpatches.Patch(color=cor_1, label=f'Homens')
    red_patch_m = mpatches.Patch(color=cor_2, label=f'Mulheres')
    plt.legend(handles=[red_patch_h, red_patch_m])
    
    # construção da barra
    plt.bar(x_axis_masc, y_axis_masc, width=width_n, color=bar_color_h, label='Homens') # gráfico masculino
    plt.bar(x_axis_fem, y_axis_fem, width=width_n, color=bar_color_m, label='Mulheres')# gráfico feminino
    
    # percentual com os valores em cada barra
    plt.annotate(f'{x:.2f}%',xy=(0,(x + 0.5)), ha='center', color='black', label='Homens') # percentual masculino         
    plt.annotate(f'{y:.2f}%',xy=(1,(y + 0.5)), ha='center', color='black', label='Mulheres')   # percentual feminino         

    # outras configurações do gráfico
    plt.ylabel('(Percentual dos Gêneros - %)') # rotulo do eixo y 
    plt.title("Gráfico de Gênero por Curso") # titulo
    plt.ylim(0,100) # intervalo fixo do eixo y
    plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) # intervalos do eixo y

    # exibição do gráfico
    plt.show()

def grafico2(x,y):
    colors = ['Navy','Purple','Red','Magenta','Lime','Gray']
    
    while True:
        cor_1 = random.choice(colors)
        #print(colors.index(cor_1))
        cor_2 = random.choice(colors)
        #print(colors.index(cor_2))
        if colors.index(cor_1) == colors.index(cor_2):
            pass
        else:
            break

    cor_1 = cor_1
    cor_2 = cor_2

    # coordenadas primeira barra
    y_axis_masc = [x]
    x_axis_masc = ['Homens']

    # coordenadas segunda barra
    y_axis_fem = [y]
    x_axis_fem = ['Mulheres']
                

    # configurações da barra 
    width_n = 0.7
    bar_color_h = cor_1
    bar_color_m = cor_2
    
    # configurações da legenda
    red_patch_h = mpatches.Patch(color=cor_1, label=f'Homens')
    red_patch_m = mpatches.Patch(color=cor_2, label=f'Mulheres')
    plt.legend(handles=[red_patch_h, red_patch_m])
    
    # construção da barra
    plt.bar(x_axis_masc, y_axis_masc, width=width_n, color=bar_color_h, label='Homens') # gráfico masculino
    plt.bar(x_axis_fem, y_axis_fem, width=width_n, color=bar_color_m, label='Mulheres')# gráfico feminino
    
    # percentual com os valores em cada barra
    plt.annotate(f'{x:.2f}%',xy=(0,(x + 0.5)), ha='center', color='black', label='Homens') # percentual masculino         
    plt.annotate(f'{y:.2f}%',xy=(1,(y + 0.5)), ha='center', color='black', label='Mulheres')   # percentual feminino         

    plt.ylabel('(Percentual dos Gêneros - %)') # rotulo do eixo y 
    plt.title("Gráfico de Gênero por Campus") # titulo
    plt.ylim(0,100) # intervalo fixo do eixo y
    plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) # intervalos do eixo y

    # exibição do gráfico
    plt.show()

def analise_curso():
    while True:
        try:
            escolha_curso = int(input("""
            ---------------------------------------------
            Escolha um curso:
            ---------------------------------------------
            [1]  - Administração / Noite
            [2]  - Administração / Tarde
            [3]  - Informática / Tarde
            [4]  - Informática / Noite 
            [5]  - Seguranca do Trabalho / Noite
            [6]  - Análises Clinicas / Tarde
            [7]  - Edificações / Noite
            [8]  - Eletrotécnica / Noite
            [9]  - Mecânica / Noite
            [10] - Agricultura / Tarde
            [11] - Contabilidade / Tarde
            [12] - Contabilidade / Noite
            [13] - Refrigeração e Climatização / Noite
            [14] - Eletrônica / Noite
            [15] - Vestuário / Noite
            [16] - Estradas / Tarde
            [17] - Agricultura / Manhã
            [18] - Mineração / Tarde
            [19] - Panificação / Tarde
            [20] - Alimentos / Tarde
            [21] - Informática para Internet / Noite
            [22] - Agroindustria / Manhã
            [23] - Instrumento Musical (Violão) / tarde
            [24] - Fruticultura / Tarde
            [25] - Instrumento Musical (Trompete) / tarde
            [26] - Restaurante e Bar / Tarde
            [27] - Instrumento Musical (Teclado Eletrônico) / tarde
            [28] - Instrumento Musical (Trombone) / tarde
            ---------------------------------------------
            [100]  - Voltar para o Menu Principal
            [0]  - Sair do Programa
            ---------------------------------------------
        Opção: """))


            if escolha_curso == 1:
                administracao_noite = dados[dados.Coluna1 == "ADMINISTRAÇÃO / NOITE"] 
                sexo_masc_adm_noite = administracao_noite[administracao_noite.Sexo == "Masculino"]
                sexo_fem_adm_noite = administracao_noite[administracao_noite.Sexo == "Feminino"]

                # nova parte com calculo de percentual
                adm_masc_noite= ((sexo_masc_adm_noite.Sexo.count() *100) / administracao_noite.Coluna1.count()) # percentual                 
                adm_fem_noite = ((sexo_fem_adm_noite.Sexo.count() * 100) / administracao_noite.Coluna1.count()) # percentual
                
                # novas variaveis para armazenar o numero relativo
                adm_masc_noite_num = (sexo_masc_adm_noite.Sexo.count()) # numero relativo           
                adm_fem_noite_num = (sexo_fem_adm_noite.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {adm_masc_noite:.2f}%  feminino - {adm_fem_noite:.2f}%
                masculino - {adm_masc_noite_num}  feminino - {adm_fem_noite_num}''')

                grafico(adm_masc_noite,adm_fem_noite)
                iniciar_menu2()
                break

            elif escolha_curso == 2:
                administracao_tarde = dados[dados.Coluna1 == "ADMINISTRAÇÃO / TARDE"] 
                sexo_masc_adm_tarde = administracao_tarde[administracao_tarde.Sexo == "Masculino"]
                sexo_fem_adm_tarde = administracao_tarde[administracao_tarde.Sexo == "Feminino"]
                
                # nova parte com calculo de percentual
                adm_masc_tarde = ((sexo_masc_adm_tarde.Sexo.count() *100) / administracao_tarde.Coluna1.count()) # percentual                 
                adm_fem_tarde  = ((sexo_fem_adm_tarde.Sexo.count() * 100) / administracao_tarde.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                adm_masc_tarde_num = (sexo_masc_adm_tarde.Sexo.count()) # numero relativo           
                adm_fem_tarde_num = (sexo_fem_adm_tarde.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {adm_masc_tarde:.2f}%  feminino - {adm_fem_tarde:.2f}%
                masculino - {adm_masc_tarde_num}  feminino - {adm_fem_tarde_num}''')

                grafico(adm_masc_tarde,adm_fem_tarde)
                iniciar_menu2()
                break


            elif escolha_curso == 3:
                informatica_tarde = dados[dados.Coluna1 == "INFORMÁTICA / TARDE"]
                sexo_masc_infor_tarde = informatica_tarde[informatica_tarde.Sexo == "Masculino"]
                sexo_fem_infor_tarde = informatica_tarde[informatica_tarde.Sexo == "Feminino"]
                    
                # nova parte com calculo de percentual
                info_masc_tarde = ((sexo_masc_infor_tarde.Sexo.count() *100) / informatica_tarde.Coluna1.count()) # percentual                 
                info_fem_tarde  = ((sexo_fem_infor_tarde.Sexo.count() * 100) / informatica_tarde.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                info_masc_tarde_num = (sexo_masc_infor_tarde.Sexo.count()) # numero relativo           
                info_fem_tarde_num = (sexo_fem_infor_tarde.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {info_masc_tarde:.2f}%  feminino - {info_fem_tarde:.2f}%
                masculino - {info_masc_tarde_num}  feminino - {info_fem_tarde_num}''')

                grafico(info_masc_tarde,info_fem_tarde)
                iniciar_menu2()
                break

            elif escolha_curso == 4:
                informatica_noite = dados[dados.Coluna1 == "INFORMÁTICA / NOITE"]
                sexo_masc_infor_noite = informatica_noite[informatica_noite.Sexo == "Masculino"]
                sexo_fem_infor_noite = informatica_noite[informatica_noite.Sexo == "Feminino"]
                
                # nova parte com calculo de percentual
                info_masc_noite = ((sexo_masc_infor_noite.Sexo.count() *100) / informatica_noite.Coluna1.count()) # percentual                 
                info_fem_noite  = ((sexo_fem_infor_noite.Sexo.count() * 100) / informatica_noite.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                info_masc_noite_num = (sexo_masc_infor_noite.Sexo.count()) # numero relativo           
                info_fem_noite_num = (sexo_fem_infor_noite.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {info_masc_noite:.2f}%  feminino - {info_fem_noite:.2f}%
                masculino - {info_masc_noite_num}  feminino - {info_fem_noite_num}''')

                grafico(info_masc_noite,info_fem_noite)
                iniciar_menu2()
                break

            elif escolha_curso == 5:    
                seguranca_do_trabalho_noite = dados[dados.Coluna1 == "SEGURANÇA DO TRABALHO -NOITE"]
                sexo_masc_seg_noite = seguranca_do_trabalho_noite[seguranca_do_trabalho_noite.Sexo == "Masculino"]
                sexo_fem_seg_noite = seguranca_do_trabalho_noite[seguranca_do_trabalho_noite.Sexo == "Feminino"]

                # nova parte com calculo de percentual
                seg_masc_noite = ((sexo_masc_seg_noite.Sexo.count() *100) / seguranca_do_trabalho_noite.Coluna1.count()) # percentual                 
                seg_fem_noite  = ((sexo_fem_seg_noite.Sexo.count() * 100) / seguranca_do_trabalho_noite.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                seg_masc_noite_num = (sexo_masc_seg_noite.Sexo.count()) # numero relativo           
                seg_fem_noite_num = (sexo_fem_seg_noite.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {seg_masc_noite:.2f}%  feminino - {seg_fem_noite:.2f}%
                masculino - {seg_masc_noite_num}  feminino - {seg_fem_noite_num}''')

                grafico(seg_masc_noite,seg_fem_noite)
                iniciar_menu2()
                break

            elif escolha_curso == 6:    
                analises_clinicas_tarde = dados[dados.Coluna1 == "ANÁLISES CLÍNICAS / TARDE"]
                sexo_masc_acl_tarde = analises_clinicas_tarde[analises_clinicas_tarde.Sexo == "Masculino"]
                sexo_fem_acl_tarde = analises_clinicas_tarde[analises_clinicas_tarde.Sexo == "Feminino"]

                 # nova parte com calculo de percentual
                acl_masc_tarde = ((sexo_masc_acl_tarde.Sexo.count() *100) / analises_clinicas_tarde.Coluna1.count()) # percentual                 
                acl_fem_tarde  = ((sexo_fem_acl_tarde.Sexo.count() * 100) / analises_clinicas_tarde.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                acl_masc_tarde_num = (sexo_masc_acl_tarde.Sexo.count()) # numero relativo           
                acl_fem_tarde_num = (sexo_fem_acl_tarde.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {acl_masc_tarde:.2f}%  feminino - {acl_fem_tarde:.2f}%
                masculino - {acl_masc_tarde_num}  feminino - {acl_fem_tarde_num}''')

                grafico(acl_masc_tarde,acl_fem_tarde)
                iniciar_menu2()
                break

            elif escolha_curso == 7:    
                edificacoes_noite = dados[dados.Coluna1 == "EDIFICAÇÕES / NOITE"]
                sexo_masc_edf_noite= edificacoes_noite[edificacoes_noite.Sexo == "Masculino"]
                sexo_fem_edf_noite= edificacoes_noite[edificacoes_noite.Sexo == "Feminino"]

                 # nova parte com calculo de percentual
                edf_masc_noite = ((sexo_masc_edf_noite.Sexo.count() *100) / edificacoes_noite.Coluna1.count()) # percentual                 
                edf_fem_noite  = ((sexo_fem_edf_noite.Sexo.count() * 100) / edificacoes_noite.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                edf_masc_noite_num = (sexo_masc_edf_noite.Sexo.count()) # numero relativo           
                edf_fem_noite_num = (sexo_fem_edf_noite.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {edf_masc_noite:.2f}%  feminino - {edf_fem_noite:.2f}%
                masculino - {edf_masc_noite_num}  feminino - {edf_fem_noite_num}''')
                
                grafico(edf_masc_noite,edf_fem_noite)
                iniciar_menu2()
                break

            elif escolha_curso == 8:    
                eletrotecnica_noite = dados[dados.Coluna1 == "ELETROTÉCNICA / NOITE"]
                sexo_masc_elt_noite= eletrotecnica_noite[eletrotecnica_noite.Sexo == "Masculino"]
                sexo_fem_elt_noite= eletrotecnica_noite[eletrotecnica_noite.Sexo == "Feminino"]

                 # nova parte com calculo de percentual
                elt_masc_noite = ((sexo_masc_elt_noite.Sexo.count() *100) / eletrotecnica_noite.Coluna1.count()) # percentual                 
                elt_fem_noite  = ((sexo_fem_elt_noite.Sexo.count() * 100) / eletrotecnica_noite.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                elt_masc_noite_num = (sexo_masc_elt_noite.Sexo.count()) # numero relativo           
                elt_fem_noite_num = (sexo_fem_elt_noite.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {elt_masc_noite:.2f}%  feminino - {elt_fem_noite:.2f}%
                masculino - {elt_masc_noite_num}  feminino - {elt_fem_noite_num}''')
                
                grafico(elt_masc_noite,elt_fem_noite)
                iniciar_menu2()
                break

            elif escolha_curso == 9:    
                mecanica_noite = dados[dados.Coluna1 == "MECÂNICA / NOITE"]
                sexo_masc_mec_noite= mecanica_noite[mecanica_noite.Sexo == "Masculino"]
                sexo_fem_mec_noite= mecanica_noite[mecanica_noite.Sexo == "Feminino"]

                # nova parte com calculo de percentual
                mec_masc_noite = ((sexo_masc_mec_noite.Sexo.count() *100) / mecanica_noite.Coluna1.count()) # percentual                 
                mec_fem_noite  = ((sexo_fem_mec_noite.Sexo.count() * 100) / mecanica_noite.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                mec_masc_noite_num = (sexo_masc_mec_noite.Sexo.count()) # numero relativo           
                mec_fem_noite_num = (sexo_fem_mec_noite.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {mec_masc_noite:.2f}%  feminino - {mec_fem_noite:.2f}%
                masculino - {mec_masc_noite_num}  feminino - {mec_fem_noite_num}''')
                
                grafico(mec_masc_noite,mec_fem_noite)
                iniciar_menu2()
                break

            elif escolha_curso == 10:    
                agricultura_tarde = dados[dados.Coluna1 == "AGRICULTURA / TARDE"]                                 
                sexo_masc_agr_tarde= agricultura_tarde[agricultura_tarde.Sexo == "Masculino"]
                sexo_fem_agr_tarde = agricultura_tarde[agricultura_tarde.Sexo == "Feminino"]

                # nova parte com calculo de percentual
                agr_masc_tarde = ((sexo_masc_agr_tarde.Sexo.count() *100) / agricultura_tarde.Coluna1.count()) # percentual                 
                agr_fem_tarde  = ((sexo_fem_agr_tarde.Sexo.count() * 100) / agricultura_tarde.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                agr_masc_tarde_num = (sexo_masc_agr_tarde.Sexo.count()) # numero relativo           
                agr_fem_tarde_num = (sexo_fem_agr_tarde.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {agr_masc_tarde:.2f}%  feminino - {agr_fem_tarde:.2f}%
                masculino - {agr_masc_tarde_num}  feminino - {agr_fem_tarde_num}''')
                
                grafico(agr_masc_tarde,agr_fem_tarde)
                iniciar_menu2()
                break

            elif escolha_curso == 11:    
                contabilidade_tarde = dados[dados.Coluna1 == "CONTABILIDADE / TARDE"]
                sexo_masc_ctb_tarde= contabilidade_tarde[contabilidade_tarde.Sexo == "Masculino"]
                sexo_fem_ctb_tarde = contabilidade_tarde[contabilidade_tarde.Sexo == "Feminino"]

                # nova parte com calculo de percentual
                ctb_masc_tarde = ((sexo_masc_ctb_tarde.Sexo.count() *100) / contabilidade_tarde.Coluna1.count()) # percentual                 
                ctb_fem_tarde  = ((sexo_fem_ctb_tarde.Sexo.count() * 100) / contabilidade_tarde.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                ctb_masc_tarde_num = (sexo_masc_ctb_tarde.Sexo.count()) # numero relativo           
                ctb_fem_tarde_num = (sexo_fem_ctb_tarde.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {ctb_masc_tarde:.2f}%  feminino - {ctb_fem_tarde:.2f}%
                masculino - {ctb_masc_tarde_num}  feminino - {ctb_fem_tarde_num}''')
               
                grafico(ctb_masc_tarde,ctb_fem_tarde)
                iniciar_menu2()
                break

            elif escolha_curso == 12:    
                contabilidade_noite = dados[dados.Coluna1 == "CONTABILIDADE / NOITE"]
                sexo_masc_ctb_noite= contabilidade_noite[contabilidade_noite.Sexo == "Masculino"]
                sexo_fem_ctb_noite = contabilidade_noite[contabilidade_noite.Sexo == "Feminino"]
                
                # nova parte com calculo de percentual
                ctb_masc_noite = ((sexo_masc_ctb_noite.Sexo.count() *100) / contabilidade_noite.Coluna1.count()) # percentual                 
                ctb_fem_noite  = ((sexo_fem_ctb_noite.Sexo.count() * 100) / contabilidade_noite.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                ctb_masc_noite_num = (sexo_masc_ctb_noite.Sexo.count()) # numero relativo           
                ctb_fem_noite_num = (sexo_fem_ctb_noite.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {ctb_masc_noite:.2f}%  feminino - {ctb_fem_noite:.2f}%
                masculino - {ctb_masc_noite_num}  feminino - {ctb_fem_noite_num}''')
               
                grafico(ctb_masc_noite,ctb_fem_noite)
                iniciar_menu2()
                break

            elif escolha_curso == 13:    
                refrigeracao_climatizacao_noite = dados[dados.Coluna1 == "REFRIGERAÇÃO E CLIMATIZAÇÃO / NOITE"]
                sexo_masc_rec_noite= refrigeracao_climatizacao_noite[refrigeracao_climatizacao_noite.Sexo == "Masculino"]
                sexo_fem_rec_noite = refrigeracao_climatizacao_noite[refrigeracao_climatizacao_noite.Sexo == "Feminino"]

                                # nova parte com calculo de percentual
                rec_masc_noite = ((sexo_masc_rec_noite.Sexo.count() *100) / refrigeracao_climatizacao_noite.Coluna1.count()) # percentual                 
                rec_fem_noite  = ((sexo_fem_rec_noite.Sexo.count() * 100) / refrigeracao_climatizacao_noite.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                rec_masc_noite_num = (sexo_masc_rec_noite.Sexo.count()) # numero relativo           
                rec_fem_noite_num = (sexo_fem_rec_noite.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {rec_masc_noite:.2f}%  feminino - {rec_fem_noite:.2f}%
                masculino - {rec_masc_noite_num}  feminino - {rec_fem_noite_num}''')
               
                grafico(rec_masc_noite_num,rec_fem_noite)
                iniciar_menu2()
                break

            elif escolha_curso == 14:    
                eletronica_noite = dados[dados.Coluna1 == "ELETRÔNICA / NOITE"]
                sexo_masc_ele_noite= eletronica_noite[eletronica_noite.Sexo == "Masculino"]
                sexo_fem_ele_noite = eletronica_noite[eletronica_noite.Sexo == "Feminino"]
                        
                # nova parte com calculo de percentual
                ele_masc_noite = ((sexo_masc_ele_noite.Sexo.count() *100) / eletronica_noite.Coluna1.count()) # percentual                 
                ele_fem_noite  = ((sexo_fem_ele_noite.Sexo.count() * 100) / eletronica_noite.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                ele_masc_noite_num = (sexo_masc_ele_noite.Sexo.count()) # numero relativo           
                ele_fem_noite_num = (sexo_fem_ele_noite.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {ele_masc_noite:.2f}%  feminino - {ele_fem_noite:.2f}%
                masculino - {ele_masc_noite_num}  feminino - {ele_fem_noite_num}''')
               
                grafico(ele_masc_noite,ele_fem_noite)
                iniciar_menu2()
                break

            elif escolha_curso == 15:    
                vestuario_noite = dados[dados.Coluna1 == "VESTUÁRIO / NOITE"]
                sexo_masc_vst_noite= vestuario_noite[vestuario_noite.Sexo == "Masculino"]
                sexo_fem_vst_noite = vestuario_noite[vestuario_noite.Sexo == "Feminino"]

                # nova parte com calculo de percentual
                vst_masc_noite = ((sexo_masc_vst_noite.Sexo.count() *100) / vestuario_noite.Coluna1.count()) # percentual                 
                vst_fem_noite  = ((sexo_fem_vst_noite.Sexo.count() * 100) / vestuario_noite.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                vst_masc_noite_num = (sexo_masc_vst_noite.Sexo.count()) # numero relativo           
                vst_fem_noite_num = (sexo_fem_vst_noite.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {vst_masc_noite:.2f}%  feminino - {vst_fem_noite:.2f}%
                masculino - {vst_masc_noite_num}  feminino - {vst_fem_noite_num}''')
               
                grafico(vst_masc_noite,vst_fem_noite)
                iniciar_menu2()
                break

            elif escolha_curso == 16:    
                estradas_tarde = dados[dados.Coluna1 == "ESTRADAS / TARDE"]
                sexo_masc_est_tarde= estradas_tarde[estradas_tarde.Sexo == "Masculino"]
                sexo_fem_est_tarde = estradas_tarde[estradas_tarde.Sexo == "Feminino"]

                # nova parte com calculo de percentual
                est_masc_tarde = ((sexo_masc_est_tarde.Sexo.count() *100) / estradas_tarde.Coluna1.count()) # percentual                 
                est_fem_tarde  = ((sexo_fem_est_tarde.Sexo.count() * 100) / estradas_tarde.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                est_masc_tarde_num = (sexo_masc_est_tarde.Sexo.count()) # numero relativo           
                est_fem_tarde_num = (sexo_fem_est_tarde.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {est_masc_tarde:.2f}%  feminino - {est_fem_tarde:.2f}%
                masculino - {est_masc_tarde_num}  feminino - {est_fem_tarde_num}''')
               
                grafico(est_masc_tarde,est_fem_tarde)
                iniciar_menu2()
                break

            elif escolha_curso == 17:    
                agricultura_manha = dados[dados.Coluna1 == "AGRICULTURA / MANHÃ"]
                sexo_masc_agc_manha= agricultura_manha[agricultura_manha.Sexo == "Masculino"]
                sexo_fem_agc_manha= agricultura_manha[agricultura_manha.Sexo == "Feminino"]
                
                # nova parte com calculo de percentual
                agc_masc_manha = ((sexo_masc_agc_manha.Sexo.count() *100) / agricultura_manha.Coluna1.count()) # percentual                 
                agc_fem_manha  = ((sexo_fem_agc_manha.Sexo.count() * 100) / agricultura_manha.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                agc_masc_manha_num = (sexo_masc_agc_manha.Sexo.count()) # numero relativo           
                agc_fem_manha_num = (sexo_fem_agc_manha.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {agc_masc_manha:.2f}%  feminino - {agc_fem_manha:.2f}%
                masculino - {agc_masc_manha_num}  feminino - {agc_fem_manha_num}''')

                grafico(agc_masc_manha,agc_fem_manha)
                iniciar_menu2()
                break

            elif escolha_curso == 18:    
                mineracao_tarde = dados[dados.Coluna1 == "MINERAÇÃO / TARDE"]
                sexo_masc_min_tarde= mineracao_tarde[mineracao_tarde.Sexo == "Masculino"]
                sexo_fem_min_tarde = mineracao_tarde[mineracao_tarde.Sexo == "Feminino"]

                # nova parte com calculo de percentual
                min_masc_tarde = ((sexo_masc_min_tarde.Sexo.count() *100) / mineracao_tarde.Coluna1.count()) # percentual                 
                min_fem_tarde  = ((sexo_fem_min_tarde.Sexo.count() * 100) / mineracao_tarde.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                min_masc_tarde_num = (sexo_masc_min_tarde.Sexo.count()) # numero relativo           
                min_fem_tarde_num = (sexo_fem_min_tarde.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {min_masc_tarde:.2f}%  feminino - {min_fem_tarde:.2f}%
                masculino - {min_masc_tarde_num}  feminino - {min_fem_tarde_num}''')
               
                grafico(min_masc_tarde,min_fem_tarde)
                iniciar_menu2()
                break

            elif escolha_curso == 19:    
                panificacao_tarde = dados[dados.Coluna1 == "PANIFICAÇÃO / TARDE"]
                sexo_masc_pan_tarde= panificacao_tarde[panificacao_tarde.Sexo == "Masculino"]
                sexo_fem_pan_tarde = panificacao_tarde[panificacao_tarde.Sexo == "Feminino"]

                 # nova parte com calculo de percentual
                pan_masc_tarde = ((sexo_masc_pan_tarde.Sexo.count() *100) / panificacao_tarde.Coluna1.count()) # percentual                 
                pan_fem_tarde  = ((sexo_fem_pan_tarde.Sexo.count() * 100) / panificacao_tarde.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                pan_masc_tarde_num = (sexo_masc_pan_tarde.Sexo.count()) # numero relativo           
                pan_fem_tarde_num = (sexo_fem_pan_tarde.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {pan_masc_tarde:.2f}%  feminino - {pan_fem_tarde:.2f}%
                masculino - {pan_masc_tarde_num}  feminino - {pan_fem_tarde_num}''')
               
                grafico(pan_masc_tarde,pan_fem_tarde)
                iniciar_menu2()
                break

            elif escolha_curso == 20:    
                alimentos_tarde = dados[dados.Coluna1 == "ALIMENTOS / TARDE"]
                sexo_masc_ali_tarde= alimentos_tarde[alimentos_tarde.Sexo == "Masculino"]
                sexo_fem_ali_tarde = alimentos_tarde[alimentos_tarde.Sexo == "Feminino"]

                # nova parte com calculo de percentual
                ali_masc_tarde = ((sexo_masc_ali_tarde.Sexo.count() *100) / alimentos_tarde.Coluna1.count()) # percentual                 
                ali_fem_tarde  = ((sexo_fem_ali_tarde.Sexo.count() * 100) / alimentos_tarde.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                ali_masc_tarde_num = (sexo_masc_ali_tarde.Sexo.count()) # numero relativo           
                ali_fem_tarde_num = (sexo_fem_ali_tarde.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {ali_masc_tarde:.2f}%  feminino - {ali_fem_tarde:.2f}%
                masculino - {ali_masc_tarde_num}  feminino - {ali_fem_tarde_num}''')
               
                grafico(ali_masc_tarde,ali_fem_tarde)
                iniciar_menu2()
                break
            

            elif escolha_curso == 21:    
                informatica_para_internet = dados[dados.Coluna1 == "INFORMÁTICA PARA INTERNET / NOITE"]
                sexo_masc_ipi_noite= informatica_para_internet[informatica_para_internet.Sexo == "Masculino"]
                sexo_fem_ipi_noite = informatica_para_internet[informatica_para_internet.Sexo == "Feminino"]

                # nova parte com calculo de percentual
                ipi_masc_noite = ((sexo_masc_ipi_noite.Sexo.count() *100) / informatica_para_internet.Coluna1.count()) # percentual                 
                ipi_fem_noite  = ((sexo_fem_ipi_noite.Sexo.count() * 100) / informatica_para_internet.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                ipi_masc_noite_num = (sexo_masc_ipi_noite.Sexo.count()) # numero relativo           
                ipi_fem_noite_num = (sexo_fem_ipi_noite.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {ipi_masc_noite:.2f}%  feminino - {ipi_fem_noite:.2f}%
                masculino - {ipi_masc_noite_num}  feminino - {ipi_fem_noite_num}''')
               
                grafico(ipi_masc_noite,ipi_fem_noite)
                iniciar_menu2()
                break

            elif escolha_curso == 22:    
                agroindustria_manha = dados[dados.Coluna1 == "AGROINDÚSTRIA / MANHÃ"]
                sexo_masc_agi_manha= agroindustria_manha[agroindustria_manha.Sexo == "Masculino"]
                sexo_fem_agi_manha= agroindustria_manha[agroindustria_manha.Sexo == "Feminino"]

                # nova parte com calculo de percentual
                agi_masc_manha = ((sexo_masc_agi_manha.Sexo.count() *100) / agroindustria_manha.Coluna1.count()) # percentual                 
                agi_fem_manha  = ((sexo_fem_agi_manha.Sexo.count() * 100) / agroindustria_manha.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                agi_masc_manha_num = (sexo_masc_agi_manha.Sexo.count()) # numero relativo           
                agi_fem_manha_num = (sexo_fem_agi_manha.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {agi_masc_manha:.2f}%  feminino - {agi_fem_manha:.2f}%
                masculino - {agi_masc_manha_num}  feminino - {agi_fem_manha_num}''')
               
                grafico(agi_masc_manha,agi_fem_manha)
                iniciar_menu2()
                break

            elif escolha_curso == 23:    
                inst_music_violao_tarde = dados[dados.Coluna1 == "INSTRUMENTO MUSICAL - VIOLÃO / TARDE"]
                sexo_masc_vio_tarde= inst_music_violao_tarde[inst_music_violao_tarde.Sexo == "Masculino"]
                sexo_fem_vio_tarde = inst_music_violao_tarde[inst_music_violao_tarde.Sexo == "Feminino"]

                # nova parte com calculo de percentual
                vio_masc_tarde = ((sexo_masc_vio_tarde.Sexo.count() *100) / inst_music_violao_tarde.Coluna1.count()) # percentual                 
                vio_fem_tarde  = ((sexo_fem_vio_tarde.Sexo.count() * 100) / inst_music_violao_tarde.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                vio_masc_tarde_num = (sexo_masc_vio_tarde.Sexo.count()) # numero relativo           
                vio_fem_tarde_num = (sexo_fem_vio_tarde.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {vio_masc_tarde:.2f}%  feminino - {vio_fem_tarde:.2f}%
                masculino - {vio_masc_tarde_num}  feminino - {vio_fem_tarde_num}''')
               
                grafico(vio_masc_tarde,vio_fem_tarde)
                iniciar_menu2()
                break

            elif escolha_curso == 24:    
                fruticultura_tarde = dados[dados.Coluna1 == "FRUTICULTURA / TARDE"]
                sexo_masc_fru_tarde= fruticultura_tarde[fruticultura_tarde.Sexo == "Masculino"]
                sexo_fem_fru_tarde = fruticultura_tarde[fruticultura_tarde.Sexo == "Feminino"]

                 # nova parte com calculo de percentual
                fru_masc_tarde = ((sexo_masc_fru_tarde.Sexo.count() *100) / fruticultura_tarde.Coluna1.count()) # percentual                 
                fru_fem_tarde  = ((sexo_fem_fru_tarde.Sexo.count() * 100) / fruticultura_tarde.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                fru_masc_tarde_num = (sexo_masc_fru_tarde.Sexo.count()) # numero relativo           
                fru_fem_tarde_num = (sexo_fem_fru_tarde.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {fru_masc_tarde:.2f}%  feminino - {fru_fem_tarde:.2f}%
                masculino - {fru_masc_tarde_num}  feminino - {fru_fem_tarde_num}''')
               
                grafico(fru_masc_tarde,fru_fem_tarde)
                iniciar_menu2()
                break


            elif escolha_curso == 25:    
                inst_music_trompete_tarde = dados[dados.Coluna1 == "INSTRUMENTO MUSICAL - TROMPETE / TARDE"]
                sexo_masc_tromp_tarde= inst_music_trompete_tarde[inst_music_trompete_tarde.Sexo == "Masculino"]
                sexo_fem_tromp_tarde = inst_music_trompete_tarde[inst_music_trompete_tarde.Sexo == "Feminino"]

                 # nova parte com calculo de percentual
                tromp_masc_tarde = ((sexo_masc_tromp_tarde.Sexo.count() *100) / inst_music_trompete_tarde.Coluna1.count()) # percentual                 
                tromp_fem_tarde  = ((sexo_fem_tromp_tarde.Sexo.count() * 100) / inst_music_trompete_tarde.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                tromp_masc_tarde_num = (sexo_masc_tromp_tarde.Sexo.count()) # numero relativo           
                tromp_fem_tarde_num = (sexo_fem_tromp_tarde.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {tromp_masc_tarde:.2f}%  feminino - {tromp_fem_tarde:.2f}%
                masculino - {tromp_masc_tarde_num}  feminino - {tromp_fem_tarde_num}''')
               
                grafico(tromp_masc_tarde,tromp_fem_tarde)
                iniciar_menu2()
                break


            elif escolha_curso == 26:    
                rest_e_bar = dados[dados.Coluna1 == "RESTAURANTE E BAR / TARDE"]
                sexo_masc_rest_tarde= rest_e_bar[rest_e_bar.Sexo == "Masculino"]
                sexo_fem_rest_tarde = rest_e_bar[rest_e_bar.Sexo == "Feminino"]

                 # nova parte com calculo de percentual
                rest_masc_tarde = ((sexo_masc_rest_tarde.Sexo.count() *100) / rest_e_bar.Coluna1.count()) # percentual                 
                rest_fem_tarde  = ((sexo_fem_rest_tarde.Sexo.count() * 100) / rest_e_bar.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                rest_masc_tarde_num = (sexo_masc_rest_tarde.Sexo.count()) # numero relativo           
                rest_fem_tarde_num = (sexo_fem_rest_tarde.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {rest_masc_tarde:.2f}%  feminino - {rest_fem_tarde:.2f}%
                masculino - {rest_masc_tarde_num}  feminino - {rest_fem_tarde_num}''')
               
                grafico(rest_masc_tarde,rest_fem_tarde)
                iniciar_menu2()
                break

            elif escolha_curso == 27:    
                inst_music_teclado_tarde = dados[dados.Coluna1 == "INSTRUMENTO MUSICAL - TECLADO ELETRÔNICO / TARDE"]
                sexo_masc_tecl_tarde= inst_music_teclado_tarde[inst_music_teclado_tarde.Sexo == "Masculino"]
                sexo_fem_tecl_tarde = inst_music_teclado_tarde[inst_music_teclado_tarde.Sexo == "Feminino"]
                
                # nova parte com calculo de percentual
                tecl_masc_tarde = ((sexo_masc_tecl_tarde.Sexo.count() *100) / inst_music_teclado_tarde.Coluna1.count()) # percentual                 
                tecl_fem_tarde  = ((sexo_fem_tecl_tarde.Sexo.count() * 100) / inst_music_teclado_tarde.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                tecl_masc_tarde_num = (sexo_masc_tecl_tarde.Sexo.count()) # numero relativo           
                tecl_fem_tarde_num = (sexo_fem_tecl_tarde.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {tecl_masc_tarde:.2f}%  feminino - {tecl_fem_tarde:.2f}%
                masculino - {tecl_masc_tarde_num}  feminino - {tecl_fem_tarde_num}''')
               
                grafico(tecl_masc_tarde,tecl_fem_tarde)
                iniciar_menu2()
                break

            elif escolha_curso == 28:    
                inst_music_trombone_tarde = dados[dados.Coluna1 == "INSTRUMENTO MUSICAL - TROMBONE / TARDE"]
                sexo_masc_tromb_tarde= inst_music_trombone_tarde[inst_music_trombone_tarde.Sexo == "Masculino"]
                sexo_fem_tromb_tarde = inst_music_trombone_tarde[inst_music_trombone_tarde.Sexo == "Feminino"]

                # nova parte com calculo de percentual
                tromb_masc_tarde = ((sexo_masc_tromb_tarde.Sexo.count() *100) / inst_music_trombone_tarde.Coluna1.count()) # percentual                 
                tromb_fem_tarde  = ((sexo_fem_tromb_tarde.Sexo.count() * 100) / inst_music_trombone_tarde.Coluna1.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                tromb_masc_tarde_num = (sexo_masc_tromb_tarde.Sexo.count()) # numero relativo           
                tromb_fem_tarde_num = (sexo_fem_tromb_tarde.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {tromb_masc_tarde:.2f}%  feminino - {tromb_fem_tarde:.2f}%
                masculino - {tromb_masc_tarde_num}  feminino - {tromb_fem_tarde_num}''')
               
                grafico(tromb_masc_tarde,tromb_fem_tarde)
                iniciar_menu2()
                break
            
            elif escolha_curso == 100:
                menu_inicial()
                break
        

            elif escolha_curso == 0:
                break
            

            else:
                print("A opção digitada está inválida, Digite novamente!") 

        except:
            print("A opção digitada está inválida, Digite novamente!") 

def analise_campus():
    while True:
        try:
            escolha_campus = int(input("""
            Escolha uma opção
            ---------------------------------------------
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
            ---------------------------------------------
            [100]  - Voltar para o Menu Principal
            [0]  - Sair do Programa
            ---------------------------------------------
        Opção: """))


            if escolha_campus == 1:
                Teresina_Central = (dados[dados.Unidade == "TERESINA - CENTRAL"])
                
                sexo_masc = (Teresina_Central[Teresina_Central.Sexo == "Masculino"])
                sexo_fem = (Teresina_Central[Teresina_Central.Sexo == "Feminino"])
                 
                # nova parte com calculo de percentual
                tc_sexo_masc = ((sexo_masc.Sexo.count() *100) / Teresina_Central.Unidade.count()) # percentual                 
                tc_sexo_fem = ((sexo_fem.Sexo.count() * 100) / Teresina_Central.Unidade.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                tc_sexo_masc_num = (sexo_masc.Sexo.count()) # numero relativo           
                tc_sexo_fem_num = (sexo_fem.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {tc_sexo_masc:.2f}%  feminino - {tc_sexo_fem:.2f}%
                masculino - {tc_sexo_masc_num}  feminino - {tc_sexo_fem_num}''')

                grafico2(tc_sexo_masc,tc_sexo_fem)
                iniciar_menu()
                break
                
            elif escolha_campus == 2:
                Teresina_Sul = (dados[dados.Unidade == "TERESINA - ZONA SUL"])
                sexo_masc = (Teresina_Sul[Teresina_Sul.Sexo == "Masculino"])
                sexo_fem = (Teresina_Sul[Teresina_Sul.Sexo == "Feminino"])
                
                # nova parte com calculo de percentual
                ts_sexo_masc = ((sexo_masc.Sexo.count() *100) / Teresina_Sul.Unidade.count()) # percentual                 
                ts_sexo_fem = ((sexo_fem.Sexo.count() * 100) / Teresina_Sul.Unidade.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                Ts_sexo_masc_num = (sexo_masc.Sexo.count()) # numero relativo           
                Ts_sexo_fem_num = (sexo_fem.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {ts_sexo_masc:.2f}%  feminino - {ts_sexo_fem:.2f}%
                masculino - {Ts_sexo_masc_num}  feminino - {Ts_sexo_fem_num}''')

                grafico2(ts_sexo_masc,ts_sexo_fem)
                iniciar_menu()
                break

            elif escolha_campus == 3:
                CORRENTE = (dados[dados.Unidade == "CORRENTE"])
                sexo_masc = (CORRENTE[CORRENTE.Sexo == "Masculino"])
                sexo_fem = (CORRENTE[CORRENTE.Sexo == "Feminino"])
                
                
                # nova parte com calculo de percentual
                corrente_sexo_masc = ((sexo_masc.Sexo.count() *100) / CORRENTE.Unidade.count()) # percentual                 
                corrente_sexo_fem= ((sexo_fem.Sexo.count() * 100) / CORRENTE.Unidade.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                corrente_sexo_masc_num = (sexo_masc.Sexo.count()) # numero relativo           
                corrente_sexo_fem_num = (sexo_fem.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {corrente_sexo_masc:.2f}%  feminino - {corrente_sexo_fem:.2f}%
                masculino - {corrente_sexo_masc_num}  feminino - {corrente_sexo_fem_num}''')

                grafico2(corrente_sexo_masc,corrente_sexo_fem)
                iniciar_menu()
                break

            elif escolha_campus == 4:
                OEIRAS = (dados[dados.Unidade == "OEIRAS"])
                sexo_masc = (OEIRAS[OEIRAS.Sexo == "Masculino"])
                sexo_fem = (OEIRAS[OEIRAS.Sexo == "Feminino"])
                
                # nova parte com calculo de percentual
                oeiras_sexo_masc = ((sexo_masc.Sexo.count() *100) / OEIRAS.Unidade.count()) # percentual                 
                oeiras_sexo_fem = ((sexo_fem.Sexo.count() * 100) / OEIRAS.Unidade.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                oeiras_sexo_masc_num = (sexo_masc.Sexo.count()) # numero relativo           
                oeiras_sexo_fem_num = (sexo_fem.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {oeiras_sexo_masc:.2f}%  feminino - {oeiras_sexo_fem:.2f}%
                masculino - {oeiras_sexo_masc_num}  feminino - {oeiras_sexo_fem_num}''')

                grafico2(oeiras_sexo_masc,oeiras_sexo_fem)
                iniciar_menu()
                break

            elif escolha_campus == 5:
                VALENCA = (dados[dados.Unidade == "VALENÇA"])
                sexo_masc = (VALENCA[VALENCA.Sexo == "Masculino"])
                sexo_fem = (VALENCA[VALENCA.Sexo == "Feminino"])
                
                # nova parte com calculo de percentual
                VALENCA_sexo_masc = ((sexo_masc.Sexo.count() *100) / VALENCA.Unidade.count()) # percentual                 
                VALENCA_sexo_fem = ((sexo_fem.Sexo.count() * 100) / VALENCA.Unidade.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                VALENCA_sexo_masc_num = (sexo_masc.Sexo.count()) # numero relativo           
                VALENCA_sexo_fem_num = (sexo_fem.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {VALENCA_sexo_masc:.2f}%  feminino - {VALENCA_sexo_fem:.2f}%
                masculino - {VALENCA_sexo_masc_num}  feminino - {VALENCA_sexo_fem_num}''')

                grafico2(VALENCA_sexo_masc,VALENCA_sexo_fem)
                iniciar_menu()
                break

            elif escolha_campus == 6:
                C_FLORIANO = (dados[dados.Unidade == "FLORIANO"])
                sexo_masc = (C_FLORIANO[C_FLORIANO.Sexo == "Masculino"])
                sexo_fem = (C_FLORIANO[C_FLORIANO.Sexo == "Feminino"])
                
                # nova parte com calculo de percentual
                floriano_sexo_masc = ((sexo_masc.Sexo.count() *100) / C_FLORIANO.Unidade.count()) # percentual                 
                floriano_sexo_fem = ((sexo_fem.Sexo.count() * 100) / C_FLORIANO.Unidade.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                floriano_sexo_masc_num = (sexo_masc.Sexo.count()) # numero relativo           
                floriano_sexo_fem_num = (sexo_fem.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {floriano_sexo_masc:.2f}%  feminino - {floriano_sexo_fem:.2f}%
                masculino - {floriano_sexo_masc_num}  feminino - {floriano_sexo_fem_num}''')

                grafico2(floriano_sexo_masc,floriano_sexo_fem)
                iniciar_menu()
                break

            elif escolha_campus == 7:
                PICOS = (dados[dados.Unidade == "PICOS"])
                sexo_masc = (PICOS[PICOS.Sexo == "Masculino"])
                sexo_fem = (PICOS[PICOS.Sexo == "Feminino"])
                
 # nova parte com calculo de percentual
                PICOS_sexo_masc = ((sexo_masc.Sexo.count() *100) / PICOS.Unidade.count()) # percentual                 
                PICOS_sexo_fem = ((sexo_fem.Sexo.count() * 100) / PICOS.Unidade.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                PICOS_sexo_masc_num = (sexo_masc.Sexo.count()) # numero relativo           
                PICOS_sexo_fem_num = (sexo_fem.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {PICOS_sexo_masc:.2f}%  feminino - {PICOS_sexo_fem:.2f}%
                masculino - {PICOS_sexo_masc_num}  feminino - {PICOS_sexo_fem_num}''')

                grafico2(PICOS_sexo_masc,PICOS_sexo_fem)
                iniciar_menu()
                break

            elif escolha_campus == 8:
                SJ_PIAUI = (dados[dados.Unidade == "SÃO JOÃO DO PIAUÍ"])
                sexo_masc = (SJ_PIAUI[SJ_PIAUI.Sexo == "Masculino"])
                sexo_fem = (SJ_PIAUI[SJ_PIAUI.Sexo == "Feminino"])
                
                # nova parte com calculo de percentual
                SJ_PIAUI_sexo_masc = ((sexo_masc.Sexo.count() *100) / SJ_PIAUI.Unidade.count()) # percentual                 
                SJ_PIAUI_sexo_fem = ((sexo_fem.Sexo.count() * 100) / SJ_PIAUI.Unidade.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                SJ_PIAUI_sexo_masc_num = (sexo_masc.Sexo.count()) # numero relativo           
                SJ_PIAUI_sexo_fem_num = (sexo_fem.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {SJ_PIAUI_sexo_masc:.2f}%  feminino - {SJ_PIAUI_sexo_fem:.2f}%
                masculino - {SJ_PIAUI_sexo_masc_num}  feminino - {SJ_PIAUI_sexo_fem_num}''')

                grafico2(SJ_PIAUI_sexo_masc,SJ_PIAUI_sexo_fem)
                iniciar_menu()
                break
                
            elif escolha_campus == 9:
                PIRIPIRI = (dados[dados.Unidade == "PIRIPIRI"])
                sexo_masc = (PIRIPIRI[PIRIPIRI.Sexo == "Masculino"])
                sexo_fem = (PIRIPIRI[PIRIPIRI.Sexo == "Feminino"])
                
                # nova parte com calculo de percentual
                PIRIPIRI_sexo_masc = ((sexo_masc.Sexo.count() *100) / PIRIPIRI.Unidade.count()) # percentual                 
                PIRIPIRI_sexo_fem = ((sexo_fem.Sexo.count() * 100) / PIRIPIRI.Unidade.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                PIRIPIRI_sexo_masc_num = (sexo_masc.Sexo.count()) # numero relativo           
                PIRIPIRI_sexo_fem_num = (sexo_fem.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {PIRIPIRI_sexo_masc:.2f}%  feminino - {PIRIPIRI_sexo_fem:.2f}%
                masculino - {PIRIPIRI_sexo_masc_num}  feminino - {PIRIPIRI_sexo_fem_num}''')

                grafico2(PIRIPIRI_sexo_masc,PIRIPIRI_sexo_fem)
                iniciar_menu()
                break

            elif escolha_campus == 10:
                PARNAIBA = (dados[dados.Unidade == "PARNAÍBA"])
                sexo_masc = (PARNAIBA[PARNAIBA.Sexo == "Masculino"])
                sexo_fem = (PARNAIBA[PARNAIBA.Sexo == "Feminino"])
                
                 # nova parte com calculo de percentual
                PARNAIBA_sexo_masc = ((sexo_masc.Sexo.count() *100) / PARNAIBA.Unidade.count()) # percentual                 
                PARNAIBA_sexo_fem = ((sexo_fem.Sexo.count() * 100) / PARNAIBA.Unidade.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                PARNAIBA_sexo_masc_num = (sexo_masc.Sexo.count()) # numero relativo           
                PARNAIBA_sexo_fem_num = (sexo_fem.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {PARNAIBA_sexo_masc:.2f}%  feminino - {PARNAIBA_sexo_fem:.2f}%
                masculino - {PARNAIBA_sexo_masc_num}  feminino - {PARNAIBA_sexo_fem_num}''')

                grafico2(PARNAIBA_sexo_masc,PARNAIBA_sexo_fem)
                iniciar_menu()
                break
                

            elif escolha_campus == 11:
                COCAL = (dados[dados.Unidade == "COCAL"])
                sexo_masc = (COCAL[COCAL.Sexo == "Masculino"])
                sexo_fem = (COCAL[COCAL.Sexo == "Feminino"])
                
                 # nova parte com calculo de percentual
                COCAL_sexo_masc = ((sexo_masc.Sexo.count() *100) / COCAL.Unidade.count()) # percentual                 
                COCAL_sexo_fem = ((sexo_fem.Sexo.count() * 100) / COCAL.Unidade.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                COCAL_sexo_masc_num = (sexo_masc.Sexo.count()) # numero relativo           
                COCAL_sexo_fem_num = (sexo_fem.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {COCAL_sexo_masc:.2f}%  feminino - {COCAL_sexo_fem:.2f}%
                masculino - {COCAL_sexo_masc_num}  feminino - {COCAL_sexo_fem_num}''')

                grafico2(COCAL_sexo_masc,COCAL_sexo_fem)
                iniciar_menu()
                break

            elif escolha_campus == 12:
                ANGICAL = (dados[dados.Unidade == "ANGICAL"])
                sexo_masc = (ANGICAL[ANGICAL.Sexo == "Masculino"])
                sexo_fem = (ANGICAL[ANGICAL.Sexo == "Feminino"])
                
                # nova parte com calculo de percentual
                ANGICAL_sexo_masc = ((sexo_masc.Sexo.count() *100) / ANGICAL.Unidade.count()) # percentual                 
                ANGICAL_sexo_fem = ((sexo_fem.Sexo.count() * 100) / ANGICAL.Unidade.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                ANGICAL_sexo_masc_num = (sexo_masc.Sexo.count()) # numero relativo           
                ANGICAL_sexo_fem_num = (sexo_fem.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {ANGICAL_sexo_masc:.2f}%  feminino - {ANGICAL_sexo_fem:.2f}%
                masculino - {ANGICAL_sexo_masc_num}  feminino - {ANGICAL_sexo_fem_num}''')

                grafico2(ANGICAL_sexo_masc,ANGICAL_sexo_fem)
                iniciar_menu()
                break


            elif escolha_campus == 13:
                PEDRO_II = (dados[dados.Unidade == "PEDRO II"])
                sexo_masc = (PEDRO_II[PEDRO_II.Sexo == "Masculino"])
                sexo_fem = (PEDRO_II[PEDRO_II.Sexo== "Feminino"])
                
                # nova parte com calculo de percentual
                PEDRO_II_sexo_masc = ((sexo_masc.Sexo.count() *100) / PEDRO_II.Unidade.count()) # percentual                 
                PEDRO_II_sexo_fem = ((sexo_fem.Sexo.count() * 100) / PEDRO_II.Unidade.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                PEDRO_II_sexo_masc_num = (sexo_masc.Sexo.count()) # numero relativo           
                PEDRO_II_sexo_fem_num = (sexo_fem.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {PEDRO_II_sexo_masc:.2f}%  feminino - {PEDRO_II_sexo_fem:.2f}%
                masculino - {PEDRO_II_sexo_masc_num}  feminino - {PEDRO_II_sexo_fem_num}''')

                grafico2(PEDRO_II_sexo_masc,PEDRO_II_sexo_fem)
                iniciar_menu()
                break


            elif escolha_campus == 14:
                CAMPO_MAIOR = (dados[dados.Unidade == "CAMPO MAIOR"])
                sexo_masc = (CAMPO_MAIOR[CAMPO_MAIOR.Sexo == "Masculino"])
                sexo_fem = (CAMPO_MAIOR[CAMPO_MAIOR.Sexo == "Feminino"])
                
                # nova parte com calculo de percentual
                CAMPO_MAIOR_sexo_masc = ((sexo_masc.Sexo.count() *100) / CAMPO_MAIOR.Unidade.count()) # percentual                 
                CAMPO_MAIOR_sexo_fem = ((sexo_fem.Sexo.count() * 100) / CAMPO_MAIOR.Unidade.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                CAMPO_MAIOR_sexo_masc_num = (sexo_masc.Sexo.count()) # numero relativo           
                CAMPO_MAIOR_sexo_fem_num = (sexo_fem.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {CAMPO_MAIOR_sexo_masc:.2f}%  feminino - {CAMPO_MAIOR_sexo_fem:.2f}%
                masculino - {CAMPO_MAIOR_sexo_masc_num}  feminino - {CAMPO_MAIOR_sexo_fem_num}''')

                grafico2(CAMPO_MAIOR_sexo_masc,CAMPO_MAIOR_sexo_fem)
                iniciar_menu()
                break

            elif escolha_campus == 15:
                PAULISTANA = (dados[dados.Unidade == "PAULISTANA"])
                sexo_masc = (PAULISTANA[PAULISTANA.Sexo == "Masculino"])
                sexo_fem = (PAULISTANA[PAULISTANA.Sexo == "Feminino"])
                
                # nova parte com calculo de percentual
                PAULISTANA_sexo_masc = ((sexo_masc.Sexo.count() *100) / PAULISTANA.Unidade.count()) # percentual                 
                PAULISTANA_sexo_fem = ((sexo_fem.Sexo.count() * 100) / PAULISTANA.Unidade.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                PAULISTANA_sexo_masc_num = (sexo_masc.Sexo.count()) # numero relativo           
                PAULISTANA_sexo_fem_num = (sexo_fem.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {PAULISTANA_sexo_masc:.2f}%  feminino - {PAULISTANA_sexo_fem:.2f}%
                masculino - {PAULISTANA_sexo_masc_num}  feminino - {PAULISTANA_sexo_fem_num}''')

                grafico2(PAULISTANA_sexo_masc,PAULISTANA_sexo_fem)
                iniciar_menu()
                break

            elif escolha_campus == 16:
                URUCUI = (dados[dados.Unidade == "URUÇUÍ"])
                sexo_masc = (URUCUI[URUCUI.Sexo == "Masculino"])
                sexo_fem = (URUCUI[URUCUI.Sexo == "Feminino"])
                
                # nova parte com calculo de percentual
                URUCUI_sexo_masc = ((sexo_masc.Sexo.count() *100) / URUCUI.Unidade.count()) # percentual                 
                URUCUI_sexo_fem = ((sexo_fem.Sexo.count() * 100) / URUCUI.Unidade.count()) # percentual

                # novas variaveis para armazenar o numero relativo
                URUCUI_sexo_masc_num = (sexo_masc.Sexo.count()) # numero relativo           
                URUCUI_sexo_fem_num = (sexo_fem.Sexo.count()) # numero relativo

                # print do percentual e numero relativo
                print(f'''\nmasculino - {URUCUI_sexo_masc:.2f}%  feminino - {URUCUI_sexo_fem:.2f}%
                masculino - {URUCUI_sexo_masc_num}  feminino - {URUCUI_sexo_fem_num}''')

                grafico2(URUCUI_sexo_masc,URUCUI_sexo_fem)
                iniciar_menu()
                break


            elif escolha_campus == 100:
                menu_inicial()
                break
            elif escolha_campus == 0:
                break
            else:
                print("A opção digitada está inválida, Digite novamente!") 

        except:
            print("A opção digitada está inválida, Digite novamente!") 

def menu_inicial():
    while True:
        try:
            opcao = int(input("""
            ---------------------------------------------
            Escolha uma opção para iniciar sua análise:
            ---------------------------------------------
                [1]  - Filtrar por Campus
                [2]  - Filtrar por Curso
            ---------------------------------------------
                [0]  - Sair
            ---------------------------------------------
        Opção: """))

            if opcao == 0:
                break

            elif opcao == 1:
                analise_campus()
                break

            elif opcao == 2:
                analise_curso()
                break

            else:
                print("A opção digitada está inválida, Digite novamente!")


        except:
            print("A opção digitada está inválida, Digite novamente!")

def iniciar_menu2():
    while True:
        try:
            opcao = int(input("""
            ---------------------------------------------
            O que você deseja fazer agora?
            ---------------------------------------------
                [1]  - Voltar para o Menu Principal
                [2]  - Escolher um Novo Curso
            ---------------------------------------------
                [0]  - Sair do Programa
            ---------------------------------------------
        Opção: """))
            if opcao == 0:
                break

            elif opcao == 1:
                menu_inicial()
                break

            elif opcao == 2:
                analise_curso()
                break

            else:
                print("A opção digitada está inválida, Digite novamente!")

        except:
            print("A opção digitada está inválida, Digite novamente!")

def iniciar_menu():
    while True:
        try:
            opcao = int(input("""
            ---------------------------------------------
            O que você deseja fazer agora?
            ---------------------------------------------
                [1]  - Voltar para o Menu Principal
                [2]  - Escolher um Novo Campus
            ---------------------------------------------
                [0]  - Sair do Programa
            ---------------------------------------------
        Opção: """))
            if opcao == 0:
                break

            elif opcao == 1:
                menu_inicial()
                break
            
            elif opcao == 2:
                analise_campus()
                break

            else:
                print("A opção digitada está inválida, Digite novamente!")

        except:
            print("A opção digitada está inválida, Digite novamente!")

print("\n\n\t\t\t\tBem vindo ao programa!!\n\n\tNesse Script você vai poder gerar gráficos sobre a quantidade de candidatos do sexo \nmasculino e feminino, filtrando o candidato por campus ou curso que ele esteja concorrendo!!")
menu_inicial()