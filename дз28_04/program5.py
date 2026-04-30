from functools import reduce

rooms = [
    {"name": "Kitchen", "length": 6, "width": 4},
    {"name": "Room 1", "length": 5.5, "width": 4.5},
    {"name": "Room 2", "length": 5, "width": 4},
    {"name": "Room 3", "length": 7, "width": 6.3},
]


def area(room):
    min_area = room["length"] * room["width"]
    return min_area


res = reduce(lambda x, room: x + area(room), rooms, 0)

print(res)
