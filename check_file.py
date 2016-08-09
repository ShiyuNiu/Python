# -*- encoding:utf-8 -*-
# 脚本名称	: check_file.py
# 原作者		: Craig Richards
# 创建日期		: 20 May 2013 
# 最后修改	: Shiyu
# 版本		: 2.0

# Modifications	: 将原Python2.7版本移植为Python3.5版本

# Description	: 读文件，相当于cat

import sys		# Import the Modules
import os		# Import the Modules

# readfile方法会读文件

def readfile(filename):
	with open(filename, mode='r', encoding='utf-8') as f:      # Ensure file is correctly closed under all circumstances
	    content = f.read()
	print(content)

def main():
  if len(sys.argv) == 2:		# 检查参数，当参数等于2时(第一个参数是脚本自身的名称)
    filename = sys.argv[1]		# 第二个参数表示文件名
    if not os.path.isfile(filename):	# 检查文件是否存在
      print('[-] ' + filename + ' does not exist.')
      exit(0)
    if not os.access(filename, os.R_OK):	# 检查你是否有读文件的权限
      print('[-] ' + filename + ' access denied')
      exit(0)
  else:
    print('[-] Usage: ' + str(sys.argv[0]) + ' <filename>') # 如果没有文件参数，提示脚本用法
    exit(0)
  print('[+] Reading from : ' + filename)	# 显示消息，读出文本
  readfile(filename)
  
if __name__ == '__main__':
  main()
