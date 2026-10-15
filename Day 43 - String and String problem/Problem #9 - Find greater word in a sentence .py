def greater_word(sentence):
    if not sentence:
        return None

    largest=""
    current_word=""
    for char in sentence:
        if char != " ":
            current_word+=char

        else:
            if len(current_word) > len(largest):
                largest=current_word

            current_word=""
    if len(current_word) > len(largest):
        largest=current_word
        


    return largest
sentence=input("Enter sentence :")
print(greater_word(sentence))

    

