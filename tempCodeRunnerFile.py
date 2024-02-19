import cv2
import easyocr

# Function to read text from an image using EasyOCR
def read_text_from_image(image_path, output_file):
    # Create EasyOCR reader
    reader = easyocr.Reader(['en'])

    # Read the image
    img = cv2.imread(image_path)

    # Get OCR results
    results = reader.readtext(image_path)

    # Write the detected text to the output file
    with open(output_file, 'w') as f:
        for (bbox, text, prob) in results:
            f.write(text + '\n')

    print("Text written to", output_file)

# Get input image path from the user
image_path = input("D:\Download Siddhi\easyOCR\Task2 data\4.png ")

# Define the output file name
output_file = 'detected_text.txt'

# Call the function to read text from the image and write to the output file
read_text_from_image(image_path, output_file)
