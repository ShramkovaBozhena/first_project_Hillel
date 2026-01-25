import string

def is_palindrome(text): 

    symbol = string.punctuation + " "

    for i in symbol:
        text = (text.replace(i, "")).lower()
    a = int(len(text) / 2)
    result = (text[:a:] == text[a+1:][::-1])
    
    return result

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1' 
assert is_palindrome('0P') == False, 'Test2' 
assert is_palindrome('a.') == True, 'Test3' 
assert is_palindrome('aurora') == False, 'Test4' 
print("OK")
