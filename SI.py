P=float(input("Enter the Principal Amount : "))
T=float(input("Enter the Time Period : "))
R=float(input("Enter the Rate of Intrest : "))

SI=(P*T*R)/100

print(f"The Simple Intrest Is {SI} ")


A = P * (1 + R/100) ** T
CI = A - P

print(f"The Compound Interest is {CI}")
print(f"The Total Amount is {A}")
