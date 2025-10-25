class Solution:
    def winner(self, arr, n):
        vote_count = {}
        for name in arr:
            vote_count[name] = vote_count.get(name, 0) + 1
        max_votes = 0
        winner_name = ""
        for name, votes in vote_count.items():
            if votes > max_votes or (votes == max_votes and name < winner_name):
                max_votes = votes
                winner_name = name
        return [winner_name, str(max_votes)]
