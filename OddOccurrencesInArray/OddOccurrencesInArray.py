# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    result = 0
    for num in A:
        result ^= num
    return result