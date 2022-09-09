def uncommon_words(sentence1: str, sentence2: str)-> list:
    """
    Given two strings representing sentences, return the words that are not common to both strings (i.e. the words that only appear in one of the sentences). You may assume that each sentence is a sequence of words (without punctuation) correctly separated using space characters. 

    Example: given the following strings...

    sentence1 = "the quick", sentence2 = "brown fox", return ["the", "quick", "brown", "fox"]
    sentence1 = "the tortoise beat the hare", sentence2 = "the tortoise lost to the hare", return ["beat", "to", "lost"]
    sentence1 = "copper coffee pot", sentence2 = "hot coffee pot", return ["copper", "hot"]
    """
    count = {}

    for word in sentence1.split():
        count[word] = count.get(word, 0) + 1
    
    for word in sentence2.split():
        count[word] = count.get(word, 0) + 1

    return [word for word in count if count[word] == 1]

if __name__ == '__main__':
    vals = [["the quick", "brown fox"], ["the tortoise beat the hare", "the tortoise lost to the hare"], ["copper coffee pot", "hot coffee pot"]]

    for val in vals:
        print(uncommon_words(sentence1=val[0], sentence2=val[1]))