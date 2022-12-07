import re


def get_files(file):
    files = []
    this_dir_size = 0

    while (line := file.readline()[:-1]) and line != "$ cd ..":
        if find_file_size := (re.search(r'(\d+)', line)):
            this_dir_size += int(find_file_size[1])
        elif line.startswith('$ cd'):
            sub_size, sub_files = get_files(file)
            this_dir_size += sub_size
            files += sub_files

    return this_dir_size, [this_dir_size] + files


with open('../input.txt') as f:

    # get total size of file structure and list of all sizes
    total_size, files = get_files(f)

    # Part 1
    print(f"Part 1: {sum([i for i in files if i < 100000])}")

    # Part 2
    disk_size, required_space = 70000000, 30000000

    files.sort()

    for i in files:
        if disk_size - total_size + i >= required_space:
            print(f"Part 2: {i}")
            break
