#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 
#    Date: 2019/06/15
#    Survived: 2019/11/25
#    Author: Shieber
#
#                             APACHE LICENSE
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#
#                            Function Description
#    Touch a watermark onto a pdf file on its any page.
#
#    Copyright 2019 
#    All Rights Reserved!

import sys
import PyPDF2

class WaterMark():
    '''给pdf加上水印'''
    def __init__(self,inputfl,outputfl,watermark,pagei,pagew):
        self.origin = inputfl
        self.output = outputfl 
        self.mark   = watermark 
        self.pageo  = pagei
        self.pagew  = pagew

    def getfixedPage(self,filename,page):
        '''提取pdf指定的某一页内容'''
        if not filename.endswith('.pdf'):
            sys.exit(-1)

        pdfObj    = open(filename,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfObj)
        fixedpage = pdfReader.getPage(page)
        return pdfObj, fixedpage

    def markedPdf(self,markedpage):
        '''形成最终加了水印的pdf'''
        pdfObj    = open(self.origin,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfObj)
        if (not 1 <= self.pageo <= pdfReader.numPages) and (self.pageo != -1):
            pdfObj.close() #若页数不在范围内就关闭文件并退出
            return None

        pdfWriter = PyPDF2.PdfFileWriter()
        if self.pageo == 1:
            #为第一页添加水印的情况
            pdfWriter.addPage(markedpage)
            for pageNum in range(1,pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)
        elif (self.pageo == -1) or (self.pageo == pdfReader.numPages):
            #为最后一页添加水印的情况
            for pageNum in range(pdfReader.numPages-1):
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)
            pdfWriter.addPage(markedpage)
        elif 1 < self.pageo < pdfReader.numPages:
            #为中间某页添加水印的情况
            for pageNum in range(self.pageo-1):
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)
            pdfWriter.addPage(markedpage)
            for pageNum in range(self.pageo,pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNum)
                pdfWriter.addPage(pageObj)
        else:
            pass

        outputObj = open(self.output,'wb')
        pdfWriter.write(outputObj)
        outputObj.close()
        pdfObj.close() 

    def finalmerge(self):
        if self.pageo == -1:
            fixedObj, fixedpage  = self.getfixedPage(self.origin,self.pageo)
        else:
            fixedObj, fixedpage  = self.getfixedPage(self.origin,self.pageo-1)

        if self.pagew == -1:
            markObj,  markpage   = self.getfixedPage(self.mark,self.pagew)
        else:
            markObj,  markpage   = self.getfixedPage(self.mark,self.pagew-1)

        fixedpage.mergePage(markpage)
        self.markedPdf(fixedpage)

        fixedObj.close()
        markObj.close()

if __name__ == "__main__":
    argv = sys.argv
    if len(argv) == 4:
        pagei,pagew = 1,1
    elif len(argv) == 5:
        pagei,pagew = int(argv[4]),1
    elif len(argv) == 6:
        pagei,pagew = int(argv[4]),int(argv[5])
    else:
        print('Usage: python addmark.py file.pdf output.pdf mark.pdf (1,n|-1) (1,n|-1)')
        sys.exit(-1)

    Input  = argv[1]
    Output = argv[2]
    Mark_pdf = argv[3]
    watermark = WaterMark(Input, Output, Mark_pdf, pagei,pagew)
    watermark.finalmerge()
