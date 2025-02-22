import re

f = open("row.txt", "r", encoding="utf-8")
text = f.read()
BINpattern = r"\nБИН\s(?P<BIN>[0-9]+)"
x = re.search(BINpattern, text)
BINresult = x.group("BIN")
print(BINresult)

Checkpattern = r"\nЧек\s(?P<Check>№[0-9]+)"
x = re.search(Checkpattern, text)
Checkresult = x.group("Check")
print(Checkresult)

ItemPattern = r"\n(?P<ItemRowNumber>.*)\n(?P<ItemName>.*)\n(?P<ItemCount>)\sx\s(?P<ItemPrice>)"


ItemResult = re.search(ItemPattern, text).group("ItemName")
print(ItemResult)