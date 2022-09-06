// Close window
function Close() {
    pywebview.api.quit();
}

// Get the value from the input box
function getInput() {
    data = document.getElementById("data").value        // Get data from input
    document.getElementById("data").value = null        // Clear input

    return data;
}

// Loading message:
const message_box = document.getElementById("message-box");

function showMessage(message) {
    message_box.innerHTML = message;

    setTimeout(function(){
        message_box.innerHTML = '';
    }, 1000);
}


/*-------------------- API FUNCTIONS (PYTHON) -----------------------*/



// Insert new node
function AddNode() {

    // Output
    var output = document.getElementById("text-output");

    data = getInput();

    // Call Python function
    if (data != '') {
        showMessage('Loading...'); // Show loading message

        output.innerHTML = ''; // Clear previous output

        // Add node
        pywebview.api.addNode(parseInt(data));
        
        // Draw the graph
        setTimeout(function() {
            drawGraph();
        }, 1000)

    }

        
}

// Delete a node
function DelNode() {

    // Output
    var output = document.getElementById("text-output");

    data = getInput();

    // Call Python function
    if (data != '') {
        showMessage('Loading...'); // Show loading message

        output.innerHTML = ''; // Clear previous output

        // Delete note
        pywebview.api.delNode(parseInt(data));

        // Draw the graph
        setTimeout(function() {
            drawGraph();
        }, 1000)
    }
        
}

// Search for a node
function Search() {
    
    data = getInput();

    if (data != '') {
        pywebview.api.search(parseInt(data)).then(
            function(response) {
                // Output
                var output = document.getElementById("text-output");

                if (response[0] == null) {
                    output.innerHTML = 'Node "' + data + '" was not found.';
                } else {
                    output.innerHTML = 'Node "' + data + '" exists.';
                }
            }
        );
    }
}

// Print level order traversal
function PrintLevelOrder() {

    // Call Python function
    pywebview.api.printLevelOrder().then(
        function(response) {
            // Output
            var output = document.getElementById("text-output");

            output.innerHTML = ''; // Clear previous output

            // If no nodes
            if (response[0] == null) {
                output.innerHTML = 'Empty tree.';
                return;
            }
            
            // Print each node data to the output
            output.innerHTML = 'Level order traversal : <br>';
            for (let node of response){
                if (node != " ") {
                    output.innerHTML = output.innerHTML + node + ' ';
                }
                
            }
        }
    );

}

// Height of a node
function getHeight() {

    data = getInput();

    if (data != '') {
        pywebview.api.getHeight(parseInt(data)).then(
            function(response) {
                // Output
                var output = document.getElementById("text-output");

                output.innerHTML = ''; // Clear previous output

                // If no nodes
                if (response[0] == "None") {
                    output.innerHTML = 'Node "' + data + '" does not exist.';
                    return;
                // If it exists
                } else {
                    output.innerHTML = 'The height of the node "' + data + '" is ' + response[0] + '.';
                }
            }
        );
    }
}

// Get the grandpa of the node
function getGrandpa() {

    data = getInput();

    if (data != '') {
        pywebview.api.getGrandpa(parseInt(data)).then(
            function(response) {
                // Output
                var output = document.getElementById("text-output");

                output.innerHTML = ''; // Clear previous output

                // If no nodes
                if (response[0] == null) {
                    output.innerHTML = 'Node "' + data + '" does not exist or does not have grandfather.';
                    return;
                // If it exists
                } else {
                    output.innerHTML = 'The grandfather of the node "' + data + '" is "' + response[0] + '".';
                }
            }
        );
    }
}

// Get the grandpa of the node
function getUncle() {

    data = getInput();

    if (data != '') {
        pywebview.api.getUncle(parseInt(data)).then(
            function(response) {
                // Output
                var output = document.getElementById("text-output");

                output.innerHTML = ''; // Clear previous output

                // If no nodes
                if (response[0] == null) {
                    output.innerHTML = 'Node "' + data + '" does not exist or does not have uncle.';
                    return;
                // If it exists
                } else {
                    output.innerHTML = 'The uncle of the node "' + data + '" is "' + response[0] + '".';
                }
            }
        );
    }

}