class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        paragraph = paragraph.lower()

        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")

        p = paragraph.split()

        dict1 = {}

        for word in p:
            if word not in banned:
                if word not in dict1:
                    dict1[word] = 1
                else:
                    dict1[word] += 1

        ans = ""
        count = 0

        for key, value in dict1.items():
            if value > count:
                count = value
                ans = key

        return ans