import json
import math
import argparse


def is_prime(num: int) -> bool:
    if num < 2: return False
    if num == 2 or num == 3: return True
    elif num % 2 == 0 or num % 3 == 0: return False
    else:
        i, limit = 5, math.isqrt(num)
        while i <= limit:
            if (num % i == 0) or (num % (i + 2) == 0):
                return False
            i += 6
    return True


def fizzbuzz(start=1, end=100):
    result = []
    if end < start:
        temp = start
        start = end
        end = temp
    for i in range(start, end + 1):
        if i % 15 == 0:
            result.append("Fizzbuzz")
        elif is_prime(i):
            result.append("Prime")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

if __name__ == "__main__":
    parser =argparse.ArgumentParser(description= "a simple script demonstrating loops, conditions and prime check")
    parser.add_argument("start", nargs="?", type=int, default=1, help= "the starting number to iterate from")
    parser.add_argument("end", nargs="?", type=int, default=100, help= "the last number to iterate to")
    parser.add_argument("--json", action="store_true", help= "get the output as a JSON array")
    args = parser.parse_args()
    result = fizzbuzz(args.start, args.end)
    print("\n".join(result) if not args.json else json.dumps(result))
