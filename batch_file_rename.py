# -*- encoding:utf-8 -*-
# batch_file_rename.py
# Created: 6th August 2012

'''
批量修改文件后缀名
'''

__author__ = 'Craig Richards'
__version__ = '1.0'

import os
import sys


def batch_rename(work_dir, old_ext, new_ext):
    for filename in os.listdir(work_dir):
        # 得到文件扩展名
        file_ext = os.path.splitext(filename)[1]
        # 根据old_ext(我们希望修改的)得到期望修改后缀名的文件
        if old_ext == file_ext:
            # 更改后缀名拼接为新的文件名
            newfile = filename.replace(old_ext, new_ext)
            # 使用rename重命名
            os.rename(
              os.path.join(work_dir, filename),
              os.path.join(work_dir, newfile)
            )

def main():
    work_dir = sys.argv[1]
    old_ext = sys.argv[2]
    new_ext = sys.argv[3]
    batch_rename(work_dir, old_ext, new_ext)

if __name__ == '__main__':
    main()