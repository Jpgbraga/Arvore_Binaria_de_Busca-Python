import os


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  
        self.right = None 


class ArvoreBinariaBusca:
    def __init__(self):
        self.root = None 

    
    def inserir(self, data):
        if self.root is None:
            self.root = Node(data)
            print(f"=> Raiz [{data}] criada com sucesso.")
        else:
            self._inserir_recursivo(data, self.root)

    def _inserir_recursivo(self, data, node):
        if data < node.data:
            
            if node.left is None:
                node.left = Node(data)
                print(f"=> [{data}] inserido à esquerda de [{node.data}].")
            else:
                self._inserir_recursivo(data, node.left)
        elif data > node.data:
            
            if node.right is None:
                node.right = Node(data)
                print(f"=> [{data}] inserido à direita de [{node.data}].")
            else:
                self._inserir_recursivo(data, node.right)
        else:
            
            print(f"=> O valor [{data}] já existe na árvore e não foi inserido.")

    
    def buscar(self, data):
        encontrado = self._buscar_recursivo(data, self.root)
        if encontrado:
            print(f"=> Valor [{data}] ENCONTRADO na árvore.")
        else:
            print(f"=> Valor [{data}] NÃO ENCONTRADO na árvore.")

    def _buscar_recursivo(self, data, node):
        
        if node is None:
            return False
        
        if node.data == data:
            return True
            
        
        if data < node.data:
            return self._buscar_recursivo(data, node.left)
        else:
            return self._buscar_recursivo(data, node.right)

    
    def imprimir(self):
        if self.root is None:
            print("=> A árvore está vazia.")
        else:
            print("=> Elementos em Ordem (Crescente): ", end="")
            self._imprimir_em_ordem(self.root)
            print() 

    
    def _imprimir_em_ordem(self, node):
        if node is not None:
            self._imprimir_em_ordem(node.left)
            print(f"[{node.data}] ", end="")
            self._imprimir_em_ordem(node.right)



def main():
    arvore = ArvoreBinariaBusca()
    
    while True:
        print("\n===============================")
        print("    ÁRVORE BINÁRIA DE BUSCA    ")
        print("===============================")
        print("1- Inserir elemento")
        print("2- Imprimir árvore (Em-Ordem)")
        print("3- Buscar elemento")
        print("0- Sair")
        print("===============================")
        
        opcao = input("Escolha a opcao: ")
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if opcao == '1':
            try:
                valor = int(input("Digite um número inteiro para inserir: "))
                arvore.inserir(valor)
            except ValueError:
                print("=> Por favor, digite apenas números inteiros válidos.")
                
        elif opcao == '2':
            arvore.imprimir()
            
        elif opcao == '3':
            try:
                valor = int(input("Digite o número que deseja buscar: "))
                arvore.buscar(valor)
            except ValueError:
                print("=> Por favor, digite apenas números inteiros válidos.")
                
        elif opcao == '0':
            print("=> Encerrando o programa...")
            break
            
        else:
            print("=> Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()