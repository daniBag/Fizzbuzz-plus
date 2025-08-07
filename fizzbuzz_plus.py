import json
import math
import argparse


def is_primary(num):
    prime = False
    if num == 2 or num == 3:
        prime = True
    elif num > 1:
        if num % 2 != 0:
            if num % 3 != 0:
                i = 5
                while i <= math.sqrt(num):
                    if (num % i == 0) or (num % (i + 2) == 0):
                        break
                    i += 6
                prime = True
    return prime


def fizzbuzz(start=1, end=100):
    result = []
    if end < start:
        temp = start
        start = end
        end = temp
    for i in range(start, end + 1):
        if i % 15 == 0:
            result.append("fizzbuzz")
        elif is_primary(i):
            result.append("prime")
        elif i % 3 == 0 and i != 3:
            result.append("fizz")
        elif i % 5 == 0:
            result.append("buzz")
        else:
            result.append(str(i))
    return result

if __name__ == "__main__":
    parser =argparse.ArgumentParser(description= "a simple script demonstrating loops, conditions and prime check")
    parser.add_argument("start", help= "the starting number to iterate from")
    parser.add_argument("end", help= "the last number to iterate to")
    parser.add_argument("--json", action="store_true", help= "get the output as a JSON array")
    args = parser.parse_args()
    try:
        start = int(args.start)
        end = int(args.end)
        result = fizzbuzz(start, end)
        if args.json:
            result = json.dumps(result)
        print(result)
    except ValueError:
        print("only numbers are accepted")
