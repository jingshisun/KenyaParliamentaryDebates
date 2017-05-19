#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 19 09:23:29 2017

@author: jingshisun
"""


import PyPDF2
import os 
import glob

def convert_pdf_to_txt(year):
    
    pathin = "/Users/jingshisun/Desktop/KenyaParliamentaryDebates/sentiment/FlatWorldFiles/" + year + "/Input/"
    pathout = "/Users/jingshisun/Desktop/KenyaParliamentaryDebates/sentiment/FlatWorldFiles/" + year + "/Output/"
    os.chdir(pathin)
    # read all pdf files under the folder year
    read_files = glob.glob("*.pdf")
    
    
    
    # add them to the wordstring
    for f in read_files:
        os.chdir(pathin)
        with open(f, "rb") as pdf_file:
            # a string to record all words
            wordstring =''
            read_pdf = PyPDF2.PdfFileReader(pdf_file, strict=False)
            number_of_pages = read_pdf.getNumPages()
            for p in range(0, number_of_pages):
                page = read_pdf.getPage(p)
                page_content = page.extractText()
                wordstring+=str(page_content.encode('utf-8'))
            
            os.chdir(pathout)
            with open(str(f)[:-3]+"txt", "w") as text_file:
                text_file.write(wordstring)
                
if __name__ == "__main__":
    year = "2017"

    convert_pdf_to_txt(year)


