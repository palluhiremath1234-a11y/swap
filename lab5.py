import sys

def simInt(principal, interest, time):
    return (principal*interest*time)/100

if __name__ == "__main__":
    P = int(sys.argv[1])
    i = int(sys.argv[2])
    t = int(sys.argv[3])

    print("Simple interest: ",simInt(P,i,t))
    print("File name is ",sys.argv[0])