# JavaScript DOM Manipulation

This project demonstrates various JavaScript DOM manipulation techniques, from basic element selection to making API requests.

## Contents

### 0. Red Text Header (0-script.js)
**What it does:** Changes the text color of the header element to red (#FF0000).

**Key concepts:**
- `document.querySelector()` - Selects the first element that matches a CSS selector
- Direct style manipulation using the `style` property

### 1. Click to Red (1-script.js)
**What it does:** Changes the header's text color to red when user clicks on an element with ID "red_header".

**Key concepts:**
- Event listeners with `addEventListener`
- Click events
- DOM element selection using ID selectors
- Event-driven programming

### 2. Add Class (2-script.js)
**What it does:** Adds the CSS class "red" to the header when user clicks on the element with ID "red_header".

**Key concepts:**
- `classList.add()` - Modern way to add classes to elements
- Class-based styling vs. inline styles
- CSS class manipulation

### 3. Toggle Classes (3-script.js)
**What it does:** Toggles the header's class between "red" and "green" when clicking on "toggle_header".

**Key concepts:**
- Class toggling logic
- `classList.contains()` - Checking if an element has a specific class
- `classList.remove()` - Removing classes
- Conditional class manipulation

### 4. Add List Items (4-script.js)
**What it does:** Adds a new `<li>` element with text "Item" to a list when clicking on "add_item".

**Key concepts:**
- `document.createElement()` - Creating new DOM elements
- `textContent` - Setting element content
- `appendChild()` - Adding elements to the DOM
- DOM tree manipulation

### 5. Update Header Text (5-script.js)
**What it does:** Updates the header text to "New Header!!!" when clicking on "update_header".

**Key concepts:**
- Modifying text content of existing elements
- Text manipulation with `textContent`

### 6. Star Wars Character (6-script.js)
**What it does:** Fetches data about a Star Wars character and displays the name.

**Key concepts:**
- `fetch()` API - Making HTTP requests
- Promises - Handling asynchronous operations
- `.then()` - Processing fetch results
- Error handling with `.catch()`
- Working with external APIs
- JSON parsing

### 7. Star Wars Movies (7-script.js)
**What it does:** Fetches all Star Wars movies and displays their titles in a list.

**Key concepts:**
- Working with API data containing arrays
- Dynamic list creation
- Iterating through API results with `forEach()`
- Creating multiple DOM elements programmatically

### 8. Hello Translation (8-script.js)
**What it does:** Fetches a translation of "hello" in French and displays it.

**Key concepts:**
- `DOMContentLoaded` event - Ensuring the DOM is ready
- Loading JavaScript in the `<head>` tag
- Handling API responses
- Script execution timing

## General DOM Manipulation Concepts

- **DOM (Document Object Model)**: A programming interface that represents HTML as a tree of objects
- **Selectors**: Different ways to target HTML elements (by tag, class, ID)
- **Events**: User actions that can trigger JavaScript code
- **Event Listeners**: Functions that wait for specific events to occur
- **DOM Traversal**: Moving through the DOM tree to find elements
- **DOM Manipulation**: Changing the structure, style, or content of the page
- **Asynchronous JavaScript**: Using promises and fetch for non-blocking operations
