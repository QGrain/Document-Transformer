import sys
import os

def md2pdf(src_name, dst_name):
    cmd = 'pandoc -N -s --toc --pdf-engine=xelatex -o {}.pdf --template=template.tex {}'.format(dst_name, src_name)
    return cmd

def md2docx(src_name, dst_name):
    cmd = 'pandoc -N -s --toc -o {}.docx {}'.format(dst_name, src_name)
    return cmd


def batchTrans(path):
    if os.path.isdir(path):
        
    pass

if __name__ == "__main__":
    argc = len(sys.argv)
    
    if sys.argv[1] == '-h' or sys.argv[1] == '--help' or sys.argv[1] == '/h':
        print('Usage: batch.py [-option] [option value] [source file]\n')
        print('-h for help, see the usage\n')
        print('-t for target, specify target file type [pdf|docx|...todo]\n')

    elif argc == 4 and (sys.argv[1] == '-t' or sys.argv[1] == '--target'):
        if sys.argv[3]:
            src_name = sys.argv[3].split('/')[-1]
            dst_name = src_name.split('.')[0]

        if sys.argv[2] == 'pdf':
            os.system(md2pdf(src_name, dst_name))
        elif sys.argv[2] == 'docx':
            os.system(md2docx(src_name, dst_name))

    