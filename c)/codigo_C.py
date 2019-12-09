import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random

pd.read_csv('C:/Users/Raifran/Desktop/Eduilson-Data Science/resultado-2015_2.csv')
dados = (pd.read_csv('C:/Users/Raifran/Desktop/Eduilson-Data Science/resultado-2015_2.csv'))

lista = dados.groupby(['Coluna1','Unidade','Sexo','Situacao','Nivel','RedeEnsino']).count()
lista = list(lista)

def grafico_pt(x,y):
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

     # coordenadas primeira barra
    y_axis_certas = [x]
    x_axis_certas = ['Certas']

    # coordenadas segunda barra
    y_axis_erradas = [y]
    x_axis_erradas = ['Erradas']

    # configurações da barra 
    width_n = 0.7
    bar_color_C = cor_1
    bar_color_E = cor_2
        
    # configurações da legenda
    red_patch_h = mpatches.Patch(color=cor_1, label=f'Certas')
    red_patch_m = mpatches.Patch(color=cor_2, label=f'Erradas')
    plt.legend(handles=[red_patch_h, red_patch_m])

    # construção da barra
    plt.bar(x_axis_certas, y_axis_certas, width=width_n, color=bar_color_C, label='Certas') # gráfico Certas
    plt.bar(x_axis_erradas, y_axis_erradas, width=width_n, color=bar_color_E, label='Erradas')# gráfico Erradas

    # percentual com os valores em cada barra
    plt.annotate(f'{x:.2f}%',xy=(0,(x + 0.5)), ha='center', color='black', label='Certas') # percentual Certas         
    plt.annotate(f'{y:.2f}%',xy=(1,(y + 0.5)), ha='center', color='black', label='Erradas')   # percentual Erradas         

    # outras configurações do gráfico
    plt.ylabel('(Percentual dos Acertos/Erros - %)') # rotulo do eixo y 
    plt.title("Gráfico de Tema - Português") # titulo
    plt.ylim(0,100) # intervalo fixo do eixo y
    plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) # intervalos do eixo y

    # exibição do gráfico
    plt.show()

def grafico_mat(a,b):
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

     # coordenadas primeira barra
    y_axis_certas = [a]
    x_axis_certas = ['Certas']

    # coordenadas segunda barra
    y_axis_erradas = [b]
    x_axis_erradas = ['Erradas']

    # configurações da barra 
    width_n = 0.7
    bar_color_C = cor_1
    bar_color_E = cor_2
        
    # configurações da legenda
    red_patch_h = mpatches.Patch(color=cor_1, label=f'Certas')
    red_patch_m = mpatches.Patch(color=cor_2, label=f'Erradas')
    plt.legend(handles=[red_patch_h, red_patch_m])

    # construção da barra
    plt.bar(x_axis_certas, y_axis_certas, width=width_n, color=bar_color_C, label='Certas') # gráfico Certas
    plt.bar(x_axis_erradas, y_axis_erradas, width=width_n, color=bar_color_E, label='Erradas')# gráfico Erradas

    # percentual com os valores em cada barra
    plt.annotate(f'{a:.2f}%',xy=(0,(a + 0.5)), ha='center', color='black', label='Certas') # percentual Certas         
    plt.annotate(f'{b:.2f}%',xy=(1,(b + 0.5)), ha='center', color='black', label='Erradas')   # percentual Erradas         

    # outras configurações do gráfico
    plt.ylabel('(Percentual dos Acertos/Erros - %)') # rotulo do eixo y 
    plt.title("Gráfico de Tema - Matemática") # titulo
    plt.ylim(0,100) # intervalo fixo do eixo y
    plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) # intervalos do eixo y

    # exibição do gráfico
    plt.show()
  
