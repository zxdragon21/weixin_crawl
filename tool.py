import os,glob2,re
import shutil
import subprocess as sp
file=r'D:\crawl\weixin_crawl\output\artilist.txt'
path=r'D:\crawl\weixin_crawl\output\new'
with open(file,'r',encoding='utf-8') as f:
    file_list = f.readlines()

pdf_list = glob2.glob(r'D:\crawl\weixin_crawl\output\tuolesi\*.pdf')
import pdb
#pdb.set_trace()
assert len(pdf_list) >= len(file_list)

intab = r'[?*/\|><]'
for i in range(len(pdf_list)):
    out = os.path.join(path,file_list[i])[:-1] + ".pdf"
    import pdb
    pdb.set_trace()
    final = re.sub(intab, "", out)
    final = ''.join([i.strip(' ') for i in final])
    #pdb.set_trace()
    shutil.copy(pdf_list[i],final)
    print(f"第{i}个，{final} copied!\n")
