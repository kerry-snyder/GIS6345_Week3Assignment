# Write a function named check_fermat that takes four parameters—a, b, c and n—and checks to see if Fermat’s theorem holds
def check_fermat(a,b,c,n):
    if n > 2 and (a**n)+(b**n)==(c**n):
        print ('Holy smokes, Fermat was wrong!')
    else:
        print ("No, that does't work")

check_fermat(1,2,3,5)
check_fermat(3,6,54,1)

#Write a function that prompts the user to input values for a, b, c and n, converts them to integers, and uses check_fermat to check whether they violate Fermat’s theorem.

    
first = input('What is your first number?\n')
   
second = input('What is your second number?\n')
   
solution = input('What is your solution?\n')
    
power = input('What is your power?\n')

def input_fermat(first, second, solution, power):
    check_fermat(int(first),int(second),int(solution),int(power))

input_fermat(first, second, solution, power)

