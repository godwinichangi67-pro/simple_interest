def sim_int(principle,interest,time):
    return (principle*interest*time)/100

if __name__=="__main__":
    p=int(input("Enter principal amount"))
    i=int(input("Enter interest"))
    t=int(input("Enter time"))
    print("Simple Interest:", sim_int(p,i,t))