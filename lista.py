from node import Node


class Lista:
    inicio = None

    def __init__(self):
        self.inicio = None

    def adicionar(self, valor,inicio = False):
        if (inicio):
            self.adicionar_no_inicio =(valor)
         else:
            self.adicionar_no_fim(valor)
            
     def adicionar_no_inicio(self, valor):
        valor = Node(valor)
        valor.proximo = self.inicio
        self.inicio = valor
       
        else:
            aux = self.inicio
            while (aux.proximo != None):
                aux = aux.proximo

            aux.proximo = Node(valor, None)

    def show(self):
        aux = self.inicio
        print("[", end='')

        while (aux != None):
            print(f"{aux.valor}, ", end='')
            aux = aux.proximo

        print("]")

    def remover_um(self, valor):
        aux = self.inicio    

        if aux == None:         
          return

        if aux != None:
          if aux.valor == valor:
            self.inicio = self.proximo
            self = None
                    

        while aux != None:         
          if aux.valor == valor:           
            break
          prev = aux
          aux = aux.proximo

        prev.proximo = aux.proximo
        aux = None

    def remover_todos(self,valor):
        aux = self.inicio

        while aux != None:
          self.remover_um(valor)
          aux = aux.proximo
