import sys
import os

g_cnt = 0

def md2pdf(src_name):
    dst_name = '"' + src_name.replace('.md', '.pdf') + '"'
    src_name = '"' + src_name + '"'
    cmd = 'pandoc.exe -N -s --toc --pdf-engine=xelatex -o {} --template=template.tex {}'.format(dst_name, src_name)
    print(cmd)
    os.system(cmd)
    print('finish transformation of {}\n'.format(dst_name))
    return cmd

def md2docx(src_name):
    dst_name = '"' + src_name.replace('.md', '.docx') + '"'
    src_name = '"' + src_name + '"'
    cmd = 'pandoc -N -s --toc -o {} {}'.format(dst_name, src_name)
    print(cmd)
    os.system(cmd)
    print('finish transformation of {}\n'.format(dst_name))
    return cmd


def batchTrans(path, targetType = None):
    global g_cnt
    if targetType == None:
        print('You should specify a target file type\n')
    elif os.path.isdir(path):
        fileList = os.listdir(path)
        for one in fileList:
            batchTrans(path + '\\' + one, targetType)
    elif path.split('.')[-1] == 'md':
        g_cnt = g_cnt + 1
        if targetType == 'pdf':
            md2pdf(path)
        elif targetType == 'docx':
            md2docx(path)
    else:
        print('Error file type\n')


if __name__ == "__main__":
    argc = len(sys.argv)
    if argc == 2 and sys.argv[1] != '-t':
        print('Usage: batch.py [-option] [option value] [source file]\n')
        print('\t\t-h for help, see the usage\n')
        print('\t\t-t for target, specify target file type [pdf|docx|...todo]\n')

    elif argc == 4 and (sys.argv[1] == '-t' or sys.argv[1] == '--target'):
        batchTrans(sys.argv[3], sys.argv[2])
        fileStr = 'file' if g_cnt <= 1 else 'files'
        print('Finish transformation of %d %s\n' %(g_cnt, fileStr))


    