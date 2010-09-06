class Main(object):
    commands = ['do']
    def do(self, x):
        pass

if __name__ == '__main__':
    import plac; plac.Interpreter.call(Main)
