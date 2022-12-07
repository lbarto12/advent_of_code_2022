# Solutions:

### Python

This solutions relies on recursion to do a depth first search for all the file sizes, in a function called `get_files(file)`, that returns the total filesize for the whole system, and a list of all the filesizes in the system.

The function has two local vairables `files` and `this_dir_size` to store the files as a list, and get the current directory size, respectively.

When the function is called with the input the while loop inside will step through it line by line until it either reaches the end of the file, or hits a line that says `$ cd ..`, which would indicate that we could move upwards in the file structure.

If at any point in it's stepping it finds numbers in a line, it will assume that the numbers correspond to a file size, and add the value to `this_dir_size`. And if at any point it finds a line that starts with `$ cd` (note that this is different from the while loop condition) it will call itself again to create a new 'directory', then store the results of the recursive call in `this_dir_size`, and `files` respectively. To make this recursion work, the function returns `this_dir_size` and `files`

#### Part 1

For part 1, the answer can be found by summing the numbers in the list that are under the given threshold of `100000`.

#### Part 2

For part 2, we create 2 variables `disk_size` and `required_space` to hold the values given to us by the question, then we sort the files, and iterate over them. Once we've found a file that - when added to `disk_size - total_size` - gives us an answer that adheres to the `required_space`, we print the answer and break the loop.
