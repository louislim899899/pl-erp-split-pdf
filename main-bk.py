from PyPDF2 import PdfReader, PdfWriter
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import os
import cv2
import numpy as np

# Function to extract images from PDF
def extract_images_from_pdf(pdf_file):
    images = convert_from_path(pdf_file)
    return images

# Function to recognize red numbers in an image
def recognize_red_numbers2(image_file, red_threshold=150):
    img = Image.open(image_file)
    img = img.convert("RGB")
    img = img.split()[-1]  # Keep only the red channel
    
    red_pixels = []
    for pixel in img.getdata():
        if pixel < red_threshold:
            red_pixels.append(pixel)
    #     if pixel[0] > red_threshold and pixel[1] < red_threshold and pixel[2] < red_threshold:
    #         red_pixels.append(pixel)

    red_img = Image.new("RGB", img.size, (255, 255, 255))
    red_img.putdata(red_pixels)
    
    # text = pytesseract.image_to_string(img)
    # print(img.getdata().size)
    red_img.show()
    exit()
    return text

def recognize_red_numbers2(image_file):
    img = cv2.imread(image_file)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)

    mask = cv2.inRange(hsv, (0,0,0), (180, 50, 130))
    dst1 = cv2.bitwise_and(img, img, mask=mask)

    th, threshed = cv2.threshold(v, 150, 255, cv2.THRESH_BINARY_INV)
    dst2 = cv2.bitwise_and(img, img, mask=threshed)

    th, threshed2 = cv2.threshold(s, 30, 255, cv2.THRESH_BINARY_INV)
    dst3 = cv2.bitwise_and(img, img, mask=threshed2)
    
    cv2.imshow('img',dst3)
    cv2.waitKey(0) 
    exit()

    cv2.imwrite("dst1.png", dst1)
    cv2.imwrite("dst2.png", dst2)
    cv2.imwrite("dst3.png", dst3)

def recognize_red_numbers(image_file):
    img = cv2.imread(image_file)

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])

    mask1 = cv2.inRange(img_hsv, lower_red, upper_red)

    lower_red = np.array([170, 50, 50])
    upper_red = np.array([180, 255, 255])

    mask2 = cv2.inRange(img_hsv, lower_red, upper_red)

    mask = mask1 + mask2

    red_img = cv2.bitwise_and(img, img, mask=mask)

    gray_img = cv2.cvtColor(red_img, cv2.COLOR_BGR2GRAY)
    _, threshold_img = cv2.threshold(gray_img, 200, 255, cv2.THRESH_BINARY)
    
    cv2.imshow('img',red_img)
    cv2.waitKey(0) 
    exit()
    
    text = pytesseract.image_to_string(red_img)
    if (text is None) :
        raise Exception("no text extracted")
    
    return(text)


    # text = pytesseract.image_to_string(threshold_img)
    
def split_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page_num])

    # Save each page as a separate PDF file
    with open(f'./singles/page_{page_num + 1}.pdf', 'wb') as f:
        pdf_writer.write(f)

# Function to split PDF into individual pages and process each page
def split_and_process_pdf(pdf_file):
    images = extract_images_from_pdf(pdf_file)
    for i, image in enumerate(images):
        extracted_image_file = f"page_{i+1}.png"
        image.save(extracted_image_file)
        # red_numbers = recognize_red_numbers(extracted_image_file)
        # os.remove(extracted_image_file)
        new_pdf_name = f"page_{i+1}.pdf"
        # new_pdf_name = f"{red_numbers.strip()}.pdf"
        # new_image_name = f"{red_numbers.strip()}.jpg"
        os.rename(pdf_file, "./singles/" + new_pdf_name)
        # os.rename(extracted_image_file, "./result/" + new_image_name)

# Main function to execute the script
def main():
    pdf_file_path = os.path.dirname(os.getcwd() + "/") + "/data/4341_to_3249.pdf"
    # split_and_process_pdf(pdf_file_path)
    # split_pdf(pdf_file_path)
    broken_image = os.path.dirname(os.getcwd() + "/") + "/result/.jpg"
    recognize_red_numbers2(broken_image)

if __name__ == "__main__":
    main()
