console.log('Debug Start');

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