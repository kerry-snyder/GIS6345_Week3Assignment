#Code defining first, last, and middle numbers
def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

#Testing the code
print(middle('at'))
print(middle('a'))
print(middle(''))
print(middle('assignment'))

#Writing a palindrome function 
def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

#Testing the palindrome function
print(is_palindrome('redivider'))
print(is_palindrome('t'))
print(is_palindrome('sweet'))
      

                            

        
             
