console.log('Debug Start');

// --- CONFIGURATION AND INITIAL SETUP ---

// 1. Retrieve the CSRF Token from the template
const csrfTokenElement = document.getElementById('csrf-token');
const CSRF_TOKEN = csrfTokenElement ? JSON.parse(csrfTokenElement.textContent) : null;
const API_URL = '/api/receive-text/'; // Define the URL for clarity

// 2. Get DOM Elements
const inputElement = document.getElementById('my-text-input');
const sendButton = document.getElementById('send-data-button');
const changeButton = document.getElementById('change-pic-button');

// --- FETCH FUNCTION ---

async function sendText(textData) {
    if (!CSRF_TOKEN) {
        console.error("CSRF token is missing. Aborting request.");
        return;
    }

    // Structure the data as an object to send JSON
    const dataToSend = {
        input_text: textData
    };

    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': CSRF_TOKEN
            },
            body: JSON.stringify(dataToSend)
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(`Server Error (${response.status}): ${errorData.message}`);
        }

        const responseData = await response.json();
        console.log("SUCCESS. Server acknowledged with message:", responseData.message);

    } catch (error) {
        console.error("Fetch request failed:", error.message);
    }
}

async function changePic() {
    if (!CSRF_TOKEN) {
        console.error("CSRF token is missing. Aborting request.");
        return;
    }

    console.log('change picture command received');

    const imageElement = document.getElementById('testpic');
    const newImageUrl = '/static/myapp/img/evImg.jpeg';

    if (imageElement) {
        // const newImageUrl = imageElement.getAttribute('data-new-src');
        imageElement.src = newImageUrl;
    }


}

// --- EVENT LISTENER ---

// Add a listener to the button
if (sendButton) {
    sendButton.addEventListener('click', () => {
        // Get the current value from the input field
        const inputValue = inputElement.value;

        // Check if the input is empty
        if (inputValue.trim() === "") {
            alert("Please enter some text before sending.");
            return;
        }

        console.log(`Sending: "${inputValue}"`);
        // Call the fetch function with the text
        sendText(inputValue);
    });
}

// Add a listener to the change button
if (changeButton) {
    changeButton.addEventListener('click', () => {
        // Get the current value from the input field
        //const inputValue = inputElement.value;

        // Check if the input is empty
        //if (inputValue.trim() === "") {
           // alert("Please enter some text before sending.");
           // return;
        //}

        console.log(`change pic`);
        // Call the  function to change the picture
        changePic();
    });
}

// 1. Get the script element using the ID
const scriptElement = document.getElementById('debug-data');

// Check if the element exists before trying to access its content
if (scriptElement) {
    // 2. Extract the text content (the JSON string)
    const jsonString = scriptElement.textContent;

    // 3. Parse the JSON string into a usable JavaScript object/array
    try {
        const pList = JSON.parse(jsonString);

        // --- Data Manipulation Starts Here ---

        console.log("Successfully retrieved and parsed pList:", pList);

        // Example: Accessing the first item (assuming pList is an array)
        // if (Array.isArray(pList) && pList.length > 0) {
        //     console.log("First item in pList:", pList[0]);
        // }

        // Example: Iterate and display some property (assuming pList is an array of objects)
        // pList.forEach(item => {
        //     console.log(`Item ID: ${item.id} | Item Name: ${item.name}`);
        //     // Add logic to manipulate the DOM here
        // });

    } catch (error) {
        console.error("Error parsing JSON data from 'debug-data':", error);
    }
} else {
    console.error("Could not find script element with ID 'debug-data'. Check your template.");
}