def portugues():

    estudo_do_texto_certas = 0
    estudo_do_texto_erradas = 0
    
    analise_linguistica_certas = 0
    analise_linguistica_erradas = 0
    
    estudo_literario_certas = 0
    estudo_literario_erradas = 0

    while True:
        try:
            filtro_2 = int(input("""
            Digite a opção que você quer ver:
            ---------------------------------------------
                [1] - Estudo do Texto
                [2] - Análise Linguística
                [3] - Estudo Literário
            ---------------------------------------------
                [0]   - Sair do Programa
            ---------------------------------------------
            """))
                    
            for i in range(0,60):  
                if filtro_2 == 1:
                    if lista[i] in('r1','r2','r3','r4','r16','r17'):
                        #estudo do texto
                        VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                        FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                        estudo_do_texto_certas += VERDADEIRO
                        estudo_do_texto_erradas += FALSO

                        estudo_do_texto_certas1 = ((estudo_do_texto_certas *100) / (estudo_do_texto_certas + estudo_do_texto_erradas)) # percentual                 
                        estudo_do_texto_erradas1 = ((estudo_do_texto_erradas *100) / (estudo_do_texto_certas + estudo_do_texto_erradas)) # percentual                 

                        grafico_pt(estudo_do_texto_certas1,estudo_do_texto_erradas1)

                        iniciar_menu()
                        break

                elif filtro_2 == 2:
                    if lista[i] in('r5','r7','r11','r12','r13', 'r14', 'r18', 'r19', 'r22', 'r23', 'r24', 'r25', 'r26', 'r27', 'r28', 'r29', 'r30'):
                        #Análise Linguística
                        VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                        FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                        analise_linguistica_certas += VERDADEIRO
                        analise_linguistica_erradas += FALSO
                        
                        analise_linguistica_certas1 = ((analise_linguistica_certas *100) / (analise_linguistica_certas + analise_linguistica_erradas)) # percentual                 
                        analise_linguistica_erradas1 = ((analise_linguistica_erradas *100) / (analise_linguistica_certas + analise_linguistica_erradas)) # percentual                 

                        
                        grafico_pt(analise_linguistica_certas1,analise_linguistica_erradas1)
                        iniciar_menu()
                        break

                elif filtro_2 == 3:
                    if lista[i] in('r8', 'r9', 'r10', 'r15', 'r20', 'r21'):
                        #Estudo Literário
                        VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                        FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                        estudo_literario_certas += VERDADEIRO
                        estudo_literario_erradas += FALSO

                        estudo_literario_certas1 = ((estudo_literario_certas *100) / (estudo_literario_certas + estudo_literario_erradas)) # percentual                 
                        estudo_literario_erradas1 = ((estudo_literario_erradas *100) / (estudo_literario_certas + estudo_literario_erradas)) # percentual                 

                        grafico_pt(estudo_literario_certas1,estudo_literario_erradas1)
                        iniciar_menu()
                        break

                elif filtro_2 == 0:
                        break
                else:
                    print('Opção inválida! Digite novamente..')
            break
        except:
            print('Opção inválida! Digite novamente..')

