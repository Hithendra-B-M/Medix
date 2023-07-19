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
