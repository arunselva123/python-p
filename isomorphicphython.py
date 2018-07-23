2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        dicS={}
        dicT={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            charS=s[i]
            charT=t[i]
            if (dicS.has_key(charS) and not dicT.has_key(charT)) or (not dicS.has_key(charS) and dicT.has_key(charT)):
                return False
            elif dicS.has_key(charS) and dicT.has_key(charT):
                if dicS[charS] != dicT[charT]:
                    return False
            else:
                dicS[charS] = len(dicS)
                dicT[charT] = len(dicT)
        return True
