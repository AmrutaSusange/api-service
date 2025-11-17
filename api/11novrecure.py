def printNums(Lrange, Urange):
    if Lrange > Urange:
        return
    printNums(Lrange + 1, Urange)
    print(Lrange)


if __name__ == "__main__":
    printNums(1,5)
