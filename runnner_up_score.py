'''Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. 
You are given n scores. Store them in a list and find the score of the runner-up.
sample input:
5
2 3 6 6 5
sample output:
5
'''
n = int(input())
scores = list(set(map(int, input().split())))
scores.sort()
runner_up_score = scores[-2]
print(runner_up_score)