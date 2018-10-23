def fibo(n):
    a,b=0,1
    print(a,end=" , ")
    for u in range(n):
        #another case is disussed here
     
      print(b,end=" , ")
      a,b=b,a+b
    print(" . . . . . . . ")
n=int(input("Enter the number : "))
fibo(n)
