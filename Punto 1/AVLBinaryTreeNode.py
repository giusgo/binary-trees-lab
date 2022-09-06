# Clase Nodo
class AVLBinaryTreeNode:
    # Constructor, con data como valor
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Función para insertar un nodo
    def insertNode(self, target):
        # Si el valor del nodo ya se encuentra en el árbol, no se inserta
        if self.data == target:
            return
        # Si el dato a insertar es menor que la raiz, debe ser insertado en el subarbol izquierdo
        if self.data > target:
            if self.left is not None:
                # Si el nodo izquierdo no es None, se llama recursivamente a la función insertNode para insertar el nodo en el subarbol izquierdo
                self.left.insertNode(target)
                # Una vez insertado el nodo, se balancea el subarbol izquierdo
                self.left = self.left.balance()
            else:
                # Si el nodo izquierdo es None, se inserta el nodo en esa posición
                self.left = AVLBinaryTreeNode(target)
        # Si el dato a insertar es mayor que la raiz, debe ser insertado en el subarbol derecho
        else:
            # de forma recursiva, mientras que el lado derecho no sea nulo, se encuentra el espacio indicado para insertar el dato
            if self.right is not None:
                self.right.insertNode(target)
                # una vez insertado, se procede a balancear el subarbol derecho
                self.right = self.right.balance()
            else:
                # Si el nodo derecho es None, se inserta el nodo en esa posición
                self.right = AVLBinaryTreeNode(target)

    # Función para eliminar un nodo
    def deleteNode(self, target):
        # Si se encuentra el nodo a eliminar
        if self.data == target:
            # Si el nodo a eliminar es una hoja, se hace None
            if self.left is None and self.right is None:
                return None
            # Si el subarbol izquierdo es None, se retorna el subarbol derecho
            if self.left is None:
                return self.right
            # Si el subarbol derecho es None, se retorna el subarbol izquierdo
            if self.right is None:
                return self.left
            # Si el nodo a eliminar tiene dos hijos
            if self.left is not None and self.right is not None:
                # Se busca el nodo con el valor mas grande en el subarbol izquierdo
                maxNode = self.left
                while maxNode.right is not None:
                    maxNode = maxNode.right
                # Se reemplaza el valor del nodo a eliminar por el valor del nodo con el valor mas grande en el subarbol izquierdo
                self.data = maxNode.data
                # Se elimina el nodo con el valor mas grande en el subarbol izquierdo
                self.left = self.left.deleteNode(maxNode.data)
        # Si el dato del nodo a eliminar es menor que el dato del nodo actual, se busca en el subarbol izquierdo
        if self.left is not None and target < self.data:
            # Se balancea el subarbol izquierdo
            self.left = self.left.deleteNode(target)
        # Si el dato del nodo a eliminar es mayor que el dato del nodo actual, se busca en el subarbol derecho
        if self.right is not None and target > self.data:
            # Se balancea el subarbol derecho
            self.right = self.right.deleteNode(target)
        # Se retorna el nodo actual balanceado
        self = self.balance()
        return self

    # Función para calcular la altura de un nodo
    def height(self):
        # Si el nodo tiene dos hijos, se retorna la mayor altura entre el subarbol izquierdo y el subarbol derecho mas 1
        if self.left is not None and self.right is not None:
            return 1 + max(self.left.height(), self.right.height())
        # Si el nodo solo tiene hijo izquierdo, se retorna la altura del subarbol izquierdo mas 1
        if self.left is not None:
            return 1 + self.left.height()
        # Si el nodo solo tiene hijo derecho, se retorna la altura del subarbol derecho mas 1
        if self.right is not None:
            return 1 + self.right.height()
        # Si el nodo es una hoja, se retorna 0
        else:
            return 0

    # Función para calcular el factor de balance de un nodo
    def balanceFactor(self):
        # Si el nodo tiene dos hijos, se retorna la altura del subarbol izquierdo menos la altura del subarbol derecho
        if self.left is not None and self.right is not None:
            return self.left.height() - self.right.height()
        # Si el nodo solo tiene hijo izquierdo, se retorna la altura del subarbol izquierdo mas 1
        if self.left is not None:
            return 1 + self.left.height()
        # Si el nodo solo tiene hijo derecho, se retorna la altura del subarbol derecho menos 1
        if self.right is not None:
            return -1 - self.right.height()
        # Si el nodo es una hoja, se retorna 0
        else:
            return 0

    # Función para rotar un subarbol a la izquierda
    def rotateLeft(self):
        # Se guarda el nodo derecho en una variable temporal
        temp = self.right
        # Se asigna el subarbol izquierdo del nodo derecho al subarbol derecho del nodo actual
        self.right = temp.left
        # Se asigna el nodo actual como subarbol izquierdo del nodo derecho
        temp.left = self
        # Se retorna el nodo derecho
        return temp

    # Funcion para rotar un subarbol a la derecha
    def rotateRight(self):
        # Se guarda el nodo izquierdo en una variable temporal
        temp = self.left
        # Se asigna el subarbol derecho del nodo izquierdo al subarbol izquierdo del nodo actual
        self.left = temp.right
        # Se asigna el nodo actual como subarbol derecho del nodo izquierdo
        temp.right = self
        # Se retorna el nodo izquierdo
        return temp

    # Funcion para balancear un nodo
    def balance(self):
        # Si el nodo actual tiene un desbalance hacia la izquierda
        if self.balanceFactor() == 2:
            # Si el subarbol izquierdo del nodo actual tiene un desbalance hacia la derecha
            if self.left.balanceFactor() == -1:
                # Se realiza una rotacion hacia la izquierda en el subarbol izquierdo del nodo actual
                self.left = self.left.rotateLeft()
            # se retorna el nodo actual rotado hacia la derecha
            return self.rotateRight()
        # Si el nodo actual tiene un desbalance hacia la derecha
        if self.balanceFactor() == -2:
            # Si el subarbol derecho del nodo actual tiene un desbalance hacia la izquierda
            if self.right.balanceFactor() == 1:
                # Se realiza una rotacion hacia la derecha en el subarbol derecho del nodo actual
                self.right = self.right.rotateRight()
            # se retorna el nodo actual rotado hacia la izquierda
            return self.rotateLeft()
        # Si el nodo actual no tiene desbalance, se retorna el nodo actual
        return self

    # Función para encontrar un nodo
    def findNode(self, target, node=None):
        # Si el dato del nodo es igual que el objetivo, se guarda el nodo en una variable y se retorna
        if self.data == target:
            node = self
        # Si el dato del nodo es menor que el objetivo, se busca en el subarbol izquierdo
        if self.left is not None:
            node = self.left.findNode(target, node)
        # Si el dato del nodo es mayor que el objetivo, se busca en el subarbol derecho
        if self.right is not None:
            node = self.right.findNode(target, node)
        # se retorna el nodo encontrado o None si no se encuentra
        return node

    # Función para encontrar el tio de un nodo
    def findUncle(self, target, uncleNode=None):
        # Se comienza buscando por el subarbol izquierdo
        if self.left is not None:
            # En el subarbol izquierdo, se compara el dato de 2 niveles debajo (si existen) del nodo actual con el objetivo
            if self.left.left is not None and self.left.left.data == target or self.left.right is not None and self.left.right.data == target:
                # si el dato es igual al objetivo, se guarda el hijo izquierdo del nodo actual en una variable para ser retornado
                uncleNode = self.right
            uncleNode = self.left.findUncle(target, uncleNode)
        # Se busca por el subarbol derecho
        if self.right is not None:
            # En el subarbol derecho, se compara el dato de 2 niveles debajo (si existen) del nodo actual con el objetivo
            if self.right.left is not None and self.right.left.data == target or self.right.right is not None and self.right.right.data == target:
                # si el dato es igual al objetivo, se guarda el hijo derecho del nodo actual en una variable para ser retornado
                uncleNode = self.left
            uncleNode = self.right.findUncle(target, uncleNode)
        # se retorna bien se el nodo encontrado o nulo
        return uncleNode

    # Función para encontrar el abuelo de un nodo
    def findGrandparent(self, target, Grandparent=None):
        # Se comienza buscando por el subarbol izquierdo
        if self.left is not None:
            # En el subarbol izquierdo, se compara el dato de 2 niveles debajo (si exitsten) del nodo actual con el objetivo
            if self.left.left is not None and self.left.left.data == target or self.left.right is not None and self.left.right.data == target:
                # si el dato es igual al objetivo, se guarda el nodo actual en una variable para ser retornado
                Grandparent = self
            Grandparent = self.left.findGrandparent(target, Grandparent)
        # Se busca por el subarbol derecho
        if self.right is not None:
            # En el subarbol derecho, se compara el dato de 2 niveles debajo (si exitsten) del nodo actual con el objetivo
            if self.right.left is not None and self.right.left.data == target or self.right.right is not None and self.right.right.data == target:
                # si el dato es igual al objetivo, se guarda el nodo actual en una variable para ser retornado
                Grandparent = self
            Grandparent = self.right.findGrandparent(target, Grandparent)
        # se retorna bien se el nodo encontrado o nulo
        return Grandparent

    # Función para imprimir por niveles los nodos del árbol
    def levelOrder(self):
        # Función auxiliar para imprimir un nivel del árbol
        def printLevel(node, level):
            if node is not None:
                # Cuando se llega al nivel deseado, se imprime el dato del nodo
                if level == 0:
                    print(node.data, end = ' ')
                else:
                    #Se llama recursivamente a la función con un nivel menos
                    printLevel(node.left, level-1)
                    printLevel(node.right, level-1)
        # Se utiliza la función auxiliar para imprimir cada nivel del árbol desde el nivel 0 hasta la altura del árbol
        for i in range(self.height() + 1):
            # Se imprime el nivel i
            printLevel(self, i)
            
    
   
        
