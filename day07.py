#!/usr/bin/env python
# encoding: utf-8
"""
Advent of Code 2022 - Day 07
https://adventofcode.com/2022/day/07

Solution 1: 1428881
Solution 2: 10475598

'Trees? Where we are going we don't need... trees'
"""

__author__ = "Filippo Corradino"
__email__ = "filippo.corradino@gmail.com"


from collections import defaultdict


def traverse_filesystem(ifile):
    # Let's compute a dict of directory sizes
    dirsize = defaultdict(int)
    location = ['/']
    with open(ifile) as file:
        for line in file:
            # Command - only check cd commands
            if line.startswith('$'):
                if line.startswith('$ cd'):
                    dir = line.strip().split()[-1]
                    if dir == '..':
                        location.pop()
                    elif dir == '/':
                        location = [dir]
                    else:
                        location.append(location[-1] + dir + '/')
            # Listing - only care for files
            elif not line.startswith('dir'):
                filesize = int(line.split()[0])
                for dir in location:
                    dirsize[dir] += filesize
    return dirsize


def main(ifile='inputs/day_07_input.txt',
         disk_total=70000000, disk_available_target=30000000, threshold=100000):
    dir_sizes = traverse_filesystem(ifile)
    small_dirs_space = sum(v for v in dir_sizes.values() if v <= threshold)
    disk_used = dir_sizes['/']
    space_to_free = disk_used + disk_available_target - disk_total
    large_dir_space = min(v for v in dir_sizes.values() if v >= space_to_free)
    print(f"The total space of directories smaller than {threshold} B "
          f"is {small_dirs_space} B")
    print(f"The size of the smallest unique directory to delete "
          f"is {large_dir_space} B")
    return [small_dirs_space, large_dir_space]
    

if __name__ == "__main__":
    main()
