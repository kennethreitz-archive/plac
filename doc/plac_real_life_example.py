# literal translation from http://groups.google.com/group/comp.lang.python/msg/de7c188e705f8eb2?hl=en
# parser = optparse.OptionParser("usage: %lines [options] arg1") 
#     parser.add_option("-l", "--lines", dest="lines", 
#                       default=10, type="int", 
#                       help="number of lines") 
#     parser.add_option("-t", "--topbottom", dest="topbottom", 
#                       default="T", type="str", 
#                       help="T(op) or B(ottom)") 
#     (options, args) = parser.parse_args() 
#     if len(args) != 1: 
#         parser.error("incorrect number of arguments") 
#     lines=options.lines 
#     tb=options.topbottom 

import plac

@plac.annotations(
    lines=('number of lines', 'option', 'l', int),
    topbottom=('T(op) or B(ottom)', 'option', 't', str, 'TB'))
def main(arg, lines=10, topbottom='T'):
    print arg, lines, topbottom

if __name__ == '__main__':
    plac.call(main)
