-------------
# 描述      #
-------------
<li><a href="README.md">English</a></li>
将某个pdf的任意页作为水印贴在另一个pdf的任意页上。

# 用法 #
	第一行是使用模板，后面为具体用例。

	$ python  addmark.py input.pdf output.pdf watermark.pdf (1,n|-1) (1,n|-1)
	$ python  addmark.py input.pdf output.pdf watermark.pdf 
	$ python  addmark.py input.pdf output.pdf watermark.pdf  1
	$ python  addmark.py input.pdf output.pdf watermark.pdf -1
	$ python  addmark.py input.pdf output.pdf watermark.pdf  1  1
	$ python  addmark.py input.pdf output.pdf watermark.pdf  1 -1
	$ python  addmark.py input.pdf output.pdf watermark.pdf -1 -1
	$ python  addmark.py input.pdf output.pdf watermark.pdf -1  1
	$ python  addmark.py input.pdf output.pdf watermark.pdf  2  1

# 注意 #
	两个(1,n|-1)分别指代每个pdf的页码，n是最后一页，-1也是最后一页(不知道总页数时使用)，这两个括号的参数默认为(1 1)
