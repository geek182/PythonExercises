def MoveArray(A, K):
  for times in range(K):
    templist = A[:]
    for i in range(len(A)):
        if i ==  len(A) - 1 :
            A[0] = templist[i]
        else:
            A[i+1] = templist[i]

  return (A)

A = [1, 2, 3, 4]
K = 2
def solution(A, K):
    return MoveArray(A, K)
solution_print = solution(A,K)

print(solution_print)
