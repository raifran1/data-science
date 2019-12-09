import pandas as pd # manipulação de dados
import numpy as np # so importa - pode ser que venha a ser usado
import matplotlib.pyplot as plt # biblioteca de geração de graficos


#ler o arquivo e coloca numa variavel
dados = (pd.read_csv('C:/Users/Raifran/Downloads/MakerDay_2019.csv'))


email_da_galera = (dados[dados.Tipo_de_ingresso == 'Expositor - Projetos IA'])
#print(dados.Email.unique())


email = (dados.Email.unique())
print(email) 



'''
# FILTRO GERAL
Informatica_Tarde = (dados[dados.Coluna1 == "INFORMÁTICA / TARDE"]) # exemplo de filtro por curso
Teresina_Central = (dados[dados.Unidade == "TERESINA - CENTRAL"]) # exemplo de filtro por campus
Feminino = (dados[dados.Sexo == "Feminino"]) # exemplo de filtro por Sexo Feminino
Masculino = (dados[dados.Sexo == "Masculino"]) # exemplo de filtro por Sexo Masculino

# FILTRO ESPECÍFICO
    # 1º de filtar por campus - EXEMPLO
Teresina_Central = (dados[dados.Unidade == "TERESINA - CENTRAL"]) 
    # 2º de filtar novamente dentro da instancia acima - EXEMPLO
TC_CONTABILIDADE = (Teresina_Central[Teresina_Central.Coluna1 == "CONTABILIDADE"]) 
TC_ADM = (Teresina_Central[Teresina_Central.r1 == "VERDADEIRO"]) 
 
cursos = dados.Coluna1.value_counts()

print(f
{cursos}
'')




 Pode filtrar varias instancias dentro de outras
 basta chamar a ultima instancia dentro da proxima
'''