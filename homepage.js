
        // Function to update the displayed file name
        function updateFileNameDisplay() {
          const fileInput = document.getElementById("fileUpload");
          const fileNameDisplay = document.getElementById("fileNameDisplay");
          
          if (fileInput.files.length > 0) {
            fileNameDisplay.textContent = fileInput.files[0].name;
          } else {
            fileNameDisplay.textContent = "No file chosen";
          }
        }
      
        // Add event listener to the file input to trigger the update when a file is chosen
        const fileInput = document.getElementById("fileUpload");
        fileInput.addEventListener("change", updateFileNameDisplay);
      