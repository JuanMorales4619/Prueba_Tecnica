import bisect

def climbingLeaderboard(ranked, player):
    unique_scores = sorted(set(ranked), reverse=True)
    unique_scores_neg = [-score for score in unique_scores]
    result = []
    for score in player:
        position = bisect.bisect_left(unique_scores_neg, -score)
        rank = position + 1
        result.append(rank)
    
    return result
print(climbingLeaderboard([100, 90, 90, 80, 75, 60],[50, 65, 77, 90, 102]))