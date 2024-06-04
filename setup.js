// script.js
// Array of image URLs
var images = [
    "image1.jpg",
    "image2.jpg",
    "image3.jpg",
    // Add more image URLs as needed
  ];
  
  function showRandomImage() {
    var imageContainer = document.getElementById("image-container");
    // Clear previous image if any
    imageContainer.innerHTML = "";
  
    // Generate a random index
    var randomIndex = Math.floor(Math.random() * images.length);
  
    // Create image element
    var img = document.createElement("img");
    img.src = images[randomIndex];
    img.alt = "Random Image";
    
    // Append image to container
    imageContainer.appendChild(img);
  }
  