# -*- coding: utf-8 -*- 
import os 
import os.path as path

toc = []

def main ():
    # recurMD(os.getcwd(), 1, "", 1)
    nonRecurs(os.getcwd(), toc)
    with open('README.md', 'wt') as f:
        for one in toc: 
            one = one.replace("\\", "/") # github 的路径用 / 分隔
            f.write(one + "\n")
            print(one)
            
    # toc.append("myNotes")
    # toc.append("---")
    
    pass


# str, int, str, int
def recurMD(baseDir, level, parentOrder, subOrder):
# def recurMD(toc, baseDir, level):
    relPath = ""
    link = ""
    
    if level > 1: 
        # relPath = path.basename(baseDir) # get folder name
        # relPath = path.split(baseDir)[-1]
        # relPath = baseDir.split("\\")[-1]
        
        parentOrder += "." + str(subOrder)
        
        relPath = "#" * level
        relPath += " " + parentOrder
        relPath += " " + path.basename(baseDir) # get folder name

        toc.append(relPath)
        # relPath = path.relpath(baseDir)
        # toc.append("#" * level + " " + str(level) + " " + relPath)

    nodeList = os.listdir(baseDir)
    forwardDir = []
    for aNode in nodeList: 
        fullPath = path.join(baseDir, aNode)
        if path.isfile(fullPath):
            relPath = path.relpath(fullPath)
            link = "- [" + aNode + "]" + \
                "(" + relPath +")"
            toc.append(link)
        elif aNode == ".git": 
            continue
        else : 
            forwardDir.append(fullPath)
    
    _subOrder = 1
    for aDir in forwardDir: 
        recurMD(aDir, level+1, parentOrder, _subOrder)
        _subOrder += 1
    return

def nonRecurs(baseDir, _toc):
    # str dir, int level, str parentOrder, int _subOrder
    stack = []
    
    level = 2
    parentOrder = ""
    
    nodeList = os.listdir(baseDir)
    forwardDir = []
    # 遍历这个目录
    for aNode in nodeList: 
        fullPath = path.join(baseDir, aNode)
        if path.isfile(fullPath): 
            relPath = path.relpath(fullPath)
            link = "- [" + aNode + "]" + \
                "(" + relPath +")"
            _toc.append(link)
        elif aNode == ".git": 
            continue
        else : 
            forwardDir.append(fullPath)
    _subOrder = len(forwardDir)
    for aDir in reversed(forwardDir):
        stack.append([aDir, level, "", _subOrder])
        _subOrder -= 1
    
    
    while len(stack) > 0: 
        baseDir, level, parentOrder, _subOrder = stack.pop()

        # 构造 header
        if level > 2: 
            thisOrder = parentOrder + "." + str(_subOrder)
        else :
            thisOrder = str(_subOrder)
        header = "#" * level
        header += " " + thisOrder
        header += " " + path.basename(baseDir)
        # 放入目录
        _toc.append(header)
        
        nodeList = os.listdir(baseDir)
        forwardDir = []
        # 遍历这个目录
        for aNode in nodeList: 
            fullPath = path.join(baseDir, aNode)
            if path.isfile(fullPath): 
                relPath = path.relpath(fullPath)
                link = "- [" + aNode + "]" + \
                    "(" + relPath +")"
                _toc.append(link)
            else : 
                forwardDir.append(fullPath)
        _subOrder = len(forwardDir)
        # 反字母序压栈
        for aDir in reversed(forwardDir):
            stack.append([aDir, level+1, thisOrder, _subOrder])
            _subOrder -= 1
        continue 
    # end while len(stack) > 0
    return

# def file_name(file_dir):   
    # for root, dirs, files in os.walk(file_dir):  
        # print(root) #当前目录路径
        # print(files) #当前路径下所有非目录子文件
        # print(dirs) #当前路径下所有子目录
        # print()
    # return

# 相对路径
def testRelpath(file): 
    ppp = os.path.relpath(file) # 相对.py 的路径
    print(ppp)
    return

if __name__=="__main__":
    main()

# 先序遍历
# <http://blog.csdn.net/hyperbolechi/article/details/42913061>
# python3-cookbook
# <http://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p01_read_write_text_data.html>