def correct_capitalization(word: str = None)-> bool:
    assert word != None, 'Word cannot be none'
    if word != '':
        if word.isupper():
            return True

        if word.islower():
            return True

        if word[0].isupper() == True:
            for letter in word[1::]:
                if letter.isupper() == True:
                    return False
        if word[0].islower() == True:
            for letter in word[1::]:
                if letter.isupper() == True:
                    return False
        return True


if __name__ == '__main__':
    words = ['USA', 'compUter', None, 'Calvin', 'coding']
    
    for word in words:
        try:
            print(f'Word is {word} answer is: {correct_capitalization(word)}')
        except Exception as e:
            print('Exception:', e)