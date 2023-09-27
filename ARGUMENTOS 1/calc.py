import getopt
import sys
def error():
    print("La operacion no es valida")
    sys.exit(2)


def calculate(argv):
    valids=["+", "-", "*", "/"]
    operator=""
    num1=""
    num2=""
    opts=[]
    try:
        opts, args = getopt.getopt(argv, "o:n:m:")
    except Exception as e:
        print("Error:", e)
        sys.exit(2)
    for i, arg in opts:
        if i in ("-o", "--operator"):
            operator=arg
        elif i in ("-n", "--num1"):
            num1=arg
        elif i in ("-m", "--num2"):
            num2=arg

    if not operator or not num1 or not num2 or operator not in valids:
        error()
    else:
        try:
            num1=int(num1)
            num2=int(num2)
        except ValueError:
            error()
        if operator=="+":
            result=num1+num2
            print(num1, "+", num2, "= ", result)
        elif operator=="-":
            result=num1-num2
            print(num1, "-", num2, "= ", result)
        elif operator=="*":
            result=num1*num2
            print(num1, "*", num2, "= ", result)
        elif operator=="/":
            if num2==0:
                error()
            else:
                result=num1/num2
                print(num1, "/", num2, "= ", result)
        else:
            error()
            return None
if __name__ == "__main__":
    calculate(sys.argv[1:])
