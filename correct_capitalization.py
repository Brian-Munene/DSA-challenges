def correct_capitalization(word: str = None)-> bool:
    """
    Given a string, return whether or not it uses capitalization correctly. A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.

    Example: Given the following strings...

    "USA", return true
    "Calvin", return true
    "compUter", return false
    "coding", return true
    """
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