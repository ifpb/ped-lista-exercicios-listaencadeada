from listaencadeada import ListaEncadeada, No

class ListaEncadeadaEstendida(ListaEncadeada):
    def pares(self):
        pares = ListaEncadeada()
        atual = self.cabeca
        while atual is not None:
            if atual.carga % 2 == 0: 
                pares.inserir_no_final(atual.carga)
            atual = atual.prox
        return pares

    def impares(self):
        impares = ListaEncadeada()
        atual = self.cabeca
        while atual is not None:
            if atual.carga % 2 != 0: 
                impares.inserir_no_final(atual.carga)
            atual = atual.prox
        return impares

    def buscar_pos(self, valor):
        c = 0
        pos = -1
        atual: 'No' = self.cabeca
        while atual is not None:
            if atual.carga == valor:
                if atual.prox is not None:
                    self.cauda = atual
                pos = c
            atual = atual.prox
            c += 1
        return pos

    def inserir_pos(self, pos, valor):
        if pos == 0 or self.cabeca is None or self.cabeca == self.cauda:
            self.inserir_no_inicio(valor)
            return

        c = 0
        atual = self.cabeca
        while atual.prox is not None and c < pos - 1:
            atual = atual.prox
            c += 1
        
        novo = No(valor)
        novo.prox = atual.prox
        atual.prox = novo


    def remover_de_posicao(self, pos):
        if pos == 0 or self.cabeca is None or self.cabeca == self.cauda:
            self.remover_do_inicio()
            return
        
        c = 0
        atual = self.cabeca
        while atual.prox is not None and c < pos - 1:
            atual = atual.prox
            c += 1

        if atual.prox is not None:
            atual.prox = atual.prox.prox

    def remover_ocorrencias(self, valor):
        while self.__remover_por_valor(valor) == True: 
            pass

    def __remover_por_valor(self, valor):
        if self.cabeca is not None and self.cabeca.carga == valor:
            self.remover_do_inicio()
            return True
        atual: 'No' = self.cabeca
        while atual.prox is not None:
            if atual.prox.carga == valor:
                atual.prox = atual.prox
                if atual.prox is not None:
                    atual.prox = atual.prox.prox
                    self.cauda = atual
                    return True
            atual = atual.prox
        return False