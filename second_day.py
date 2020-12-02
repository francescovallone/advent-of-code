import requests
from collections import Counter
#res_dct = 


def main():
    # You can get your passwords using a get request, 
    # but you need your session id, to get it go on https://adventofcode.com/2020/day/2/input,
    # use the developers tools with any browser and look at the header of the request
    r = requests.get("https://adventofcode.com/2020/day/2/input", headers={"Cookie": "YOUR-SESSION-ID"})
    if r.status_code == 200:
        strings = [x for x in r.content.decode().split('\n') if x is not '']
        validity = {index: {"letter": strings[index].split(':')[0].strip().split(' ')[1],\
             "min": int(strings[index].split(':')[0].strip().split(' ')[0].split("-")[0]),\
             "max": int(strings[index].split(':')[0].strip().split(' ')[0].split("-")[1])} for index in range(0, len(strings))}
        passwords = [x.split(':')[1].strip() for x in strings]
        print("First = {}".format(first(passwords, validity)))
        print("Second = {}".format(second(passwords, validity)))


def first(passwords, validity):
    valid = 0
    for index in range(0, len(passwords)):
        letters_count = Counter(passwords[index])
        n_of_specific_letter = letters_count[validity[index]['letter']]
        if validity[index]['min'] <= n_of_specific_letter <=validity[index]['max']:
            valid += 1
    return valid


def second(passwords, validity):
    valid = 0
    for index in range(0, len(passwords)):
        if (passwords[index][validity[index]['min']-1] == validity[index]['letter'] and passwords[index][validity[index]['max']-1] != validity[index]['letter'])\
            or (passwords[index][validity[index]['max']-1] == validity[index]['letter'] and passwords[index][validity[index]['min']-1] != validity[index]['letter']):
            valid+=1
    return valid



if __name__ == "__main__":
    main()