#User function Template for python3
class Solution:

	
	def removeDuplicates(self, s):
	    # code here
	    seen = set()
	    result = []
	    for c in s:
	        if c not in seen:
	            seen.add(c)
	            result.append(c)
	    return ''.join(result)