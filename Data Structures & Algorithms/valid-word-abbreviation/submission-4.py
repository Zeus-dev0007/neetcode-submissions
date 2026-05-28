class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0  # i tracks word, j tracks abbr
        
        while i < len(word) and j < len(abbr):
            # Case 1: If we find a number in the abbreviation
            if abbr[j].isdigit():
                # Check for invalid leading zero
                if abbr[j] == '0':
                    return False
                
                # Fetch the full number (handles multi-digit numbers like "12")
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                
                # Move the word pointer forward by the number of skipped characters
                i += num
                
            # Case 2: If we find a letter, it must match the letter in 'word'
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
                
        # Both pointers must reach the exact end of their respective strings
        return i == len(word) and j == len(abbr)