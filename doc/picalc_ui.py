import time
from Tkinter import *
from threading import Thread
from picalculator import PiCalculator

def taskwidget(root, task, tick=500):
    "A Label widget showing the output of a task every 500 ms"
    sv = StringVar(root)
    lb = Label(root, textvariable=sv)
    def show_outlist():
        try:
            out = task.outlist[-1]
        except IndexError: # no output yet
            out = ''
        sv.set('%s %s' % (task, out))
        root.after(tick, show_outlist)
    root.after(0, show_outlist)
    return lb

def monitor(calculator):
    calculator.submit_tasks()
    th = Thread(target=calculator.run)
    th.start()
    root = Tk()
    try:
        for task in calculator.i.tasks():
            taskwidget(root, task).pack()
        root.mainloop()
    except KeyboardInterrupt:
        root.quit()
    finally:
        calculator.close()
        th.join()

if __name__ == '__main__':
    import plac; monitor(plac.call(PiCalculator))
