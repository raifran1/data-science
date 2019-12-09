import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.read_csv('C:/Users/Raifran/Desktop/Eduilson-Data Science/resultado-2015_2.csv')
dados = (pd.read_csv('C:/Users/Raifran/Desktop/Eduilson-Data Science/resultado-2015_2.csv'))

lista = dados.groupby(['Coluna1','Unidade','Sexo','Situacao','Nivel','RedeEnsino']).count()
lista = list(lista)

while True:
    filtro_1 = int(input("""
     Digite a opção que você quer ver:
         [1] - Português
         [2] - Matemática
         [3] - Sair
    """))
        
    estudo_do_texto_certas = 0
    estudo_do_texto_erradas = 0
    
    analise_linguistica_certas = 0
    analise_linguistica_erradas = 0
    
    estudo_literario_certas = 0
    estudo_literario_erradas = 0
    
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
    
    
    if filtro_1 == 1: #PORTUGUÊS
        filtro_2 = int(input("""
    Digite a opção que você quer ver:
         [1] - Estudo do Texto
         [2] - Análise Linguística
         [3] - Estudo Literário
    """))
            
        for i in range(0,60):  
            if filtro_2 == 1:
                if lista[i] in('r1','r2','r3','r4','r16','r17'):
                    #estudo do texto
                    VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                    FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                    estudo_do_texto_certas += VERDADEIRO
                    estudo_do_texto_erradas += FALSO
            elif filtro_2 == 2:
                if lista[i] in('r5','r7','r11','r12','r13', 'r14', 'r18', 'r19', 'r22', 'r23', 'r24', 'r25', 'r26', 'r27', 'r28', 'r29', 'r30'):
                    #Análise Linguística
                    VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                    FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                    analise_linguistica_certas += VERDADEIRO
                    analise_linguistica_erradas += FALSO
            elif filtro_2 == 3:
                if lista[i] in('r8', 'r9', 'r10', 'r15', 'r20', 'r21'):
                    #Estudo Literário
                    VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                    FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                    estudo_literario_certas += VERDADEIRO
                    estudo_literario_erradas += FALSO
    
                    
    #print(estudo_do_texto_certas)
    #print(estudo_do_texto_erradas)
    #print(analise_linguistica_certas)
    #print(analise_linguistica_erradas)
                    
        if estudo_do_texto_certas > 0 or estudo_do_texto_erradas > 0:
                    
            y_axis = [estudo_do_texto_certas,estudo_do_texto_erradas]
            x_axis = ['CERTAS','ERRADAS']
            width_n = 0.8
            bar_color = 'red'
                
            plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
            plt.show()
        
        elif analise_linguistica_certas > 0 or analise_linguistica_erradas > 0:
                     
            y_axis = [analise_linguistica_certas,analise_linguistica_erradas]
            x_axis = ['CERTAS','ERRADAS']
            width_n = 0.8
            bar_color = 'red'
                
            plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
            plt.show()
            
        elif estudo_literario_certas > 0 or estudo_literario_erradas > 0:
                     
            y_axis = [estudo_literario_certas,estudo_literario_erradas]
            x_axis = ['CERTAS','ERRADAS']
            width_n = 0.8
            bar_color = 'red'
                
            plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
            plt.show()
    
    elif filtro_1 == 2:
        filtro_3 = int(input("""
        Digite a opção que você quer ver:
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
    """))
        for i in range(0,60):  
            if filtro_3 == 1:
                if lista[i] in('r31','r32','r58','r44','r45'):
                    
                    VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                    FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                    nocoes_logica_certas += VERDADEIRO
                    nocoes_logica_erradas+= FALSO
                    
            elif filtro_3 == 2:
                if lista[i] in('r46','r34','r47','r48'):    
                    VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                    FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                    matematica_financeira_certas += VERDADEIRO
                    matematica_financeira_erradas += FALSO
    
            elif filtro_3 == 3:
                if lista[i] in('r33','r53','r39'):    
                    VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                    FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                    conjuntos_certas += VERDADEIRO
                    conjuntos_erradas  += FALSO
            
            elif filtro_3 == 4:
                if lista[i] in('r49'):    
                    VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                    FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                    conjuntos_numericos_certos += VERDADEIRO
                    conjuntos_numericos_errados  += FALSO
    
            elif filtro_3 == 5:
                nenhum = True
                break
                
            elif filtro_3 == 6:
                if lista[i] in('r50','r51','r52'):    
                    VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                    FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                    funcao_afim_certas += VERDADEIRO
                    funcao_afim_erradas  += FALSO
                    
            elif filtro_3 == 7:
                if lista[i] in('r35','r36'):    
                    VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                    FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                    funcao_quadratica_certas += VERDADEIRO
                    funcao_quadratica_erradas += FALSO
                    
            elif filtro_3 == 8:
                nenhum = True
                break
            
            elif filtro_3 == 9:
                if lista[i] in('r35','r36'):    
                    VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                    FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                    exponencial_certas  += VERDADEIRO
                    exponencial_erradas += FALSO
            
            elif filtro_3 == 10:
                if lista[i] in('r56','r57'):    
                    VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                    FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                    logaritmos_certas  += VERDADEIRO
                    logaritmos_erradas += FALSO
            
            elif filtro_3 == 11:
                if lista[i] in('r42','r43'):    
                    VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                    FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                    geometria_certas += VERDADEIRO
                    geometria_erradas += FALSO
            elif filtro_3 == 11:
                if lista[i] in('r59','r60'):    
                    VERDADEIRO = len(dados.groupby([lista[i]]).groups['VERDADEIRO'])
                    FALSO = len(dados.groupby([lista[i]]).groups['FALSO'])
                    trigonometria_certas += VERDADEIRO
                    trigonometria_erradas += FALSO
        
        if nenhum:
            print("Não há questões")
            
        if matematica_financeira_certas  > 0 or matematica_financeira_certas > 0:
                        
            y_axis = [matematica_financeira_certas,matematica_financeira_erradas]
            x_axis = ['CERTAS','ERRADAS']
            width_n = 0.8
            bar_color = 'red'
            
            plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
            plt.show()
            
        elif nocoes_logica_certas > 0 or nocoes_logica_erradas > 0:
                        
            y_axis = [nocoes_logica_certas,nocoes_logica_erradas]
            x_axis = ['CERTAS','ERRADAS']
            width_n = 0.8
            bar_color = 'red'
            
            plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
            plt.show()
            
        elif conjuntos_certas > 0 or conjuntos_erradas > 0:
                        
            y_axis = [conjuntos_certas ,conjuntos_erradas ]
            x_axis = ['CERTAS','ERRADAS']
            width_n = 0.8
            bar_color = 'red'
            
            plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
            plt.show()
            
        elif conjuntos_numericos_certos > 0 or conjuntos_numericos_errados> 0:
                        
            y_axis = [conjuntos_numericos_certos ,conjuntos_numericos_errados]
            x_axis = ['CERTAS','ERRADAS']
            width_n = 0.8
            bar_color = 'red'
            
            plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
            plt.show()
        
        elif funcao_afim_certas > 0 or funcao_afim_erradas> 0:
                        
            y_axis = [funcao_afim_certas ,funcao_afim_erradas]
            x_axis = ['CERTAS','ERRADAS']
            width_n = 0.8
            bar_color = 'red'
            
            plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
            plt.show()
        
        elif funcao_quadratica_certas > 0 or funcao_quadratica_erradas> 0:
                        
            y_axis = [funcao_quadratica_certas ,funcao_quadratica_erradas]
            x_axis = ['CERTAS','ERRADAS']
            width_n = 0.8
            bar_color = 'red'
            
            plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
            plt.show()
        
        elif exponencial_certas > 0 or exponencial_erradas> 0:
                        
            y_axis = [exponencial_certas ,exponencial_erradas]
            x_axis = ['CERTAS','ERRADAS']
            width_n = 0.8
            bar_color = 'red'
            
            plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
            plt.show()
       
        elif logaritmos_certas > 0 or logaritmos_erradas> 0:
                        
            y_axis = [logaritmos_certas ,logaritmos_erradas]
            x_axis = ['CERTAS','ERRADAS']
            width_n = 0.8
            bar_color = 'red'
            
            plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
            plt.show()
       
        elif geometria_certas > 0 or geometria_erradas> 0:
                        
            y_axis = [geometria_certas ,geometria_erradas]
            x_axis = ['CERTAS','ERRADAS']
            width_n = 0.8
            bar_color = 'red'
            
            plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
            plt.show()
    
        elif trigonometria_certas > 0 or trigonometria_erradas> 0:
                        
            y_axis = [trigonometria_certas ,trigonometria_erradas]
            x_axis = ['CERTAS','ERRADAS']
            width_n = 0.8
            bar_color = 'red'
            
            plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
            plt.show()
    elif filtro_1 == 3:
        break