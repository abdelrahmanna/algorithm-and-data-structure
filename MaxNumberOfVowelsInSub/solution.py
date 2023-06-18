def maxVowels(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    if len(s) < k:
        k = len(s)

    # num of vowls in first k letter
    Vowel = {'a', 'e', 'i', 'o', 'u'}
    numberOfVowels = 0
    for i in range(k):
        if s[i] in Vowel:
            numberOfVowels += 1

    maxSub = numberOfVowels
    i = k
    j = 1
    while i < len(s):
        if s[j] in Vowel:
            numberOfVowels -= 1
        if s[i] in Vowel:
            numberOfVowels += 1

        if numberOfVowels > maxSub:
            maxSub = numberOfVowels

        i += 1
        j += 1
    
    return maxSub

if __name__ == "__main__":
    print(maxVowels("weallloveyou", 7))