class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        # If lengths match, a 1-to-1 mapping is impossible
        if len(pattern) != len(words):
            return False
            
        char_to_word = {}
        word_to_char = {}
        
        for char, word in zip(pattern, words):
            # Check if character already maps to a different word
            if char in char_to_word and char_to_word[char] != word:
                return False
            # Check if word already maps to a different character
            if word in word_to_char and word_to_char[word] != char:
                return False
                
            # Establish the mapping
            char_to_word[char] = word
            word_to_char[word] = char
            
        return True
