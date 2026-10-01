import easyocr
import cv2
import os
from medicine_info import search_medicine

# Create OCR reader
reader = easyocr.Reader(['en'])


def extract_text(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Could not read the image.")
        return ""

    results = reader.readtext(image)

    extracted_text = []

    for result in results:
        text = result[1]
        extracted_text.append(text)

    return "\n".join(extracted_text)


# Image path
image_path = os.path.join("sample_images", "test_medicine.jpg")

print("Image path:", image_path)
print("Image exists:", os.path.exists(image_path))

# OCR
text = extract_text(image_path)

print("\nExtracted Text:")
print(text)


# Search medicine using first OCR line
lines = text.splitlines()

if lines:
    medicine_name = lines[0].strip()

    print("\nSearching dataset for:", medicine_name)

    medicine = search_medicine(medicine_name)

    if medicine is not None:
        print("\nMedicine Found!")
        print("-------------------------")
        print("Medicine Name:", medicine["product_name"])
        print("Ingredient:", medicine["active_or_main_ingredient"])
        print("Strength:", medicine["strength"])
        print("Form:", medicine["dosage_or_form"])
        print("Manufacturer:", medicine["manufacturer"])
        print("Common Use:", medicine["common_use"])
    else:
        print("\nMedicine not found in dataset.")