# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # Implement your solution here
    length = len(A)
    result = [0]*length

    for i in range(0, length):
        index = i+K if i+K < length else i+K-length
        result[index] = A[i]

    return result