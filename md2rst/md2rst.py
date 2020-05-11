import os
import sys
import requests

def md2rst_via_web(src_file, dst_file):
    response = requests.post(
        url='http://c.docverter.com/convert',
        data={'to': 'rst', 'from': 'markdown'},
        files={'input_files[]': open(src_file, 'rb')}
    )

    print(response)

    if response.ok:
        with open(dst_file, "wb") as f:
            f.write(response.content)

def md2rst_via_pandoc(src_file, dst_file):
    cmd = "pandoc --from=markdown --to=rst --output=" + dst_file + " " + src_file
    try:
        os.system(cmd)
    except:
        sys.stderr.write("Error with transformation!")
        sys.exit(1)

def main(argv):
    md2rst_via_pandoc(src_file = argv[1], dst_file = argv[2])

if __name__ == '__main__':
    main(sys.argv)
    