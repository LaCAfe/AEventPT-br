#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 02:47:59 2018

@author: alexandre
"""
#Importes
import pandas as pd
import numpy as np
import os
import csv

#Para identificar o diretório atual (pwd):
    #os.getcwd() # cwd = current working directory

#Para listar o conteúdo (ls):    
    #os.listdir() #retorna um objeto do tipo list (lista), claro!    

#Mudar de diretório (cd):
    path = '/HD/DADOS/000 - Área de trabalho/1 - Mestrado/0 - CEFET (Em Curso)/0 - Dissertação/stanford-corenlp-full-2018-02-27/pt-model'    
    os.chdir(path)
    
# Nome do arquivo
arquivo1 = 'pt-br-universal-train3.conll'

# Carrega o arquivo
base = pd.read_csv(arquivo1,delimiter ='/t')#Lê arquivos separados por vírgula

ficheiro = open(arquivo1, 'rb')
arquivo2 = csv.reader(ficheiro, dialect=csv.excel_tab)

#Formato do dataframe (linhas e colunas)
base.shape
arquivo2.shape

#Criar DataSet  com doenças

doencas = pd.DataFrame(base['DESCRICAO'])

print(doencas)

doencas['Entidade'] = 'Doença'
 
 


