# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    map = {}
    for num in A:
        map[num] = map.get(num, 0) + 1
    
    for num, count in map.items():
        if count < 2:
            return numtest