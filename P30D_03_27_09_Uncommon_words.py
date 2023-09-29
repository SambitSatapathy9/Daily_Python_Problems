#30 Days Coding Challenge 27-09-23
#Q3 - Finding uncommon words in two sentences
"""
Here’s an example of the input and output values of this problem:

sentence 1 = “Humko mili hai aaj yeh ghadiya naseeb se”,
sentence 2 = “Humko dekh lijiye aap bade kareeb se”
Output: ['mili', 'hai', 'aaj', 'yeh', 'ghadiya', 'naseeb', 'dekh', 'lijiye', 'aap', 'bade', 'kareeb']
"""def uncommon_words(s1,s2):
    words1 = s1.split()
    words2 = s2.split()
    
    counts = {}
    for word in words1 + words2:
        counts[word] = counts.get(word,0) + 1
        
    uncommon = [word for word in counts if counts[word] == 1]
    return uncommon

sn1 = "Humko mili hai aaj yeh ghadiya naseeb se"
sn2 = "Humko dekh lijiye aap bade kareeb se"
print(uncommon_words(sn1,sn2))
