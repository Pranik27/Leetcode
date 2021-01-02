'''

Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.



Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.


Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 105

Time Complexity: O(n * n)
Space Complexity: O(n) , call stack
'''


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) == 0 or k > len(s):
            return 0
        elif k == 0:
            return len(s)

        char_count = [0] * 26
        temp = 0

        for i in range(len(s)):
            char_count[ord(s[i]) - ord('a')] += 1

        for i in range(len(s)):

            if char_count[ord(s[i]) - ord('a')] < k:

                temp = i
                while i < len(s) and char_count[ord(s[i]) - ord('a')] < k:
                    i += 1

                return max(self.longestSubstring(s[0:temp], k), self.longestSubstring(s[i:], k))

        return len(s)
