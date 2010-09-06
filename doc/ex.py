import os, plac, ishelve2

try:
    fifo = os.mkfifo('/tmp/x')
except OSError: # fifo exists
    pass

if __name__ == '__main__':
    i = plac.Interpreter(ishelve2.main())
    i.execute(iter(open('/tmp/x').readline, ''), verbose=True)
