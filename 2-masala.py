with open ("1f.txt","r") as f1:
    with open ("2f.txt","r") as f2:
        t1=f1.read()
        t2=f2.read()
        l2=list(t2.split("\n"))
        b=0
        for i in list(t1.split("\n")):
            print(f"{i}-{l2[b]}")
            b+=1
