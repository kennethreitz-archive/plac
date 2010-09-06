# example10.py
import plac

@plac.annotations(
operator=("The name of an operator", 'positional', None, str, ['add', 'mul']),
numbers=("A number", 'positional', None, float, None, "n"))
def main(operator, *numbers):
    "A script to add and multiply numbers"
    if operator == 'mul':
        op = float.__mul__
        result = 1.0
    else: # operator == 'add'
        op = float.__add__
        result = 0.0
    for n in numbers:
        result = op(result, n)
    return result

if __name__ == '__main__':
    print(plac.call(main))
