// static/script.js

let inputField = document.getElementById('inputField');

inputField.addEventListener('keydown', function (event) {
    // Check if the Enter key is pressed
    if (event.key === 'Enter') {
        let inputData = inputField.value;
        sendDataToServer(inputData);
    }
});

inputField.addEventListener('keyup', function (event) {
    // Check if the Enter key is released
    if (event.key === 'Enter') {
        // Clear the input field when Enter key is released
        inputField.value = '';
    }
});

function sendDataToServer(data) {
    // Create a new XMLHttpRequest
    let xhr = new XMLHttpRequest();

    // Configure it to make a POST request to the server
    xhr.open('POST', '/process_input', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

    // Send the data to the server
    xhr.send('input_data=' + encodeURIComponent(data));
}
