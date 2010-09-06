import threading, Queue, time, random, Tkinter
import plac

queue = Queue.Queue()

def make_target(i):
    def thunk():
        time.sleep(random.random())
        queue.put(str(i))
    return thunk

def launch_threads(n):
    for i in range(n):
        th = threading.Thread(target=make_target(i))
        th.start()
        yield th

class ThreadContext(object):
    def __init__(self, func, *args, **kw):
        self.thread = threading.Thread(None, func, args=args, kwargs=kw)
    def __enter__(self):
        self.thread.start()
        return self
    def __exit__(self, etype, exc, tb):
        self.thread.join()

def interpret_queue(interpreter, queue):
    with interpreter:
        for value in iter(queue.get, 'exit'):
            print(interpreter.send(value))

if __name__ == '__main__':
    thlist = list(launch_threads(10))
    i = plac.Interpreter(lambda x: x)
    root = Tkinter.Tk()
    threading.Timer(3, lambda : [queue.put('exit'), root.quit()]).start()
    with ThreadContext(interpret_queue, i, queue):
        root.mainloop()
    for th in thlist:
        th.join()
