# se importa AVLBinaryTreeNode  del modulo AVLBinaryTreeNode
from AVLBinaryTreeNode import AVLBinaryTreeNode

# clase AVLTree


class AVLTree:
    # constructor
    def __init__(self):
        self.root = None

    # metodo para insertar nodos
    def insertNode(self, target):
        # si el arbol esta vacio, se inserta el nodo como raiz
        if self.root is None:
            self.root = AVLBinaryTreeNode(target)
        # sino, se hace uso de la funcion insertNode de la clase AVLBinaryTreeNode para insertar el nodo en el lugar correcto
        else:
            self.root.insertNode(target)
            # se hace uso de la funcion balancear para balancear el arbol
            self.root = self.root.balance()

    # metodo para eliminar nodos
    def deleteNode(self, target):
        # si el arbol esta vacio, no se elimina nada
        if self.root is None:
            return
        # si solo hay un nodo(raiz), se elimina el nodo
        elif self.root.data == target and self.root.left is None and self.root.right is None:
            self.root = None
        # si el nodo a eliminar es la raiz y el árbol solo consta de la raiz y un hijo izquierdo, la raiz pasa a a ser el hijo izquierdo
        elif self.root.data == target and self.root.right is None:
            self.root = self.root.left
        # si el nodo a eliminar es la raiz y árbol solo consta de la raiz y un hijo derecho, la raiz pasa a a ser el hijo derecho
        elif self.root.data == target and self.root.left is None:
            self.root = self.root.right
        # si el nodo a eliminar no es la raiz, se hace uso de la funcion deleteNode de la clase AVLBinaryTreeNode para eliminar el nodo
        else:
            self.root.deleteNode(target)

    # metodo para encontrar un nodo
    def find(self, target):
        # si el arbol esta vacio, no se encuentra nada
        if self.root is None:
            return None
        # si el arbol no esta vacio, se hace uso de la funcion find de la clase AVLBinaryTreeNode para encontrar el nodo
        else:
            if self.root.findNode(target):
                print(self.root.findNode(target).data)
            return self.root.findNode(target)

    # metodo para encontrar el tio de un nodo
    def findUncle(self, target):
        # si el arbol esta vacio, no se encuentra nada
        if self.root is None:
            return None
        # si el arbol no esta vacio, se hace uso de la funcion findUncle de la clase AVLBinaryTreeNode para encontrar el tio de un nodo
        else:
            if self.root.findUncle(target):
                print(self.root.findUncle(target).data) # imprimir el tio
            return self.root.findUncle(target)

    # metodo para encontrar el abuelo de un nodo
    def findGrandparent(self, target):
        # si el arbol esta vacio, no se encuentra nada
        if self.root is None:
            return None
        # si el arbol no esta vacio, se hace uso de la funcion findGrandparent de la clase AVLBinaryTreeNode para encontrar el abuelo de un nodo
        else:
            if self.root.findGrandparent(target):
                print(self.root.findGrandparent(target).data) # imprimir el abuelo
            return self.root.findGrandparent(target)

    # metodo para calcular la altura del arbol
    def height(self, target=None):
        if self.root is None:
            print("Tree is empty")
        elif target is None:
            print(self.root.height())
        elif self.root.findNode(target) is not None:
            print(self.root.findNode(target).height())
        else:
            print('None')


    # metodo para imprimir el arbol por niveles
    def levelOrder(self):
        # si el arbol esta vacio, no se imprime nada
        if self.root is None:
            return None
        # si el arbol no esta vacio, se hace uso de la funcion levelOrder de la clase AVLBinaryTreeNode para imprimir el arbol por niveles
        else:
            self.root.levelOrder()
