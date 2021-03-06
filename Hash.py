# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 14:30:30 2021

@author: Marco Antônio
"""
from Diretorio import Diretorio
from Bucket import Bucket

class Hash:
    def __init__(self, profundidadeGlobal, tamanhoDoBucket):
        self.tamanhoDoBucket = tamanhoDoBucket
        self.diretorio = Diretorio(profundidadeGlobal)
        self.buckets = []
        for i in range(self.diretorio.quantidadeDeDiretoriosIniciais):
            bucketAux = Bucket(self.tamanhoDoBucket, profundidadeGlobal)
            self.buckets.append(bucketAux)
            
    def inserir(self, chave, mostrar):
        index = self.diretorio.retornaEndereco(chave)
        cabe = self.buckets[index].get_size() < self.tamanhoDoBucket   
        if(cabe):
            if chave not in self.buckets[index].valores:
                self.buckets[index].valores.append(chave)
                if(mostrar):
                    print("Valor inserido")
            else:
                if(mostrar):
                    print("valor já inserido")
        else:
            profundidadesdiferentes = self.buckets[index].profundidadeLocal != self.diretorio.profundidadeGlobal
            if(not profundidadesdiferentes):
                valores = []
                self.diretorio.duplicarDiretorio()
                self.buckets[index].profundidadeLocal += 1
                aux = Bucket(self.tamanhoDoBucket, self.buckets[index].profundidadeLocal)
                self.buckets.append(aux)
                self.diretorio.realocarEnderecos(index, len(self.buckets) - 1)
                for i in range (len(self.buckets[index].valores)):
                    valores.append(self.buckets[index].valores[i])
                self.buckets[index].valores.clear()
                for valor in valores:
                    self.inserir(valor)
                valores.clear()
                self.inserir(chave)
            else:
                valores = []
                self.buckets[index].profundidadeLocal += 1
                aux = Bucket(self.tamanhoDoBucket, self.buckets[index].profundidadeLocal)
                self.buckets.append(aux)
                self.diretorio.realocarEnderecos(index, len(self.buckets) - 1)
                for i in range (len(self.buckets[index].valores)):
                    valores.append(self.buckets[index].valores[i])
                self.buckets[index].valores.clear()
                for valor in valores:
                    self.inserir(valor)
                valores.clear()
                self.inserir(chave)
            
            
    def mostrar(self):
        for buckets in self.buckets:
            print(buckets.valores,"\n\n")
            
            
            
    def buscar(self, chave):
        index = self.diretorio.retornaEndereco(chave)
        if(chave in self.buckets[index].valores):
            print("Valor encontrado!")
        else:
            print("Valor não econtrado")
        
    def remover(self, chave,mostrar):
        try:
            index = self.diretorio.retornaEndereco(chave)
            self.buckets[index].valores.remove(chave)
            if(mostrar):
                print("Valor removido")
        except:
            if(mostrar):
                print("Não foi possivel remover o item informado")
        
        
        
        
        
        
        
        
        