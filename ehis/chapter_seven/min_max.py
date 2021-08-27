import sys


def my_version_of_max(a_list: list):
    maximum: int = -sys.maxsize
    for i in a_list:
        if i > maximum:
            maximum = i
    return maximum


def my_version_of_min(a_list: list):
    minimum: int = sys.maxsize
    for i in a_list:
        if i < minimum:
            minimum = i
    return minimum


if __name__ == "__main__":
    print(f"The maximum in {2, 3, 5,46, -2} is {my_version_of_max([2,3,5,46,-2])}")
    print(f"The minimum in {2, 3, 5,46, -2} is {my_version_of_min([2,3,5,46,-2])}")
