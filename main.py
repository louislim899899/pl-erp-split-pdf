# from PyPDF2 import PdfReader, PdfWriter
from pdf2image import convert_from_path
# from PIL import Image
# import pytesseract
import os
# import cv2
# import numpy as np
from natsort import natsorted, ns

# Function to split PDF into individual pages and process each page
def convert_and_rename_pdfs(input_folder, output_folder, skip_num, num_range):
    
    
    pdf_files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]
    pdf_files = natsorted(pdf_files)

    current_index = num_range[0]

    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_folder, pdf_file)
        images = convert_from_path(pdf_path, 
                                   output_folder=output_folder,
                                   fmt="jpeg",
                                   use_pdftocairo=True,
                                   first_page=1,
                                   last_page=len(pdf_files))

        for i, image in enumerate(images):
            while current_index in skip_num:
                current_index -= 1
                
            if current_index < num_range[1]:
                break
            
            new_filename = f"{current_index}.jpg"
            new_filepath = os.path.join(output_folder, new_filename)
            image.save(new_filepath)
            current_index -= 1

# Main function to execute the script
def main():
    pdf_file_path = os.path.dirname(os.getcwd() + "/") + "/data/"
    output_path = os.path.dirname(os.getcwd() + "/") + "/result/"
    skip_num = [3300, 3390, 3416, 3417, 3666, 3825, 3907]
    num_range = [4341, 3249]
    convert_and_rename_pdfs(pdf_file_path, output_path, skip_num, num_range)

if __name__ == "__main__":
    main()
