class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        current_count = [0 for i in range(52)]
        expected_count = [0 for i in range(52)]
        
        for char in t:
            expected_count[ord(char) - ord('a')] += 1
        
        i, count, start, min_width, min_start = 0, 0, 0, float("inf"), 0
        while i < len(s):
            current_count[ord(s[i]) - ord('a')] += 1
            if current_count[ord(s[i]) - ord('a')] <= expected_count[ord(s[i]) - ord('a')]:
                count += 1
            
            if count == len(t):
                while expected_count[ord(s[start]) - ord('a')] == 0 or \
                      current_count[ord(s[start]) - ord('a')] > expected_count[ord(s[start]) - ord('a')]:
                    current_count[ord(s[start]) - ord('a')] -= 1
                    start += 1
                
                if min_width > i - start + 1:
                    min_width = i - start + 1
                    min_start = start
            i += 1
                    
        if min_width == float("inf"):
            return ""
        
        return s[min_start:min_start + min_width]
