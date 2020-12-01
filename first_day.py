import requests
import itertools


def main():
    # You can get your numbers using a get request, 
    # but you need your session id, to get it go on https://adventofcode.com/2020/day/1/input,
    # use the developers tools with any browser and look at the header of the request
    r = requests.get("https://adventofcode.com/2020/day/1/input", headers={"Cookie": "YOUR-SESSION-ID"})
    if r.status_code == 200:
        numbers = [int(x) for x in r.content.decode().split('\n') if x is not '']
        target = 2020
        print("First = {}".format(first(numbers, target)))
        second(numbers, target)



def first(numbers, target):
    for i, number in enumerate(numbers[:-1]):
        complementary = target - number
        if complementary in numbers[i+1:]:
            return (number*complementary)


def second(numbers, target, partial=[]):
    s = sum(partial)
    if s == target and len(partial) is 3:
        print("Second = {}".format(partial[0]*partial[1]*partial[2]))
    if s >= target:
        return

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        second(remaining, target, partial + [n])
        

if __name__ == "__main__":
    main()