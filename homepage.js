function updateFileNameDisplay() {
  const fileInput = document.getElementById('fileUpload');
  const fileNameDisplay = document.getElementById('fileNameDisplay');

  if (fileInput.files.length > 0) {
    fileNameDisplay.textContent = 'Uploaded Successfully';
  } else {
    fileNameDisplay.textContent = 'No file chosen';
  }
}

const fileInput = document.getElementById('fileUpload');
fileInput.addEventListener('change', () => {
  updateFileNameDisplay();
  toggleSubmitButton();
});

updateFileNameDisplay();

function toggleSubmitButton() {
  const fileInput = document.getElementById('fileUpload');
  const submitButton = document.getElementById('submitBtn');

  if (fileInput.files.length > 0) {
    submitButton.disabled = false;
  } else {
    submitButton.disabled = true;
  }
}

const form = document.getElementById('myForm');
form.addEventListener('submit', (event) => {
  event.preventDefault();

  const submitButton = document.getElementById('submitBtn');
  const loadingSpinner = document.getElementById('loadingSpinner');
  const successMessage = document.getElementById('successMessage');

  submitButton.style.display = 'none';
  loadingSpinner.style.display = 'block';

  // Perform your form submission here (e.g. using fetch())

  setTimeout(() => {
    // Hide the loading spinner and show the success message
    loadingSpinner.style.display = 'none';
    successMessage.style.display = 'block';
  }, 1500);
});
