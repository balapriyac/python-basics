with open("scores.txt", "r") as file:
    scores = [float(line.strip()) for line in file]

print(scores)
