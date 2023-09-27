import os
import sys

def invert(line):
    return line[::-1]

def main():
    if len(sys.argv) != 3 or sys.argv[1] != "-f":
        print("Use: {} -f archive.txt".format(sys.argv[0]))
        sys.exit(1)
    archive=sys.argv[2]
    with open(archive, "r") as f:
        lines=f.readlines()
    pipes=[]

    for line in lines:
        r, w=os.pipe()
        pipes.append((r, w))
        pid=os.fork()
        if pid == 0:
            os.close(r)
            w=os.fdopen(w, "w")
            w.write(invert(line))
            w.close()
            sys.exit(0)
        else:
            os.close(w)
    for r, _ in pipes:
        r=os.fdopen(r)
        print(r.read().strip())
        r.close()

if __name__=="__main__":
    main()