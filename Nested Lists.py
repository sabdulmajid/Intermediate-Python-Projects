# Nested Lists.py
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[3][0])

for row in number_grid:
    for col in row:
        print(col)

scores = []
marks = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marks += [[name, score]]
        scores += [score]
    sorted_variable = sorted(list(set(scores)))[1]

    for i, j in sorted(marks):
        if j == sorted_variable:
            print(i)