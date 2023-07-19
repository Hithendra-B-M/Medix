<div align="center">
  <image src="https://github.com/k-arthik-r/Medix/assets/111432615/e3521579-d9eb-49cc-a8b3-b8858da689e4"/>
</div>

----------------------------

<div align="center">
  <a><img src="https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white"></a> &nbsp;
</div>

----------------------------

## Requirments
Python 

<a href="https://www.python.org/downloads/" alt="3.11.1">
        <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" /></a>
  
<h4>Modules Imported</h4>

- numpy
- pandas
- tensorflow
- sklearn
- matplotlib

The Current model was trained using Kaggle GPU P100 Accelerator.

----------------------------

## Dataset

API Command
```bash
kaggle datasets download -d voidexiae/nih-chest-x-ray-voidex
```

Link
```bash
https://www.kaggle.com/datasets/voidexiae/nih-chest-x-ray-voidex
```
----------------------------

## How to train the Model using Kaggle?

Visit
```bash
https://www.kaggle.com/
```

Next, 
- After Successfull Login,
- Click on Create -> New Notebook
- Click on Add Data -> NIH | Chest-X-Ray | Voidex (Search for this)
- Now, select add dataset

- After Successfully Adding dataset,
- Copy the code present in [train.py](train.py)
- Include it in the code section of the kaggle notebook.
- goto More -> Accelerator -> GPU P100
- Click on Run.
- Wait till all the Epoch are Completed and check for the HDF(.h5) file in the output folder of the kaggle Notebook.

## Use test and validate
import both test.py and validate.py python file along with Voidex.h5 and run it using,
```bash
python test.py
```
```bash
python validate.py
```

----------------------------

## About the Model

### Input Layer
The input images are expected to have a shape of (img_width, img_height, 3), representing RGB images.

### Convolutional Layers
- The first convolutional layer has 32 filters with a kernel size of (3, 3) and applies the ReLU activation function.
- MaxPooling is applied with a pool size of (2, 2) to reduce the spatial dimensions of the output.
- The second convolutional layer has 64 filters with a kernel size of (3, 3) and applies the ReLU activation function.
- MaxPooling is applied again with a pool size of (2, 2).
- The third convolutional layer has 128 filters with a kernel size of (3, 3) and applies the ReLU activation function.
- MaxPooling is applied once more with a pool size of (2, 2).

  
### Flattening Layer
The output of the last convolutional layer is flattened into a 1-dimensional vector to be fed into the dense layers.

### Dense Layers
- The flattened vector is passed through a dense layer with 128 units and the ReLU activation function.
- The final dense layer has 18 units (corresponding to the 18 classes) and applies the sigmoid activation function.
- The sigmoid activation function is used because the task is multi-label classification, where each class can be present or absent independently.
  
### Model Compilation
- The model is compiled with the Adam optimizer and the binary cross-entropy loss function, suitable for multi-label classification.
- The accuracy metric is also specified to monitor the performance during training.
  
### Data Generators
- The code sets up two ImageDataGenerators, train_generator and validation_generator, which perform data augmentation and normalization by rescaling the pixel values to the range [0, 1].
- The generators are configured to load images from the respective directories (dataset_path + '/train' and dataset_path + '/validation').
- The target size for the images is set to (img_width, img_height).
- The class_mode is set to 'categorical', indicating that the labels are one-hot encoded.
  
### Model Training
- The model is trained using the fit function.
- The train_generator is used to provide training data, with the number of steps per epoch set to train_generator.samples // batch_size.
- The training is performed for the specified number of epochs.
- The validation_generator is used to provide validation data, with the number of validation steps set to validation_generator.samples // batch_size.
  
### Model Saving
After training, the model is saved to a file named 'CAESARS.h5' using the save function.

----------------------------

## Test Results

After Successfully testing the Deep Learning Model with 26,000 Image we obtained an Accuracy of 85%.

