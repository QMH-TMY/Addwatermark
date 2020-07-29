#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 
# Date: 2019/06/15
# Modified: 2020/03/13
# Modified: 2020/07/23
# Author: Shieber
# Touch a watermark onto any page of a pdf file.

import sys
import click
import PyPDF2

class AddWaterMark():
    """命令行水印添加"""
    def __init__(self, argv, page2mk, wmkpage):
        self.input  = argv[1]    #src pdf 输入pdf
        self.output = argv[2]    #out pdf 输出pdf
        self.wtmark = argv[3]    #wmmark pdf 水印pdf
        self.page2mk = page2mk    #page to add mark 要加水印的pdf页码
        self.wmkpage = wmkpage    #page of mark pdf 水印pdf中水印页码
        self._detect_file_type()

    #检测文件是否是Pdf
    def _detect_file_type(self):
        if not self.input.endswith('.pdf'):
            print("Invalid input file type: must end with .pdf")
            sys.exit(-1)
        if not self.output.endswith('.pdf'):
            print("Invalid output file type: must end with .pdf")
            sys.exit(-1)

    #提取pdf指定的某一页内容
    def _get_page(self, filename, pagenumber):
        pdfobj = open(filename, 'rb')
        pdfRdr = PyPDF2.PdfFileReader(pdfobj)
        pdfPg  = pdfRdr.getPage(pagenumber)
        return pdfobj, pdfPg

    #对所有页添加水印
    def _mark_all_page(self, wmkpage):
        with open(self.input,'rb') as pdfobj1:
            pdfRdr = PyPDF2.PdfFileReader(pdfobj1)
            pdfWtr = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfRdr.numPages):
                pdfPg = pdfRdr.getPage(pageNum)
                pdfPg.mergePage(wmkpage)
                pdfWtr.addPage(pdfPg)

            with open(self.output,'wb') as pdfobj2:
                pdfWtr.write(pdfobj2)
            
    #对某一页添加水印
    def _mark_pdf(self,wmkpage):
        with open(self.input,'rb') as pdfobj1:
            pdfRdr = PyPDF2.PdfFileReader(pdfobj1)
            maxPg  = pdfRdr.numPages

            if (not 1 <= abs(self.page2mk) <= maxPg):   #判断是否超页
                print("pdf page number exceeded")
                sys.exit(-1)

            if self.page2mk <= 0:
                pdfobj2, mkdPg = self.get_page(self.input, self.page2mk)
            else:
                pdfobj2, mkdPg = self.get_page(self.input, self.page2mk - 1)

            mkdPg.mergePage(wmkpage)     #得到加了水印的pdf页

            pdfWtr = PyPDF2.PdfFileWriter()
            if (self.page2mk == 1) or (self.page2mk == 0) or (self.page2mk == -maxPg):
                pdfWtr.addPage(mkdPg) #为第一页添加水印的情况
                for pageNum in range(1,maxPg):
                    pdfPg = pdfRdr.getPage(pageNum)
                    pdfWtr.addPage(pdfPg)
            elif 1 < self.page2mk < maxPg:  
                for pageNum in range(self.page2mk-1):
                    pdfPg = pdfRdr.getPage(pageNum)
                    pdfWtr.addPage(pdfPg)
                pdfWtr.addPage(mkdPg) #为中间某页添加水印的情况
                for pageNum in range(self.page2mk, maxPg):
                    pdfPg = pdfRdr.getPage(pageNum)
                    pdfWtr.addPage(pdfPg)
            elif -maxPg < self.page2mk < -1:  
                for pageNum in range(maxPg + self.page2mk):
                    pdfPg = pdfRdr.getPage(pageNum)
                    pdfWtr.addPage(pdfPg)
                pdfWtr.addPage(mkdPg) #为中间某页添加水印的情况
                for pageNum in range(maxPg + self.page2mk + 1, maxPg):
                    pdfPg = pdfRdr.getPage(pageNum)
                    pdfWtr.addPage(pdfPg)
            elif (self.page2mk == maxPg) or (self.page2mk == -1): 
                for pageNum in range(maxPg - 1):
                    pdfPg = pdfRdr.getPage(pageNum)
                    pdfWtr.addPage(pdfPg)
                pdfWtr.addPage(mkdPg) #为最后一页添加水印的情况

            with open(self.output,'wb') as pdfobj3:
                pdfWtr.write(pdfobj3)
                pdfobj2.close()

    def add(self):
        #1.获取水印页
        if self.wmkpage <= 0:
            pdfobj, wmkpage = self._get_page(self.wtmark, self.wmkpage)
        else:
            pdfobj, wmkpage = self._get_page(self.wtmark, self.wmkpage-1)

        #2.给某(或所有)页添加水印
        if self.page2mk != 'all':
            self._mark_pdf(wmkpage)
        else:
            self._mark_all_page(wmkpage)

        pdfobj.close()

@click.command()
@click.option('--page2mk', default='1', help='pdf page number onto which add a watermark')
@click.option('--wmkpage', default='1', help='watermark page number you want to use')
def parse_parameters(page2mk, wmkpage):
    """
       Usage:\n
       Addmark input.pdf output.pdf watermark.pdf [page2mk] [wmkpage]
       page2mk和wmkpage为input.pdf和watermark.pdf的页码，默认为1，1。
       可以使用1,n和-1,-n两种方式指代页码，-1代表最后一页
       若page2mk为a, all, -a, -all, --all，则对pdf每一页添加wmkpage指定页的水印。
     """

    argvlen = len(sys.argv)
    if argvlen == 4:
        pagewmk, wmkpage = int(page2mk), int(wmkpage)
    elif argvlen == 5:
        if page2mk.replace('-','').isdigit(): 
            page2mk, wmkpage = int(page2mk), int(wmkpage)
        else:
            page2mk, wmkpage = 'all', int(wmkpage)
    elif argvlen == 6:
        if page2mk.replace('-','').isdigit(): 
            page2mk, wmkpage = int(page2mk), int(wmkpage)
        else:
            page2mk, wmkpage = 'all', int(wmkpage)
    else:
        sys.exit(-1)

    return page2mk, wmkpage

if __name__ == "__main__":
    page2mk, wmkpage = parse_parameters()
    addwtmk = AddWaterMark(sys.argv, page2mk, wmkpage)
    addwtmk.add() 
