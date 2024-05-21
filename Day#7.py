"""
dolar - komendy
/ - główny katalog
cd - zmiana katalogu
cd x - szuka tego katalogu i go uobecnia
cd .. - wychodzi z obecnego katalogu
cd / - przenosi na główny katalog

ls - wypisuje wszystko co zawarte w obecnym katalogu
dir ...- katalog zawiera katlog nazwany ...
123 x - katalog zawiera plik "x" z rozmiarem 123
"""

with open("day7.txt") as file:
    data = [i for i in file.read().strip().splitlines()]

sorted_data = [i.split(" ") for i in data]

pre_dir = "/main"
dirs = {"/main": 0}
total = 0

for i in sorted_data:
    if i[0] == "$":
        if i[1] == "cd":
            if i[2] == "/":
                pre_dir = "/main"
            elif i[2] == "..":
                pre_dir = pre_dir[: pre_dir.rfind("/")]
            else:
                dir_name = i[2]
                pre_dir = pre_dir + "/" + dir_name
                dirs.update({pre_dir: 0})
        if i[1] == "ls":
            pass
    elif i[0] == "dir":
        pass
    else:
        size = int(i[0])

        directory = pre_dir
        for i in range(pre_dir.count("/")):
            dirs[directory] += size
            directory = directory[: directory.rfind("/")]

limit = 30000000 - (70000000 - dirs["/main"])
too_high_dirs = []

for directory in dirs:
    if dirs[directory] <= 100000:
        total += dirs[directory]

    if limit <= dirs[directory]:
        too_high_dirs.append(dirs[directory])


print("Answer to part 1:", total)
print("Answer to part 2:", min(too_high_dirs))
