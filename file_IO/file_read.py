# .read()でファイルの中身の全てを一つのstringとして返す
# with open("pep8_introduction.txt") as f:
#     print(f.read())
    
# .readline()で一行づつ取得しながらでstring返す
# with open("pep8_introduction.txt") as f:
#     line = f.readline()
#     while line:
#         print(line, end="")
#         line = f.readline()
        
# .readlines()で全ての行をlistで返す
with open("pep8_introduction.txt") as f:
    lines = f.readlines()
    print(lines)
