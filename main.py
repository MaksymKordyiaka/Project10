'''Дано: текстовий файл, який містить в собі 1000000 рандомних символів. Створити функцію,
результатом роботи якої буде: словник, де ключем виступатиме символ, значення- скільки
разів цей символ зустрічається в файлі.

Нас цікавлять лише літери, тобто- цифри/розділові знаки чи пробіли ми не враховуємо,
при цьому- велика та мала літера, це одна літера. Методи count() використовувати заборонено.
'''

def file_func(file_name):
    dct = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        for i in file.read():
            if i.isalpha():
                if i in dct:
                    dct[i] += 1
                else:
                    dct[i] = 1
    return dct
n = file_func('your file')
print(n)





