#User function Template for python3
class Solution:
	def removeDups(self, str):
		# code here
		seen = set()
		result = []
		for c in str:
		    if c not in seen:
		        seen.add(c)
		        result.append(c)
		return ''.join(result)