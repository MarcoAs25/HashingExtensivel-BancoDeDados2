# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 15:30:01 2021

@author: Marco Antônio
"""

from Hash import Hash as hashextensivel
import time

if __name__ == '__main__':
    h = hashextensivel(0,100)
    
    
    arq = open('output.csv','r')
    entrada = list()
    print("Inserindo os valores de output.csv")
    inicio = time.time()
    for linha in arq:
        valores = linha.split(',')
        if(valores[0] == '+'):
            entrada = list(map(int, valores[1:]))
            #print(entrada)#caso queira visualizar as entradas
            for i in entrada:
                h.inserir(i,False)
        elif(valores[0] == '-'):
            chave = int(valores[1])
            h.remover(chave,False)
    fim = time.time()
    h.mostrar()
    print("Tempo de execução: ",fim - inicio," ms")
    while(True):
        print("\n1 - Remover valor no Hash")
        print("2 - Inserir valor no Hash")
        print("3 - Buscar valor no Hash")
        print("0 - sair")
        n = int(input("Digite uma opção: "))
        if n == 1:
            numero = int(input("Digite o valor para ser removido: "))
            inicio = time.time()
            h.remover(numero,True)
            fim = time.time()
            print("Tempo de execução: ",fim - inicio," ms")
        elif n== 2:
            
            numero = int(input("Digite o valor para ser inserido: "))
            inicio = time.time()
            h.inserir(numero,True)
            fim = time.time()
            print("Tempo de execução: ",fim - inicio," ms")
        elif n == 3:
            
            numero = int(input("Digite o valor para ser buscado: "))
            inicio = time.time()
            h.buscar(numero)
            fim = time.time()
            print("Tempo de execução: ",fim - inicio," ms")
        else:
            break;