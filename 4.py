def levenshtein_distance(source, target):
    m = len(source) + 1
    n = len(target) + 1

    D = [[0] * n for _ in range(m)]
    for i in range(m):
        D[i][0] = i
    for j in range(n):
        D[0][j] = j

    for i in range(1, m):
        for j in range(1, n):
            if source[i-1] == target[j-1]:
                cost = 0
            else:
                cost = 1
            D[i][j] = min(D[i-1][j] + 1,
                          D[i][j-1] + 1,
                          D[i-1][j-1] + cost)

    return D[-1][-1], D

source = "yu"
target = "you"
distance, D = levenshtein_distance(source, target)
print("Levenshtein distance:", distance)
print ( levenshtein_distance (" hola ", " hello ") )
print("Matrix D:")
for row in D:
    print(row)