### Description 

[[中文版](./README_CN.md)] Add a watermark from one pdf onto anthor pdf file. 

### Compatible OS 
- Linux 
- Mac OS
- Windows

### Dependency
- click  
- PyPDF2 

### Usage 
First line is the usage template，later are examples.

	### python  addmark.py input.pdf output.pdf watermark.pdf (1,n|-1) (1,n|-1)
	$ python  addmark.py input.pdf output.pdf watermark.pdf 
	$ python  addmark.py input.pdf output.pdf watermark.pdf  1
	$ python  addmark.py input.pdf output.pdf watermark.pdf -1
	$ python  addmark.py input.pdf output.pdf watermark.pdf  1  1
	$ python  addmark.py input.pdf output.pdf watermark.pdf  1 -1
	$ python  addmark.py input.pdf output.pdf watermark.pdf -1 -1
	$ python  addmark.py input.pdf output.pdf watermark.pdf -1  1
	$ python  addmark.py input.pdf output.pdf watermark.pdf  2  1
	$ python  addmark.py input.pdf output.pdf watermark.pdf  2  2
	$ python  addmark.py input.pdf output.pdf watermark.pdf -2 -2

	### python  addmark.py input.pdf output.pdf watermark.pdf (a|all) (1,n|-1)
	$ python  addmark.py input.pdf output.pdf watermark.pdf  a 
	$ python  addmark.py input.pdf output.pdf watermark.pdf  a  1
	$ python  addmark.py input.pdf output.pdf watermark.pdf  a -1
	$ python  addmark.py input.pdf output.pdf watermark.pdf  -a 
	$ python  addmark.py input.pdf output.pdf watermark.pdf  -a  1
	$ python  addmark.py input.pdf output.pdf watermark.pdf  -a -1
	$ python  addmark.py input.pdf output.pdf watermark.pdf  all 
	$ python  addmark.py input.pdf output.pdf watermark.pdf  all  1
	$ python  addmark.py input.pdf output.pdf watermark.pdf  all -1
	$ python  addmark.py input.pdf output.pdf watermark.pdf  --all 
	$ python  addmark.py input.pdf output.pdf watermark.pdf  --all 1
	$ python  addmark.py input.pdf output.pdf watermark.pdf  --all -1
    # a or all parameter means to add watermark onto every page.

### Change Log
- 2020.07.23 Modify: Use click to parse parameters
- 2020.01.29 New Feature：add watermark page onto all pdf pages
- 2019.06.15 Add watermark onto one selected page

### Note 
- The version of Python is 3, and the PyPDF2 and click pacakage is required. 
- the options (1,n|-1) are optional, which specify the page number of pdf files. 
- a all -a -all --all are options for watermarking all pdf pages. 
- and n is your specified page number, -1 is the last page in case of you don't know how many pages the pdf file have. 
