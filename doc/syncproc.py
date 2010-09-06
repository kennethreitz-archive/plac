from __future__ import with_statement
import plac, plac_ext

def main(*args):
    yield args

if __name__ == '__main__':
    proc = plac_ext.SyncProcess(['syncproc.py'])
    while True:
        inp = raw_input(proc.recv())
        proc.send(inp)
