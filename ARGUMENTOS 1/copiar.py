import argparse
import os

parser= argparse.ArgumentParser()
parser.add_argument("-i", type=str, required=True)
parser.add_argument("-o", type=str, required=True)
args = parser.parse_args()

if os.path.exists(args.i):
    with open(args.i, "r") as f:
        content = f.read()
    with open(args.o, "w") as f:
        f.write(content)
else:
    print(f"El archivo {args.i} no existe.")