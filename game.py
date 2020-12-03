from scrap_words import words
from random import shuffle

score = 0
for word in words:
    print('-'*72)
    l_word = list(word)
    shuffle(l_word)
    randomized = ''.join(l_word)
    print(randomized + '\n')

    guess = input('Sence bu hangi kelime?\nCevabın:')

    if (guess == word):
        score += 1
        print('Doğru!')
        print('Skorun:', score)

    else:
        print('Yanlış! Cevap:', word)
        print('Skorun:', score)

print('-' * 72)
print('Oyun Bitti! Skorun:', score)
