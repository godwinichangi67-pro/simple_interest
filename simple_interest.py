import sys

def sim_int(principle,interest,time):
    return (principle*interest*time)/100

if __name__=="__main__":
    p=int(sys.argv[1])
    i=int(sys.argv[2])
    t=int(sys.argv[3])
    print("Simple Interest:", sim_int(p,i,t))
    print(sys.argv[0])