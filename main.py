def clean_data(data):
    return [item.strip().lower() for item in data.split(',')]

# Пример использования
data = "   Apple, Banana , orange "
cleaned = clean_data(data)
print(cleaned)  # ['apple', 'banana', 'orange']

def filter_emails(emails):
    return [email for email in emails.split() if email.count('@') == 1 and '.' in email.split('@')[1]]

# Пример использования
emails = "mail us test@example.com and invalid-email.com.djwd with example@test.co"
valid_emails = filter_emails(emails)
print(valid_emails)  # ['test@example.com', 'example@test.co']

def extract_keywords(words, length):
    return [word for word in words.split() if len(word) > length]

# Пример использования
words = "apple pear banana kiwi"
filtered_words = extract_keywords(words, 4)
print(filtered_words)  # ['apple', 'banana']

import re

def process_text(texts):
    cleaned_texts = [re.sub(r'\W+', '', text.strip().lower()) for text in texts.split(',')]
    return [text for text in cleaned_texts if text and len(text) > 1]

# Пример использования
texts = "  Hello!  , Yes? , No. ,   "
processed_texts = process_text(texts)
print(processed_texts)  # ['hello', 'yes']

def normalize_data(data):
    numbers = [float(num) for num in data.split(',')]
    max_value = max(numbers)
    return [round(num / max_value, 3) for num in numbers]

# Пример использования
numbers = "10, 20,30"
normalized_numbers = normalize_data(numbers)
print(normalized_numbers)  # [0.333, 0.667, 1.0]

def concatenate_strings(data, separator):
    return ''.join(data.split(separator))

# Пример использования
data = "hello*world*again"
concatenated = concatenate_strings(data, '*')
print(concatenated)  # 'helloworldagain'

def sum_numeric_strings(numbers):
    return sum(int(num) for num in numbers.split(',') if num.strip().isdigit())

# Пример использования
numbers = "1, 2, test,  3, 4"
total_sum = sum_numeric_strings(numbers)
print(total_sum)  # 10

def filter_numbers(data, threshold):
    return [int(num) for num in data.split() if num.isdigit() and int(num) > threshold]

# Пример использования
numbers = "10 test 30 40"
filtered = filter_numbers(numbers, 25)
print(filtered)  # [30, 40]

def map_to_squares(numbers):
    return [int(num)**2 for num in numbers.split(',') if num.strip().isdigit()]

# Пример использования
numbers = "1, 2, 3, 4"
squared_numbers = map_to_squares(numbers)
print(squared_numbers)  # [1, 4, 9, 16]

def reverse_strings(words):
    return [word[::-1] for word in words.split(',')]

# Пример использования
words = "apple,banana,carrot"
reversed_words = reverse_strings(words)
print(reversed_words)  # ['elppa', 'ananab', 'torrac']
