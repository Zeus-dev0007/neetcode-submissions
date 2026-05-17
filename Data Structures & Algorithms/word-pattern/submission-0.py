class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
# Step 1: Split the string 's' by spaces into a list of words
        words = s.split()
        
        # If the number of characters doesn't match the number of words,
        # it's impossible to have a 1-to-1 pattern match.
        if len(pattern) != len(words):
            return False
            
        # Step 2: Use two dictionaries to store the two-way mappings
        char_to_word = {}
        word_to_char = {}
        
        # Step 3: Check characters and words side-by-side
        for char, word in zip(pattern, words):
            
            # Check the forward mapping: character -> word
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                char_to_word[char] = word
                
            # Check the reverse mapping: word -> character
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False
            else:
                word_to_char[word] = char
                
        return True