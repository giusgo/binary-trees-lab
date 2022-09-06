/**
    The Node class here is just for doing the graph,
    it does NOT do any operation on the tree (inserting, deleting, etc.).
    It helps for keeping track of the connections between each node.

**/


// Graph box
const graph = document.getElementById("tree");

// Node constructor (within the graph)
class Node {
    constructor(element, data) {
        this.element = element;
        this.data = data;
        this.left = null;
        this.right = null;
    }

    set setData(value) {
        this.data.innerHTML = value;
    }

    show() {
        this.element.style.display = "block";
    }
}

// Collection of Nodes objects in DOM
var Nodes = [];

// Collection of nodes in the graph box
const nodes_collection = document.getElementsByClassName("node");
// Collection of data of each node
const data_collection = document.getElementsByClassName("data");

function Setup() {

    // Creating nodes in DOM
    for (let i = 0; i < nodes_collection.length; i++) {
        element = nodes_collection[i];
        data = data_collection[i];
        Nodes[i] = new Node(element, data);
    }

    // Linking each node
    Nodes[0].left = Nodes[1];
    Nodes[0].right = Nodes[2];

    Nodes[1].left = Nodes[3];
    Nodes[1].right = Nodes[4];
    Nodes[2].left = Nodes[5];
    Nodes[2].right = Nodes[6];

    Nodes[3].left = Nodes[7];
    Nodes[3].right = Nodes[8];
    Nodes[4].left = Nodes[9];
    Nodes[4].right = Nodes[10];
    Nodes[5].left = Nodes[11];
    Nodes[5].right = Nodes[12];
    Nodes[6].left = Nodes[13];
    Nodes[6].right = Nodes[14];
}
    


// Draw the graph
function drawGraph() {

    // Reset the graph
    for (let i = 0; i < nodes_collection.length; i++) {
        nodes_collection[i].style.display = 'none';
    }

    var nodes_to_graph = []; // Nodes to graph in the graph box

    // Get the level order traversal of the tree and graph
    pywebview.api.printLevelOrder().then(
        function(response) {

            // Cleaning the array received in the response
            for(let nodes in response) {
                if (response[nodes] != " ") {
                    nodes_to_graph.push(response[nodes]);
                }
            }

            // Check if the tree is empty
            if (nodes_to_graph[0] == null) {
                return;
            }

            // Root node
            node_root = nodes_to_graph[0];
            Nodes[0].setData = node_root; // Set root data
            Nodes[0].show(); // Show node

            // Compare nodes and graph
            for (let i = 1; i < nodes_to_graph.length; i++) {
                current_node = Nodes[0];

                while (true) {

                    // Search to the right
                    if (parseInt(nodes_to_graph[i]) > parseInt(current_node.data.innerHTML)) {
                        // Check if level > 4:
                        if (current_node.right == null) {
                            showMessage('Tree level > 4, deleting new node...'); // Show warning message
                            pywebview.api.delNode(parseInt(nodes_to_graph[i])); // Delete inserted node
                            break;
                        } 

                        // If it is found
                        if (current_node.right.element.style.display == 'none') {
                            current_node = current_node.right;
                            current_node.setData = parseInt(nodes_to_graph[i]);
                            current_node.show();
                            break;
                        // If NOT
                        } else {
                            current_node = current_node.right;
                        }

                    // Search to the left
                    } else if (parseInt(nodes_to_graph[i]) < parseInt(current_node.data.innerHTML)) {
                        // Check if level > 4:
                        if (current_node.left == null) {
                            showMessage('Tree level > 4, deleting new node...'); // Show warning message
                            pywebview.api.delNode(parseInt(nodes_to_graph[i])); // Delete inserted node
                            break;
                        } 

                        // If it is found
                        if (current_node.left.element.style.display == 'none') {
                            current_node = current_node.left;
                            current_node.setData = parseInt(nodes_to_graph[i]);
                            current_node.show();
                            break;
                        // If NOT
                        } else {
                            current_node = current_node.left;
                        }
                    }
                    
                }
                
            }
        }
    );

}

// Initial setup for the graph
Setup();