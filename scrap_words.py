import random

with open('words.txt', 'r', encoding='utf-8') as f:
    words = f.readlines()

words = map(lambda x: x.split('\n')[0], words)
words = [x for x in words if (len(x) > 3)]


random_index = [random.randint(0, len(words)-1) for i in range(10)]

words = [words[index] for index in random_index]
