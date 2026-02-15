import codecs 

def delete_html_tags(html_file, result_file='cleaned.txt'): 
    with codecs.open(html_file, 'r', 'utf-8') as file: 
        html = file.read()

    result = str()
    tag = False

    for i in html:
        match i:
            case '<':
                tag = True
            case '>':
                tag = False
            case _:
                if not tag:
                    result += i

    lines = []
    
    for k in result.splitlines():
        if k.strip():
            lines.append(k.strip())

    result = '\n'.join(lines)

    with open(result_file, 'w', encoding='utf-8') as file:
        file.write(result)

delete_html_tags('draft.html')

assert open('cleaned.txt', encoding='utf-8').read() == """Жарт про функції
Блог
Вхід
Реєстрація
Жарт про функції
Ідуть дві функції — Декоратор і Генератор — через ліс. В одній з них раптом стався ексепшен.
— Ох, я впала! — сказала Функція-Декоратор. — Піди, поклич мій ексепшен!
— А що це таке, ексепшен? — запитав Функція-Генератор.
— Ну, він зазвичай знає, що робити, коли я падаю!"""

print('Ok') 