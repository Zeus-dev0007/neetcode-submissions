class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # mapST tracks: s character -> t character
        # mapTS tracks: t character -> s character
        mapST, mapTS = {}, {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]

            # Check if c1 is already mapped to something else
            if c1 in mapST and mapST[c1] != c2:
                return False
            
            # Check if c2 is already mapped to something else
            if c2 in mapTS and mapTS[c2] != c1:
                return False

            # Establish the partnership
            mapST[c1] = c2
            mapTS[c2] = c1
            
        return True