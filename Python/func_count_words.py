def count_words(sentence):
    return sentence.count(' ') + 1

sentence = input()
print(f"단어 수: {count_words(sentence)}")