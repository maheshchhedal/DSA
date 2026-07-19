class Solution(object):
    def mostWordsFound(self, sentences):
        max_word = 0
        
        for sen in sentences:
            word = sen.split()
            max_word = max(max_word, len(word))
            
        return max_word