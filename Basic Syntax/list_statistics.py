n = int(input())
positives = []
negatives = []

for num in range(n):
    num = int(input())
    if num >= 0:
        positives.append(num)
    else:
        negatives.append(num)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")