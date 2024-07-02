def single_root_words(root_word, *other_words):
    same_words = []
    other_words = list(other_words)
    root_word = root_word.upper()
    other_words2 = []
    for j in other_words:
        a = j.upper()
        other_words2.append(a)
    for i in range(len(other_words)):
        if root_word in other_words2[i] or other_words2[i] in root_word:
            same_words.append(other_words[i])
    return(same_words)


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)