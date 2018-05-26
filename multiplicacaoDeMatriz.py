n = int(input())
arr = [-1] # o index 0 do array nao eh usado

def dp(i, j):

	global arr

	if memo[i][j] != (2 ** 30):
		return memo[i][j]

	if i == j: # nao eh possivel multiplicar uma matriz
		memo[i][j] = 0

	elif (j - i) == 1: # sabemos quanto custa multiplicar duas matrizes
		memo[i][j] = (arr[i][0] * arr[j][0] * arr[j][1])

	else:
		for k in range(i, j):
			value = dp(i, k) + dp(k + 1, j) + (arr[i][0] * arr[k][1] * arr[j][1])
			#print("k = {}, v = {}".format(k, value))
			if value < memo[i][j]:
				#print("i = {}, j = {}, k = {}".format(i, j, k))
				memo[i][j] = value
	print("memo[{}][{}] = {}".format(i, j, memo[i][j]))
	return memo[i][j]

for i in range(n):
	matrix = list(map(int, input().split()))
	arr.append(matrix)

memo = [[2 ** 30] * (n + 1) for i in range(n + 1)]

print(dp(1, n))