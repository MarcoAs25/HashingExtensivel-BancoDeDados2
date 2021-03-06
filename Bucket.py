# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 13:21:37 2021

@author: Marco Antônio
"""
from __future__ import annotations

class Bucket:
    def __init__(self, tamanhodoBalde, profundidadeLocal):
        self.tamanhodoBalde = tamanhodoBalde
        self.profundidadeLocal = profundidadeLocal
        self.valores = []#valores
        
    def get_size(self) -> int:
        return len(self.valores)

    def is_empty(self) -> bool:
        return len(self.valores) == 0

    def is_full(self) -> bool:
        return len(self.valores) == self.tamanhodoBalde-1


    def get_profLocal(self) -> int:
        return self.profundidadeLocal
    
    def set_profLocal(self, profLocal):
        self.profundidadeLocal = profLocal
    
    def set_valores(self, valores):
        self.valores = valores