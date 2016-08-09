# Python操作文件小技巧


os.listdir(dir)函数可以得到指定目录下所有文件(夹)名。
```
In [8]: os.listdir("d:/")
Out[8]:
['$RECYCLE.BIN',
 'Program Files',
 'public',
 'Shiyu.Niu',
 'System Volume Information']
```
os.path.splitext(filename)可以将指定文件的名字拆分为两部分：文件名和后缀名。
```
In [9]: os.path.splitext("/workspace/check_file.py")
Out[9]: ('/workspace/check_file', '.py')
```
os.rename(oldname, newname)可以将文件的老名称改为新名称。
```
# rename的参数是两个路径
os.rename(
	# 得到文件的绝对路径
	os.path.join(work_dir, oldname),
	os.path.join(work_dir, newname)
)
```
os.path.join(work_dir, filename)可以将两个参数合并为一个文件路径。
```
In [14]: os.path.join('d:/','/test')
Out[14]: 'd:/test'
```
os.path.isfile(filename)根据文件路径（绝对路径/相对路径）判断是否是一个文件（而非文件夹或根本不存在）
os.access(filename, os.R_OK)检查当前用户是否对文件有读权限