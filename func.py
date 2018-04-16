import json
from urllib.request import urlopen
import os,shutil


#copy/movefile-----------------------------------------------------------------
def movefile(srcfile,dstfile):
    if not os.path.isfile(srcfile):
        print("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.move(srcfile,dstfile)          #移动文件
        print("move successful \n%s -> %s"%( srcfile,dstfile))

def copyfile(srcfile,Topic):
    dstfile='./classification/'+Topic+'/'+srcfile
    if not os.path.isfile(srcfile):
        print("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(dstfile)    #分离文件名和路径
        if not os.path.exists(fpath):
            os.makedirs(fpath)                #创建路径
        shutil.copyfile(srcfile,dstfile)      #复制文件
        print("copy successful \n%s -> %s"%( srcfile,dstfile))

#------------------------------------------------------------------------------
def filter(i):
    for a in ["the","a","an","to","of"]:
        if a in i:
            return False
    return True

def beautiful_keyword(Keyword):
    print("\nUni-gram:")
    uni_gram={}
    for i in Keyword.get("1"):
        if Keyword.get("1").get(i)>3 and filter(i):
            uni_gram[i]=Keyword.get("1").get(i)
    for elem in sorted(uni_gram.items(),key=lambda item:item[1],reverse=True):
        print("\t"+str(elem))

    print("\nBi-gram:")
    bi_gram={}
    for i in Keyword.get("2"):
        if Keyword.get("2").get(i)>1 and "the" not in i and "of" not in i:
            bi_gram[i]=Keyword.get("2").get(i)
    for elem in sorted(bi_gram.items(),key=lambda item:item[1],reverse=True):
        print("\t"+str(elem))

    print("\nTri-gram:")
    tri_gram={}
    for i in Keyword.get("3"):
        if Keyword.get("3").get(i)>1 and "the" not in i:
            tri_gram[i]=Keyword.get("3").get(i)
    for elem in sorted(tri_gram.items(),key=lambda item:item[1],reverse=True):
        print("\t"+str(elem))
