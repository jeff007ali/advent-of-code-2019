from collections import Counter

min = 136760
max = 595730

match = 0
for number in range(min, max + 1):
    previous = []
    increaseFlag = True
    doubleFlag = False

    for character in str(number):
        if len(previous) > 1:
            if character < previous[-1]:
                increaseFlag = False
                break
            if previous.count(character) > 0:
                doubleFlag = True

        previous.append(character)

    if increaseFlag and doubleFlag and 2 in Counter(previous).values():
        print(Counter(previous))
        print(number)
        match += 1


print("match: {}".format(match))

