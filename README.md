-----------------
# Compatible OS #
-----------------
	Mac OS
	Windows
	Unix-like OS

-------------
# Description #
-------------

<li><a href="README_CN.md">中文版</a></li>

Add a watermark from one pdf onto anthor pdf file. 

# Usage #
Firs line is the standard，later are examples.

	# python  addmark.py input.pdf output.pdf watermark.pdf (1,n|-1) (1,n|-1)
	$ python  addmark.py input.pdf output.pdf watermark.pdf 
	$ python  addmark.py input.pdf output.pdf watermark.pdf  1
	$ python  addmark.py input.pdf output.pdf watermark.pdf -1
	$ python  addmark.py input.pdf output.pdf watermark.pdf  1  1
	$ python  addmark.py input.pdf output.pdf watermark.pdf  1 -1
	$ python  addmark.py input.pdf output.pdf watermark.pdf -1 -1
	$ python  addmark.py input.pdf output.pdf watermark.pdf -1  1
	$ python  addmark.py input.pdf output.pdf watermark.pdf  2  1

# Note #
	The version of Python is 2 or 3(recommended), and the PyPDF2 pacakage is required. 
	the two options (1,n|-1) are optional, which specify the page number of each pdf file. 
	and n is your specified page number, -1 is the last page in case of you don't know 
	how many pages the pdf file have. 
