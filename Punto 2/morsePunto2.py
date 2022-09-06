class Morse:
    # Función para llenar el árbol con los valores del codigo morse
    def initializeMorseTree():
        morse = morseTreeNode("")
        morse.dot = morseTreeNode("E")
        morse.dash = morseTreeNode("T")
        morse.dot.dot = morseTreeNode("I")
        morse.dot.dash = morseTreeNode("A")
        morse.dash.dot = morseTreeNode("N")
        morse.dash.dash = morseTreeNode("M")
        morse.dot.dot.dot = morseTreeNode("S")
        morse.dot.dot.dash = morseTreeNode("U")
        morse.dot.dash.dot = morseTreeNode("R")
        morse.dot.dash.dash = morseTreeNode("W")
        morse.dash.dot.dot = morseTreeNode("D")
        morse.dash.dot.dash = morseTreeNode("K")
        morse.dash.dash.dot = morseTreeNode("G")
        morse.dash.dash.dash = morseTreeNode("O")
        morse.dot.dot.dot.dot = morseTreeNode("H")
        morse.dot.dot.dot.dash = morseTreeNode("V")
        morse.dot.dot.dash.dot = morseTreeNode("F")
        morse.dot.dash.dot.dot = morseTreeNode("L")
        morse.dot.dash.dash.dot = morseTreeNode("P")
        morse.dot.dash.dash.dash = morseTreeNode("J")
        morse.dash.dot.dot.dot = morseTreeNode("B")
        morse.dash.dot.dot.dash = morseTreeNode("X")
        morse.dash.dot.dash.dot = morseTreeNode("C")
        morse.dash.dot.dash.dash = morseTreeNode("Y")
        morse.dash.dash.dot.dot = morseTreeNode("Z")
        morse.dash.dash.dot.dash = morseTreeNode("Q")
        morse.dash.dash.dash.dot = morseTreeNode("Ó")
        morse.dot.dot.dash.dot.dot = morseTreeNode("É")
        morse.dot.dash.dash.dot.dash = morseTreeNode("Á")
        morse.dash.dash.dot.dash.dash = morseTreeNode("Ñ")
        return morse


# Clase Nodo
class morseTreeNode:
    # Constructor, recibe una letra como valor
    def __init__(self, letter: str):
        self.letter = letter
        self.dot = None
        self.dash = None

    # Función para convertir un string a codigo morse
    def encode(self, string: str):

        # Función auxiliar para convertir una letra a codigo morse
        def encondeLetter(self, letter: str, morse=None):
            # Al inicio morse es None, por lo que se crea una lista vacia para ir agregando los puntos y guiones
            if morse is None:
                morse = []
            # Si la letra es igual a la letra del nodo actual, se retorna true e inicia el proceso de regreso insertando puntos y guiones en la lista hasta llegar a la raiz
            if self.letter == letter.upper():
                return True
            # Se busca la letra en el subarbol izquierdo(dot) del nodo actual
            if self.dot is not None and encondeLetter(self.dot, letter, morse):
                # Si se encuentra la letra, se inserta un punto en la lista en la posición 0
                morse.insert(0, ".")
                # Se retorna true para regresar a la anterior llamada si el nodo actual no es la raiz en caso contrario se retorna true para continuar el proceso
                return "".join(morse) if self.letter == "" else True
            # Se busca la letra en el subarbol derecho(dash) del nodo actual
            if self.dash is not None and encondeLetter(self.dash, letter, morse):
                # Si se encuentra la letra, se inserta un guion en la lista en la posición 0
                morse.insert(0, "-")
                # Se retorna true para regresar a la anterior llamada si el nodo actual no es la raiz en caso contrario se retorna true para continuar el proceso
                return "".join(morse) if self.letter == "" else True
            # Si no se encuentra la letra en el subarbol izquierdo ni derecho, se retorna false
            return False

        # Función auxiliar para convertir una palabra a codigo morse
        def encodeWord(self, word: str):
            # Se inicializa un string vacio para ir agregando los puntos y guiones de cada letra de la palabra
            morse = ""
            # Se recorre cada letra de la palabra
            for letter in word:
                # Se agrega el codigo morse de la letra actual al string morse y se agrega un espacio
                morse += encondeLetter(self, letter) + " "
            # Se retorna el string morse sin el ultimo espacio
            return morse.strip()

        # Se separa la cadena de texto en palabras
        wordsList = string.split()
        # Se recorre la lista con las palabras
        for word in wordsList:
            # Se remplaza cada palabra por su codigo morse y se agrega un espacio
            wordsList[wordsList.index(word)] = encodeWord(self, word) + " "
        # Se retorna el string con el codigo morse de cada palabra separadas con una barra y un espacio
        return "/ ".join(wordsList)

    def decode(self, string: str):

        # Función auxiliar para convertir un codigo morse a una letra
        def decodeMorseLetter(self, morseLetter: str):
            # Se verifica si el primer caracter es un punto
            if morseLetter[0] == ".":
                # Si no hay mas caracteres, se retorna la letra del nodo actual, en caso contrario se llama a la función con el subarbol izquierdo(dot) del nodo actual y el string a partir del segundo caracter
                return self.dot.letter if morseLetter[1:] == "" else decodeMorseLetter(self.dot, morseLetter[1:])
            # Se verifica si el primer caracter es un guion
            if morseLetter[0] == "-":
                # Si no hay mas caracteres, se retorna la letra del nodo actual, en caso contrario se llama a la función con el subarbol derecho(dash) del nodo actual y el string a partir del segundo caracter
                return self.dash.letter if morseLetter[1:] == "" else decodeMorseLetter(self.dash, morseLetter[1:])

        # Función auxiliar para convertir un codigo morse a una palabra
        def decodeWord(self, morseWord: str):
            # Se inicializa un string vacio para ir agregando las letras de la palabra
            word = ""
            # Se separa la palabra en letras
            for letter in morseWord.split():
                # Se agrega la letra actual al string word
                word += decodeMorseLetter(self, letter)
            # Se retorna el string word
            return word

        # Se separa la cadena de texto en codigo morse en palabras
        wordsList = string.split("/")
        # Se recorre la lista con las palabras en codigo morse
        for word in wordsList:
            # Se remplaza cada codigo morse por su traducción correspondiente
            wordsList[wordsList.index(word)] = decodeWord(self, word)
        # Se retorna el codigo morse traducido a texto con cada palabra separada por un espacio
        return " ".join(wordsList)


# arbol con el codigo morse
morse = Morse.initializeMorseTree()
# Traducción de texto a codigo morse
print(morse.encode("Estructura de datos II"))
# Traducción de codigo morse a texto
print(morse.decode(". ... - .-. ..- -.-. - ..- .-. .- / -.. . / -.. .- - --- ... / .. .."))
