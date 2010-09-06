import time
import plac

class Importer(object):
    "A fake importer with an import_file command"
    thcommands = ['import_file']
    def __init__(self, dsn):
        self.dsn = dsn
    def import_file(self, fname):
        "Import a file into the database"
        for n in range(10000):
            time.sleep(.01)
            if n % 100 == 99:
                yield 'Imported %d lines' % (n+1)
            yield

if __name__ == '__main__':
    plac.Interpreter.plac.call(Importer)
