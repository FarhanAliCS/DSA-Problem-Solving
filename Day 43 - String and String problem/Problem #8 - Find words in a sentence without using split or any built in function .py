def count_words_in_sentence(sentence):
    if not sentence:
        return 0
    
    in_word=False
    count=0
    for char in sentence:
        if char != " " and not in_word:
            count+=1
            in_word=True
        elif char == " ":
            in_word=False


    return count

sentence=input("Enter a sentence :")
print(count_words_in_sentence(sentence))