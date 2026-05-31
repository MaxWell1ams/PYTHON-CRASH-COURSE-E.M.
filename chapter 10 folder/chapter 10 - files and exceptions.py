from pathlib import Path
path = Path('chapter 10 folder/txtfile.txt')
contents = path.read_text().rstrip()
print(contents)