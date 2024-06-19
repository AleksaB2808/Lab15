# Lab15
def clean_data(data):
    return [item.strip().lower() for item in data.split(',')]
Опис:
Ця функція очищує рядок data, розділяючи його за комами, видаляючи зайві пробіли по боках кожного елемента та перетворюючи їх у нижній регістр.

Функція filter_emails

def filter_emails(emails):
    return [email for email in emails.split() if email.count('@') == 1 and '.' in email.split('@')[1]]
Опис:
Ця функція фільтрує рядок emails, витягаючи з нього тільки ті email-адреси, які мають рівно один символ '@' і наступний за ним символ '.'.

Функція extract_keywords

def extract_keywords(words, length):
    return [word for word in words.split() if len(word) > length]
Опис:
Ця функція витягує ключові слова з рядка words, довжина яких більше length.

Функція process_text

import re

def process_text(texts):
    cleaned_texts = [re.sub(r'\W+', '', text.strip().lower()) for text in texts.split(',')]
    return [text for text in cleaned_texts if text and len(text) > 1]
Опис:
Ця функція очищує текст texts, видаляючи всі неалфанумеричні символи, зменшує регістр до нижнього, і видаляє пусті рядки або рядки довжиною менше 2 символів.

Функція normalize_data

def normalize_data(data):
    numbers = [float(num) for num in data.split(',')]
    max_value = max(numbers)
    return [round(num / max_value, 3) for num in numbers]
Опис:
Ця функція нормалізує числові дані data, поділені комами. Вона перетворює числа в тип float, знаходить максимальне значення серед них, а потім кожне число ділить на максимальне значення і округлює до трьох знаків після коми.

Функція concatenate_strings

def concatenate_strings(data, separator):
    return ''.join(data.split(separator))
Опис:
Ця функція конкатенує рядок data, розділений separator, у єдиний рядок без проміжків.

Функція sum_numeric_strings

def sum_numeric_strings(numbers):
    return sum(int(num) for num in numbers.split(',') if num.strip().isdigit())
Опис:
Ця функція сумує всі числові рядки у numbers, розділені комами, ігноруючи некоректні значення.

Функція filter_numbers

def filter_numbers(data, threshold):
    return [int(num) for num in data.split() if num.isdigit() and int(num) > threshold]
Опис:
Ця функція фільтрує рядок data, витягуючи з нього тільки числа, які більші за threshold.

Функція map_to_squares

def map_to_squares(numbers):
    return [int(num)**2 for num in numbers.split(',') if num.strip().isdigit()]
Опис:
Ця функція підносить до квадрата кожне число у рядку numbers, розділеному комами, якщо вони є цілими числами.

Функція reverse_strings

def reverse_strings(words):
    return [word[::-1] for word in words.split(',')]
Опис:
Ця функція обертає кожне слово у рядку words, розділеному комами, в зворотньому порядку.

Кожна з цих функцій виконує конкретні завдання з обробки даних або обробки рядків згідно з вказаними правилами.
