#commannd line utilities
#This is a way to pass the command line arguments

import argparse  #import this package for args, This is used for command line utolity
import sys
def calc(args):
    
    if args.output=="add":
        return args.value1+args.value2
    
    elif args.output=="sub":
        return args.value1-args.value2
    
    elif args.output=="mul":
        return args.value1*args.value2
    
    elif args.output=="div":
        return args.value1/args.value2
    
    else:
        return "OOPS something went wrong"

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--value1',type=float,default=1.0,help="please contact harry bhai")

    parser.add_argument('--value2',type=float,default=1.0,help="please contact harry bhai")

    parser.add_argument('--output',type=str,default="add",help="please contact harry bhai")
    args=parser.parse_args()
    sys.stdout.write(str(calc(args)))


#Similarly you can discover more on sys module 
#This is the way you can create your pyhton command line utilities



