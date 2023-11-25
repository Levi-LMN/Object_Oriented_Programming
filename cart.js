// Function to add item to the cart with additional functionality
function addItemToCart(containerId, button) {
    // Get the product container HTML by ID
    var productContainerHTML = document.getElementById(containerId).cloneNode(true);

    // Remove the "Add to Cart" button in the cloned product container
    var btnBox = productContainerHTML.querySelector(".btn-box");
    btnBox.parentNode.removeChild(btnBox);

    // Check if the item is already in the cart
    if (isItemInCart(productContainerHTML.outerHTML)) {
        alert("Item is already in the cart!");
        return;
    }

    // Create a new list item for the cart
    var listItem = document.createElement("li");
    listItem.innerHTML = productContainerHTML.outerHTML;

    // Create a remove button for the list item
    var removeButton = document.createElement("button");
    removeButton.textContent = "Remove";
    removeButton.onclick = function () {
        removeItemFromCart(listItem, button);
    };

    // Set the same class as "btn-box" to the remove button
    removeButton.className = "btn-box";

    // Append the remove button to the list item
    listItem.appendChild(removeButton);

    // Append the list item to the cart
    document.getElementById("cartItems").appendChild(listItem);

    // Display an alert
    alert("Item added to the cart!");

    // Ask if the user wants to view the cart
    var viewCart = confirm("Do you want to view the items in the cart?");

    // Change the link text to "In Cart"
    button.textContent = "In Cart";
    button.removeAttribute("onclick"); // Remove the onclick attribute

    // Perform the desired functionality when the user wants to view the cart
    if (viewCart) {
        // Example: Set URL fragment to #cartContainer
        window.location.hash = "cartContainer";
    }
}



    // Function to check if the item is already in the cart
    function isItemInCart(productContainerHTML) {
      var cartItems = document.getElementById("cartItems").getElementsByTagName("li");

      for (var i = 0; i < cartItems.length; i++) {
        var itemHTML = cartItems[i].innerHTML;
        if (itemHTML === productContainerHTML) {
          return true; // Item is already in the cart
        }
      }

      return false; // Item is not in the cart
    }

    // Function to remove item from the cart
    function removeItemFromCart(item, button) {
      // Remove the item from the cart
      document.getElementById("cartItems").removeChild(item);

      // Display an alert
      alert("Item removed from the cart!");

      // Change the link text back to "Add to Cart"
      button.textContent = "Add To Cart";
      button.onclick = function () {
        addItemToCart(button);
        return false;
      };
    }
