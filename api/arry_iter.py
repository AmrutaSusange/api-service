def totalArray(ar:list):
    total = 0
    for nums in ar:
        total = total + nums
    print(total)
    return total


def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


if __name__ == "__main__":
    print(reverse_string("hello"))
