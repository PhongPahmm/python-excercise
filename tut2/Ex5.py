def find_substring_occurrences(s, sub):
    start = 0
    positions = []
    while True:
        start = s.find(sub, start)
        if start == -1:
            break
        positions.append(start)
        start += len(sub)
    return positions

s = input("Enter a string: ")
sub = input("Enter a sub-string: ")
positions = find_substring_occurrences(s, sub)
print(positions)