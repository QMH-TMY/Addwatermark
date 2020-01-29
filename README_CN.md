### 兼容系统 
- Linux 
- Mac OS
- Windows

### 描述      
[[English](./README.md)] 将某个pdf的任意页作为水印贴在另一个pdf的任意页上。

### 用法 
	###行是使用方法，后面为具体用例。

	### python  addmark.py input.pdf output.pdf watermark.pdf (1,n|-n,-1) (1,n|-n,-1)
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
	$ python  addmark.py input.pdf output.pdf watermark.pdf  a -1
	$ python  addmark.py input.pdf output.pdf watermark.pdf  -a 
	$ python  addmark.py input.pdf output.pdf watermark.pdf  -a -1
	$ python  addmark.py input.pdf output.pdf watermark.pdf  -all 
	$ python  addmark.py input.pdf output.pdf watermark.pdf  -all -1
	$ python  addmark.py input.pdf output.pdf watermark.pdf  --all 
	$ python  addmark.py input.pdf output.pdf watermark.pdf  --all -1
	$ python  addmark.py input.pdf output.pdf watermark.pdf  --all -3

### 日志 
- 2020.01.29 新功能：对所有页添加水印
- 2019.06.15 首次实现对指定pdf页添加水印

### 注意 
- Python版本为3   
- 两个(1,n|-n,-1)分别指代原始pdf和水印pdf的页码，n是指定的某页  
- -n,-1是逆序，-1就是最后一页(不知道总页数时使用)  
- 未指定参数时，两括号内的参数默认为1 1，请确定两个pdf的页码范围正确  
- 第一个页码参数为-a -all --all a all时将为整个pdf添加你指定的水印  
