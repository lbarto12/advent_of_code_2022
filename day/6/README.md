# Solutions:

### Python

The logic for this problem is entirely contained in `get_marker_location(stream, block_size)`.

The function begins by creating a string `packet` of length `block_size` initialized with 0's to act as a kind of viewport, since we need to view `block_size` characters from the stream at a time

Then, it iterates over the enumerated stream to unpack `i`, and `char`. Each iteration moves the stream 1 character to the left

e.g "000h" => "00hs" => "0hsk" => "hsks"

Essentially sliding the stream over `packet` to view `block_size` characters each iteration

Then, function checks whether there are any duplicates in the string by comparing the lengths of a set that holds all the characters, and the `block_size`. If there are no duplicates, the function returns the current value of `i` + 1 to get the position of the first found marker.

This function is re-used in part 2 with a block_size of 14
