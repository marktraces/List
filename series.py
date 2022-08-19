def sequences():
    series = ["Fibonacci = Fib","Arithmetic Progression = AP", "Geometric Progression = GP"]
    print("Which of the following series would you like to operate in? \n")
    for i in range(0,len(series)):
        print(series[i].title())
    seq = input("Which of the above would you like to select :  \n --> \t")
    if seq.title() == "Fib":
        a = 1/(5**0.5)
        b = (1 + 5**0.5)
        c = (1 - 5**0.5)
        n = int(input("Which term of the series would you like to display: \n --> \t"))
        fib = int(a * (b**n - c**n)/2**n)
        print(f"{fib} is the {n}th term of the {seq} series")
    elif seq.title() == "AP":
        a = input("What is the first term of your series: \n --> \t")
        b = input("What is the second term of your series: \n --> \t")
        d = (b - a)
        n = int(input("Which term of the series would you like to display: \n --> \t"))
        AP = a + (n-1)*d
        print(f"The {n} term of the series is {AP}")
    elif seq.title() == "GP":
        a = input("What is the first term of your series: \n --> \t")
        b = input("What is the second term of your series: \n --> \t")
        r = (b/a)
        n = int(input("Which term of the series would you like to display: \n --> \t"))
        GP = a * (r**(n-1))
        print(f"The {n}th term of the series is {GP}")

print("Let's commence our program")
boolean = input("Would you like to begin? Y/N: \n --> \t")
while boolean.upper == "Y":
  sequences()
  boolean = input("Do you still want to continue? Y/N: \n --> \t")
