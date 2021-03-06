# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 13:53:22 2021

@author: Marco Antônio
"""

import math

class Diretorio:
    def __init__(self, profundidadeGlobal):
        self.profundidadeGlobal = profundidadeGlobal
        self.quantidadeDeDiretoriosIniciais = int(math.pow(2, profundidadeGlobal))
        self.EnderecoDebuckets = []
        
        for i in range(self.quantidadeDeDiretoriosIniciais):
            self.EnderecoDebuckets.append(i)
        print(self.EnderecoDebuckets)
    
    def funcaoHash(self, chave) -> int:
        return int(chave) % int (math.pow(2, self.profundidadeGlobal))
    
    def retornaEndereco(self, chave) -> int:
        return self.EnderecoDebuckets[self.funcaoHash(chave)]
    
    def duplicarDiretorio(self):
        self.profundidadeGlobal += 1
        for i in range (int (math.pow(2, self.profundidadeGlobal)/2)):
            self.EnderecoDebuckets.append(self.EnderecoDebuckets[i])
        print("novo tamanho do diretorio",len(self.EnderecoDebuckets))
    
    def realocarEnderecos(self, endIni, novoEnd):
        troquei = True
        for i in range (len(self.EnderecoDebuckets)):
            if(self.EnderecoDebuckets[i] == endIni):
                if(not troquei):
                    self.EnderecoDebuckets[i] = novoEnd
                    troquei = True
                else:
                    troquei = False
    
            
    
            
            
            
            
            
            
            
            
            
            
            