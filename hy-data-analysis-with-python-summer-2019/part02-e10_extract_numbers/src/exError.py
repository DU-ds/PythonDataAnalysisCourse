import sys
s=input("Give a number: ")
s=s[:-1] # strip the \n character from the end
try:
    x=int(s)
    sys.stdout.write(f"You entered {x}\n")
except ValueError:
    print("You didn’t enter a number")

