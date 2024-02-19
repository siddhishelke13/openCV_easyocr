import cv2
import easyocr
import os

# Function to process images in a folder using EasyOCR
def process_images(input_folder, output_folder):
    # Create EasyOCR reader
    reader = easyocr.Reader(['en'])

    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all image files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            # Read the image
            image_path = os.path.join(input_folder, filename)
            img = cv2.imread(image_path)

            # Get OCR results
            results = reader.readtext(image_path)

            # Draw bounding boxes and text on the image
            for (bbox, text, prob) in results:
                (top_left, top_right, bottom_right, bottom_left) = bbox
                top_left = tuple(map(int, top_left))
                bottom_right = tuple(map(int, bottom_right))

                # Draw red box around the detected text
                cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 2)

                # Display green text beside the red box
                cv2.putText(img, text, (top_left[0], top_left[1] - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Save the processed image to the output folder
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, img)

# Specify input and output folders
input_folder = r'D:\Download Siddhi\easyOCR\images_test'
output_folder = r'D:\Download Siddhi\easyOCR\images_test_output'

# Call the function to process images
process_images(input_folder, output_folder)
