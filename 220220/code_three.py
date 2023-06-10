def neonew_game(lower,upper):

    if(lower<upper):
        for i in range(lower,upper+1):
            str = ""
            if(i%3==0):
                str="=NEO"
                if(i%5==0):
                    str=str+"NEW"
            elif(i%5==0):
                str="=NEW"
            print(i, str)
    else:
        print("Value of lower limit should be less than that of upper limit")



lower=int(input("Enter lower limit of range"))
upper=int(input("Enter upper limit of range"))
neonew_game(lower,upper)