def matematica():
    
    matematica_financeira_certas = 0
    matematica_financeira_erradas = 0
    
    nocoes_logica_certas = 0
    nocoes_logica_erradas = 0
    
    conjuntos_certas = 0
    conjuntos_erradas = 0
    
    conjuntos_numericos_certos = 0
    conjuntos_numericos_errados = 0
    
    relacoes_funcoes_certas = 0
    relacoes_funcoes_erradas = 0
    
    gereralidade_sobre_funcoes_certas = 0
    gereralidade_sobre_funcoes_erradas = 0
    
    logaritmos_certas = 0
    logaritmos_erradas = 0
    
    funcao_quadratica_certas = 0
    funcao_quadratica_erradas = 0
    
    funcao_afim_certas = 0
    funcao_afim_erradas = 0
    
    geometria_certas = 0
    geometria_erradas = 0
    
    trigonometria_certas = 0
    trigonometria_erradas = 0
    
    teorema_tales_certas = 0
    teorema_tales_erradas = 0
    
    exponencial_certas = 0
    exponencial_erradas = 0

    while True:
        try:
            filtro_3 = int(input("""
            Digite a opção que você quer ver:
            ---------------------------------------------
                [1] - Noções de Matematica Finaceira
                [2] - Noções de Lógica
                [3] - Conjuntos
                [4] - Conjuntos Numéricos
                [5] - Relações e Funções
                [6] - Função Afim
                [7] - Função Quadratica
                [8] - Generalidades Sobre Funções
                [9] - Exponencial
                [10] - Logaritmos
                [11] - Geometria Plana
                [12] - Trigonometria
            ---------------------------------------------
                [0]   - Sair do Programa
            ---------------------------------------------
            """))
            for i in range(0,60):  
                if filtro_3 == 1:
                    if lista[i] in('r31','r32','r58','r44','r45'):
                        VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                        FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                        nocoes_logica_certas += VERDADEIRO
                        nocoes_logica_erradas+= FALSO

                        nocoes_logica_certas1 = ((nocoes_logica_certas *100) / (nocoes_logica_certas + nocoes_logica_erradas)) # percentual                 
                        nocoes_logica_erradas1 = ((nocoes_logica_erradas *100) / (nocoes_logica_certas + nocoes_logica_erradas)) # percentual                 

                        grafico_mat(nocoes_logica_certas1,nocoes_logica_erradas1)
                        iniciar_menu2()
                        break
                        
                elif filtro_3 == 2:
                    if lista[i] in('r46','r34','r47','r48'):    
                        VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                        FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                        matematica_financeira_certas += VERDADEIRO
                        matematica_financeira_erradas += FALSO

                        matematica_financeira_certas1 = ((matematica_financeira_certas *100) / (matematica_financeira_certas + matematica_financeira_erradas)) # percentual                 
                        matematica_financeira_erradas1 = ((matematica_financeira_erradas *100) / (matematica_financeira_certas + matematica_financeira_erradas)) # percentual                 

                        grafico_mat(matematica_financeira_certas1,matematica_financeira_erradas1)
                        iniciar_menu2()
                        break

                elif filtro_3 == 3:
                    if lista[i] in('r33','r53','r39'):    
                        VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                        FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                        conjuntos_certas += VERDADEIRO
                        conjuntos_erradas  += FALSO

                        conjuntos_certas1 = ((conjuntos_certas *100) / (conjuntos_certas + conjuntos_erradas)) # percentual                 
                        conjuntos_erradas1 = ((conjuntos_erradas *100) / (conjuntos_certas + conjuntos_erradas)) # percentual                 

                        grafico_mat(conjuntos_certas1,conjuntos_erradas1)
                        iniciar_menu2()
                        break
                
                elif filtro_3 == 4:
                    if lista[i] in('r49'):    
                        VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                        FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                        conjuntos_numericos_certos += VERDADEIRO
                        conjuntos_numericos_errados  += FALSO

                        conjuntos_numericos_certos1 = ((conjuntos_numericos_certos *100) / (conjuntos_numericos_certos + conjuntos_numericos_errados)) # percentual                 
                        conjuntos_numericos_errados1 = ((conjuntos_numericos_errados *100) / (conjuntos_numericos_certos + conjuntos_numericos_errados)) # percentual                 

                        grafico_mat(conjuntos_numericos_certos1,conjuntos_numericos_errados1)
                        iniciar_menu2()
                        break

                elif filtro_3 == 5:
                    nenhum = True
                    break
                    
                elif filtro_3 == 6:
                    if lista[i] in('r50','r51','r52'):    
                        VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                        FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                        funcao_afim_certas += VERDADEIRO
                        funcao_afim_erradas  += FALSO

                        funcao_afim_certas1 = ((funcao_afim_certas *100) / (funcao_afim_certas + funcao_afim_erradas)) # percentual                 
                        funcao_afim_erradas1 = ((funcao_afim_erradas *100) / (funcao_afim_certas + funcao_afim_erradas)) # percentual                 

                        grafico_mat(funcao_afim_certas1,funcao_afim_erradas1)
                        iniciar_menu2()
                        break
                        
                elif filtro_3 == 7:
                    if lista[i] in('r35','r36'):    
                        VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                        FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                        funcao_quadratica_certas += VERDADEIRO
                        funcao_quadratica_erradas += FALSO

                        funcao_quadratica_certas1 = ((funcao_quadratica_certas *100) / (funcao_quadratica_certas + funcao_quadratica_erradas)) # percentual                 
                        funcao_quadratica_erradas1 = ((funcao_quadratica_erradas *100) / (funcao_quadratica_certas + funcao_quadratica_erradas)) # percentual                 

                        grafico_mat(funcao_quadratica_certas1,funcao_quadratica_erradas1)
                        iniciar_menu2()
                        break
                        
                elif filtro_3 == 8:
                    nenhum = True
                    break
                
                elif filtro_3 == 9:
                    if lista[i] in('r35','r36'):    
                        VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                        FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                        exponencial_certas  += VERDADEIRO
                        exponencial_erradas += FALSO

                        exponencial_certas1 = ((exponencial_certas *100) / (exponencial_certas + exponencial_erradas)) # percentual                 
                        exponencial_erradas1 = ((exponencial_erradas *100) / (exponencial_certas + exponencial_erradas)) # percentual                 

                        grafico_mat(exponencial_certas1,exponencial_erradas1)
                        iniciar_menu2()
                        break
                
                elif filtro_3 == 10:
                    if lista[i] in('r56','r57'):    
                        VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                        FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                        logaritmos_certas  += VERDADEIRO
                        logaritmos_erradas += FALSO

                        logaritmos_certas1 = ((logaritmos_certas *100) / (logaritmos_certas + logaritmos_erradas)) # percentual                 
                        logaritmos_erradas1 = ((logaritmos_erradas *100) / (logaritmos_certas + logaritmos_erradas)) # percentual                 

                        grafico_mat(logaritmos_certas1,logaritmos_erradas1)
                        iniciar_menu2()
                        break
                
                elif filtro_3 == 11:
                    if lista[i] in('r42','r43'):    
                        VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                        FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                        geometria_certas += VERDADEIRO
                        geometria_erradas += FALSO

                        geometria_certas1 = ((geometria_certas *100) / (geometria_certas + geometria_erradas)) # percentual                 
                        geometria_erradas1 = ((geometria_erradas *100) / (geometria_certas + geometria_erradas)) # percentual                 

                        grafico_mat(geometria_certas1,geometria_erradas1)
                        iniciar_menu2()
                        break

                elif filtro_3 == 12:
                    if lista[i] in('r59','r60'):    
                        VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                        FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                        trigonometria_certas += VERDADEIRO
                        trigonometria_erradas += FALSO

                        trigonometria_certas1 = ((trigonometria_certas *100) / (trigonometria_certas + trigonometria_erradas)) # percentual                 
                        trigonometria_erradas1 = ((trigonometria_erradas *100) / (trigonometria_certas + trigonometria_erradas)) # percentual                 

                        grafico_mat(trigonometria_certas1,trigonometria_erradas1)
                        iniciar_menu2()
                        break

                elif filtro_3 == 0:
                    break

                else:
                    print('Opção inválida! Digite novamente..')

            break

            if nenhum:
                print("Não há questões")  
        except:
            print('Opção inválida! Digite novamente..')
        
def menu_inicial():
    while True:
        try:
            opcao = int(input("""
            ---------------------------------------------
            Escolha uma opção para iniciar sua análise:
            ---------------------------------------------
                [1]  - Escolher a Matéria - Português
                [2]  - Escolher a Matéria - Matemática
            ---------------------------------------------
                [0]  - Sair
            ---------------------------------------------
        Opção: """))

            if opcao == 0:
                break

            elif opcao == 1:
                portugues()
                break

            elif opcao == 2:
                matematica()
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
                [2]  - Escolher um novo Tema 
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
                portugues()
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
                [2]  - Escolher um novo Tema 
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
                matematica()
                break

            else:
                print("A opção digitada está inválida, Digite novamente!")

        except:
            print("A opção digitada está inválida, Digite novamente!")

print("\n\n\t\t\t\tBem vindo ao programa!!\n\n\tNesse Script você vai poder gerar gráficos sobre os Temas\ndas questões que fazem parte das Matérias de Português e Matemática!!")
menu_inicial()