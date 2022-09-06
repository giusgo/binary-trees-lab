from AVLTree import AVLTree    # Class for an individual tree
import webview                 # GUI framework
import sys                     # For Logger class

# Logger for console output
class Logger():
    stdout = sys.stdout
    messages = []

    def start(self): 
        sys.stdout = self
        self.messages = []

    def stop(self): 
        sys.stdout = self.stdout

    def write(self, text): 
        self.messages.append(text)

# Class for inter-domain communication between the window (python)
# and JavaScript.
class WindowApi():
    def __init__(self):
        self._window = None

    # Store generated window
    def set_window(self, window):
        self._window = window

    # Quit window
    def quit(self):
        self._window.destroy()
    
    ### Methods for JavaScript ###
    # Insert a new node
    def addNode(self, data):
        AVL.insertNode(data)

    # Delete an existing node
    def delNode(self, data):
        AVL.deleteNode(data)

    # Searching an existing node
    def search(self, data):
        log.start()
        AVL.find(data)
        log.stop()

        return log.messages # Return node (if found)

    # Print the level order traversal of the tree
    def printLevelOrder(self):
        log.start()
        AVL.levelOrder()
        log.stop()

        return log.messages # Return nodes (if found)
    
    # Print the height of a node
    def getHeight(self, data):
        log.start()
        AVL.height(data)
        log.stop()

        return log.messages # Return height of the node (if found)

    # Print the grandpa of a node
    def getGrandpa(self, data):
        log.start()
        AVL.findGrandparent(data)
        log.stop()

        return log.messages # Return grandpa of the node (if found)

    # Print the uncle of a node
    def getUncle(self, data):
        log.start()
        AVL.findUncle(data)
        log.stop()

        return log.messages # Return uncle of the node (if found)


if __name__ == '__main__':

    # Python console logger
    log = Logger()

    # Tree to use to display
    AVL = AVLTree()

    # API object
    window_api = WindowApi()

    # Graphical interface
    window = webview.create_window('AVL Tree visualization', url='views/index.html', js_api=window_api, width=1280, height=720, easy_drag=False, \
                        resizable=False, fullscreen=False, frameless=True, minimized=False, on_top=True, confirm_close=False, text_select=False)

    # Store generated window
    window_api.set_window(window)

    # Start window
    webview.start()
