#Testing interpreting arguments
import sys, getopt, argparse

parser = argparse.ArgumentParser(description='A tool to interpret REP files')

parser.add_argument('-v','--version', help='get the price version of the REP file', action="store_true")
parser.add_argument('filename', help='The name of the REP file to be parsed', type = str)

args = parser.parse_args()

if args.version:
    print ('The name of the file is ' + args.filename + '\n')