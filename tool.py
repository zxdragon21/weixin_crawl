import os,glob2,re
import shutil
import subprocess as sp
file=r'D:\crawl\wxhub\output\save\artilist.txt'
path=r'D:\crawl\wxhub\output\new'
with open(file,'r',encoding='utf-8') as f:
    file_list = f.readlines()

pdf_list = glob2.glob(r'D:\crawl\wxhub\output\save\*.pdf')
assert len(pdf_list) == len(file_list)
import pdb

intab = r'[?*/\|><]'
for i in range(len(pdf_list)):
    out = os.path.join(path,file_list[i])[:-1]+".pdf"
    final = re.sub(intab, "", out)
    final = ''.join([i.strip(' ') for i in final])
    #pdb.set_trace()
    shutil.copy(pdf_list[i],final)
    print(f"{final} copied!\n")
