# PDF 2 Image

This mini app convert a list of pdfs into jpgs.

## Caution
The images produced will be named in the range of numbers defined by user, in **DESCENDING ORDER**!!

## How to use

1. If you have a pdf with multiple pages, break the page using online tools or adobe acrobat reader pro

2. Put the list of data into data directory

3. Edit variable:
* **pdf_file_path** (str): where all your pdfs located
* **output_path** (str): where the output will be produced
* **skip_num** (int[]): 
* **num_range** (int[2]): named by number from start to end. eg: 30,1 = 30.jpg, 29.jpg ... 1.jpg

4.  run $ python main.py