class Solution:
	# is_match(self, pattern: str, s: str) -> bool
	# precondition: None
	# Postcondition:
	#	there is no effect.
	#	result = true for pattern matching, else false, ? acts as wildcard
	def is_match(self, pattern : str, s : str) -> bool:
		# check lenght of s and pattern
		if len(s) != len(pattern):
			return False
		# loop through the string s
		for i in range(len(s)):
			if s[i] == pattern[i]:
				continue
			elif pattern[i] == '?': # wildcard check
				continue
			else:
				return False
		return True

# Anmerkung von Chatgpt:
# anstatt for i in range(len(s))
# for p_char, s_char in zip(pattern, s):
#	if p_char != '?' and p_char != s_char:
#		return False
#
# Ist kürzer and besser zum lesen
