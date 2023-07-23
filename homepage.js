// homepage.js

function updateFileNameDisplay() {
  const fileInput = document.getElementById("fileUpload");
  const fileNameDisplay = document.getElementById("fileNameDisplay");

  if (fileInput.files.length > 0) {
    fileNameDisplay.textContent = "Uploaded Successfully";
  } else {
    fileNameDisplay.textContent = "No file chosen";
  }
}

// Add event listener to the file input to trigger the update when a file is chosen
const fileInput = document.getElementById("fileUpload");
fileInput.addEventListener("change", updateFileNameDisplay);

// Call the function on page load to set the initial message
updateFileNameDisplay();
