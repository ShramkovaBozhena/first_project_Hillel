import string

def is_palindrome(text): 
    symbol = string.punctuation + " "

    for i in symbol:
        text = (text.replace(i, "")).lower()

    len_str = len(text)

    for idx, item in enumerate(text):
        if item != text[len_str - 1 - idx]:
            result = False
            break
        if idx == int((len_str) / 2):
            result = True
            break
    return result

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1' 
assert is_palindrome('0P') == False, 'Test2' 
assert is_palindrome('a.') == True, 'Test3' 
assert is_palindrome('aurora') == False, 'Test4' 
print("OK")