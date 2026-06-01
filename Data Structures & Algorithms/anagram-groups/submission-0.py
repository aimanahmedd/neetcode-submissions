class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char)-ord("a")] +=1
            hashMap[tuple(count)].append(word) #doing tuple so we can use the list as a key
        return list(hashMap.values())