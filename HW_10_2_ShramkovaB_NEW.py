def first_word(text):
    n = len(text)
    i = 0
    result = str()

    while i < n and not (text[i].isalpha() or text[i] == "'"):
        i += 1
    
    while i < n and (text[i].isalpha() or text[i] == "'"):
        result += text[i]
        i += 1
    return result
  
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
