# 💊 MediScan – Smart Medicine Label Reader

MediScan is a Python-based OCR application that reads text from a medicine label image and searches a medicine dataset to display general label information.

The project uses EasyOCR to extract visible text from the uploaded image and connects the extracted medicine name with a dataset containing medicine information.

## ✨ Features

- 📷 Upload a medicine label image
- 🔍 Extract text from the image using EasyOCR
- 💊 Detect the medicine name from the extracted text
- 📊 Search the medicine in a dataset
- 📋 Display medicine name, ingredient, strength, form, manufacturer, and common use
- 🖥️ Interactive web interface using Streamlit
- 🌙 Dark-themed user interface
- ⚠️ Handles medicines that are not available in the dataset

## 🔄 Project Workflow

Medicine Label Image
        ↓
     OpenCV
        ↓
     EasyOCR
        ↓
  Extracted Text
        ↓
  Medicine Name
        ↓
  Dataset Search
        ↓
Medicine Information

TECHNOGIES USED
| Technology | Purpose                              |
| ---------- | ------------------------------------ |
| Python     | Main programming language            |
| EasyOCR    | Text extraction from medicine images |
| OpenCV     | Image processing                     |
| Pandas     | Dataset handling                     |
| Streamlit  | Web application interface            |

PROJECT STRUCTURE
MediScan/
│
├── data/
│   └── medicines.csv
│
├── sample_images/
│   └── test_medicine.jpg
│
├── app.py
├── ocr.py
├── medicine_info.py
├── requirements.txt
├── README.md
└── .gitignore

DATASET
## 🧪 Dataset

A synthetic dataset with **250 records** is used for testing and demonstration.

It contains:
- Product name
- Ingredient
- Strength
- Form
- Manufacturer
- Common use

## 🖥️ Application

Upload a medicine label image. MediScan uses **EasyOCR** to extract the medicine name and searches the dataset to display general information.

