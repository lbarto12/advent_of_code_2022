def get_marker_location(stream, block_size):
    packet = "0" * block_size
    for i, char in enumerate(stream):
        packet = packet[1:] + char
        if len(set(packet)) == block_size:
            return i + 1

with open('../input.txt') as file:
    file = file.read()

    print(f"Part 1: {get_marker_location(stream=file, block_size=4)}")
    print(f"Part 2: {get_marker_location(stream=file, block_size=14)}")
