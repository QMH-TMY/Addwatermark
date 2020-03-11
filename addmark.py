#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 
#Date: 2019/06/15
#Survived: 2019/11/25
#Modified: 2020/01/29
#Author: Shieber
#Touch a watermark onto any page of a pdf file.
#

import sys
import PyPDF2

class AddWaterMark():
    def __init__(self, argv, pageIpt, pageWmk):
        self.input  = argv[1]    #src pdf 原始pdf
        self.output = argv[2]    #out pdf 输出pdf
        self.wtmark = argv[3]    #mark pdf 水印pdf
        self.pageOg = pageIpt    #page to add mark 要加水印的pdf页码
        self.pageWm = pageWmk    #page of mark pdf 水印pdf中水印页码
        self.detectFileType()

    def detectFileType(self):
        #检测文件是否是Pdf
        if not self.input.endswith('.pdf'):
            print("Invalid input file type: must end with .pdf")
            sys.exit(-1)
        if not self.output.endswith('.pdf'):
            print("Invalid output file type: must end with .pdf")
            sys.exit(-1)

    def getPage(self, flName, pageNum):
        #提取pdf指定的某一页内容
        pdfObj = open(flName, 'rb')
        pdfRdr = PyPDF2.PdfFileReader(pdfObj)
        pdfPg  = pdfRdr.getPage(pageNum)
        return pdfObj, pdfPg

    def markAllPdf(self, wtmkPg):
        #对所有页添加水印
        with open(self.input,'rb') as pdfObj1:
            pdfRdr = PyPDF2.PdfFileReader(pdfObj1)
            pdfWtr = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfRdr.numPages):
                pdfPg = pdfRdr.getPage(pageNum)
                pdfPg.mergePage(wtmkPg)
                pdfWtr.addPage(pdfPg)

            with open(self.output,'wb') as pdfObj2:
                pdfWtr.write(pdfObj2)
            
    def markPdf(self,wtmkPg):
        #对某一页添加水印
        pageOg = self.pageOg
        with open(self.input,'rb') as pdfObj1:
            pdfRdr = PyPDF2.PdfFileReader(pdfObj1)
            maxPg  = pdfRdr.numPages

            if (not 1 <= abs(pageOg) <= maxPg):   #判断是否超页
                print("pdf page number exceeded")
                sys.exit(-1)

            if pageOg <= 0:
                pdfObj2, mkdPg = self.getPage(self.input, pageOg)
            else:
                pdfObj2, mkdPg = self.getPage(self.input, pageOg - 1)

            mkdPg.mergePage(wtmkPg)     #得到加了水印的pdf页

            pdfWtr = PyPDF2.PdfFileWriter()
            if (pageOg == 1) or (pageOg == 0) or (pageOg == -maxPg):
                pdfWtr.addPage(mkdPg) #为第一页添加水印的情况
                for pageNum in range(1,maxPg):
                    pdfPg = pdfRdr.getPage(pageNum)
                    pdfWtr.addPage(pdfPg)
            elif 1 < pageOg < maxPg:  
                for pageNum in range(pageOg-1):
                    pdfPg = pdfRdr.getPage(pageNum)
                    pdfWtr.addPage(pdfPg)
                pdfWtr.addPage(mkdPg) #为中间某页添加水印的情况
                for pageNum in range(pageOg, maxPg):
                    pdfPg = pdfRdr.getPage(pageNum)
                    pdfWtr.addPage(pdfPg)
            elif -maxPg < pageOg < -1:  
                for pageNum in range(maxPg + pageOg):
                    pdfPg = pdfRdr.getPage(pageNum)
                    pdfWtr.addPage(pdfPg)
                pdfWtr.addPage(mkdPg) #为中间某页添加水印的情况
                for pageNum in range(maxPg + pageOg + 1, maxPg):
                    pdfPg = pdfRdr.getPage(pageNum)
                    pdfWtr.addPage(pdfPg)
            elif (pageOg == maxPg) or (pageOg == -1): 
                for pageNum in range(maxPg - 1):
                    pdfPg = pdfRdr.getPage(pageNum)
                    pdfWtr.addPage(pdfPg)
                pdfWtr.addPage(mkdPg) #为最后一页添加水印的情况

            with open(self.output,'wb') as pdfObj3:
                pdfWtr.write(pdfObj3)
                pdfObj2.close()

    def add(self):
        #1.获取水印页
        if self.pageWm <= 0:
            pdfObj, wtmkPg = self.getPage(self.wtmark, self.pageWm)
        else:
            pdfObj, wtmkPg = self.getPage(self.wtmark, self.pageWm-1)

        #2.给某(或所有)页添加水印
        if self.pageOg != 'all':
            self.markPdf(wtmkPg)
        else:
            self.markAllPdf(wtmkPg)

        pdfObj.close()

def parseParameters(argv):
    #解析命令行参数
    if   len(argv) == 4:
        pagei, pagew = 1, 1
    elif len(argv) == 5:
        if argv[4].replace('-','').isdigit(): 
            pagei, pagew = int(argv[4]), 1
        else:
            pagei, pagew = 'all', 1
    elif len(argv) == 6:
        if argv[4].replace('-','').isdigit(): 
            pagei, pagew = int(argv[4]), int(argv[5])
        else:
            pagei, pagew = 'all', int(argv[5])
    else:
        print('''Usage: 
        Addmark input.pdf output.pdf watermark.pdf (1,n|-n,-1)|('-a|a|-all') (1,n|-n,-1)
        [两个(1,n|-n,-1)为控制参数，可选项，分别是原始pdf和水印pdf的页码，默认为1,1。
         页码可以使用1,n的和-1,-n两种方式，不想数总页数时，-1代表最后一页，依次类推。
         若第一个控制参数为a, all, -a, -all, --all时，对原始pdf每一页添加水印。
        ]''')
        sys.exit(-1)

    return pagei, pagew 

if __name__ == "__main__":
    pgi,pgw = parseParameters(sys.argv)
    addwtmk = AddWaterMark(sys.argv, pgi, pgw)
    addwtmk.add() 
