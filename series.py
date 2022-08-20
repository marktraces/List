#Function Defining

def sequences(a):
    if a == "Y":
        series = ["Fibonacci = Fib","Arithmetic Progression = AP", "Geometric Progression = GP", "Collatz Conjecture or Hailstone Series = Hstone"]
        print("Which of the following series would you like to operate in? \n")
        for i in range(0,len(series)):
            print(series[i].title())

def fibo(n):
    a = 1/(5**0.5)
    b = (1 + 5**0.5)
    c = (1 - 5**0.5)
    for n in range(1,(n+1)):
         fib = int(a * (b**n - c**n)/2**n)
         print(str(n) + ". " + str(fib))

def arith(a,b,n):
    d = (b - a)
    for n in range(1,(n+1)):
         e = (n - 1)
         AP = a + e*d
         print(str(n) + ". " + str(AP))

def geo(a,b,n):
     r = (b/a)
     for n in range(1,(n+1)):
         e = (n - 1)
         GP = a * (r**e)
         print(str(n) + ". " + str(GP))

def collatz(n):
    print(f"The collatz conjecture of {n} is given below :")
    print(float(n))
    while n != 1 :
        if n%2 == 0:
            n = float(n/2)
            print (f"{n}")
        elif n%2 != 0:
            n = float(3*n + 1)
            print (f"{n}")
    

#Actual Beginning Of The Program

print("Let's commence our program")
yorn = input("Would you like to begin? Y/N: \n --> \t")
while yorn.title() == "Y":
      sequences(yorn)
      seq = input("Which of the above would you like to select :  \n --> \t")
      if seq.title() == "Fib":
         n = int(input("Till which term of the series would you like to display: \n --> \t"))
         fibo(n)
      elif seq.title() == "Ap":
         a = float(input("What is the first term of your series: \n --> \t"))
         b = float(input("What is the second term of your series: \n --> \t"))
         n = int(input("Till which term of the series would you like to display: \n --> \t"))
         arith(a,b,n)
      elif seq.title() == "Gp":
         a = float(input("What is the first term of your series: \n --> \t"))
         b = float(input("What is the second term of your series: \n --> \t"))
         n = int(input("Till which term of the series would you like to display: \n --> \t"))
         geo(a,b,n)
      elif seq.title() == "Hstone":
         n = int(input("Which number's collatz conjecture do you want to generate : \n --> \t"))
         collatz(n)
      yorn = input("Do you still want to continue? Y/N: \n --> \t")
