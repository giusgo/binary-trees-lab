#CLASE NODO
class BTreeNode:
    #constructor
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []

#CLASE BTREE
class BTree:
    #constructor, donde t es el orden de la árbol
    def __init__(self, t):
        self.root = None
        self.t = t
    
    #funcion para insertar una llave en el árbol
    def insertNode(self, key):

        # si la raíz está vacía, se le asigna un nodo a la raíz
        if self.root is None:
            self.root = BTreeNode(True)
            self.root.keys.append(key)
            return
            
        #si el árbol no está vacío, se inserta la llave en el árbol
        self.insertWhileIsNotFull(self.root, key)

        #si el nodo esta lleno, el árbol crece en altura
        if len(self.root.keys) == (2 * self.t) - 1:
            #se crea un nuevo nodo raíz, dondé el nodo no es hoja
            newRoot = BTreeNode(False)
            #se guarda la raíz actual en una variable
            oldRoot = self.root
            #la raiz actual se actualiza a la nueva raíz creada
            self.root = newRoot
            # la nueva raiz tendrá como hijo la vieja ráiz
            newRoot.child.append(oldRoot)
            # se divide la raiz vieja en dos, y la llave media de dicha raíz se mueve a la nueva raíz padre
            self.splitChild(newRoot, 0)

    def insertWhileIsNotFull(self, root, key):

        #se inicializa un indice como el valor maximo del array de llaves de la raíz	
        i = len(root.keys) - 1

        #si la raíz es una hoja
        if root.leaf:    
            #se inserta la llave en el array de llaves de la raíz
            root.keys.append(key)
            #se ordena el array de llaves de la raíz de forma ascendente
            root.keys.sort()

        #si la raíz no es una hoja
        else:
            #se encuentra el hijo de la raíz mas apropiado para insertar la llave
            while i >= 0 and key < root.keys[i]:
                i -= 1
            i += 1

            #se inserta la llave en el hijo apropiado
            self.insertWhileIsNotFull(root.child[i], key)

            #si el nodo hijo en el que se insertó la llave está lleno, se divide
            if len(root.child[i].keys) == (2 * self.t) - 1:
                self.splitChild(root, i)
                if key > root.keys[i]:
                    i += 1
            
    def splitChild(self, root, i):

        #se crea un nuevo nodo de la misma naturaleza(hoja o no) que el nodo a dividir
        newNode = BTreeNode(root.child[i].leaf)

        # el nuevo nodo debe tener t-1 llaves(es decir todas las llaves posteriores a t)
        for j in range(self.t - 1):
            #se insertan las llaves de la raíz en el nuevo nodo creado previamente
            newNode.keys.append(root.child[i].keys[j + self.t])
        
        # si el hijo no es una hoja, se insertan los hijos de la raíz en el nuevo nodo creado previamente
        if not root.child[i].leaf:
            for j in range(self.t):
                newNode.child.append(root.child[i].child[j + self.t])
            
        # el valor medio del nodo que se divido sube al nodo padre
        root.keys.append(root.child[i].keys[self.t - 1])

        # se remueven del nodo divido todos los valores que se insertaron en el nuevo nodo y el valor t que subió al nodo padre
        for j in range((root.child[i].keys.__len__() - self.t)+1):
            root.child[i].keys.pop()

        #el nuevo nodo se inserta en el nodo padre
        root.child.append(newNode)

    #función para imprimir el árbol
    def print_tree(self, x, l=0):
        print("Level ", l, " ", len(x.keys), end=":")
        for i in x.keys:
            print(i, end=" ")
        print()
        l += 1
        if len(x.child) > 0:
            for i in x.child:
                self.print_tree(i, l)
    #creditos de la función para imprimir el árbolhttps://www.programiz.com/dsa/b-tree

#main
def main():
    #se crea el árbol
    B = BTree(3)
    #se insertan las llaves en el árbol
    B.insertNode(5)
    B.insertNode(3)
    B.insertNode(2)
    B.insertNode(4)
    B.insertNode(1)
    B.insertNode(6)
    B.insertNode(7)
    B.insertNode(8)
    B.insertNode(9)
    B.insertNode(10)
    B.insertNode(11)
    #se imprime el árbol
    B.print_tree(B.root)
    
if __name__ == '__main__':
    main()