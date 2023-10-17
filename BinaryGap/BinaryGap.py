# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # Implement your solution here
    binString = decToBin(N)

    longestGap = 0
    gap = 0

    for c in binString:
        if c == "1":
            longestGap = max(longestGap, gap)
            gap = 0
        else:
            gap += 1

    return longestGap

def decToBin(N: int) -> str:
    binString = ""
    while N > 0:
        binString = str(N%2) + binString
        N //= 2

    return binString