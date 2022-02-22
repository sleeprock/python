data = [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = []
for member in data:
    age = member[0]
    hand = member[1]
    if age >= 55 and hand > 7:
        memCat = 'Senior'
    else:
        memCat = 'Open'
    print(memCat)

""" def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data] """