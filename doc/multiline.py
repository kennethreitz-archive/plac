import sys
from plac_ext import Process

if __name__ == '__main__':
    proc = Process(['ishelve2.py', '-c', '~/conf.shelve'])
    while True:
        multiline = ' '.join(iter(sys.stdin.readline, 'END\n'))
        if not multiline:
            break
        print proc.send(multiline)
