from collections import Counter



def day1():
    with open("d4.in") as f:
        valid = 0
        for line in f:
            seen = set()
            for phrase in line.strip().split():
                try: seen.remove(phrase)
                except: seen.add(phrase)
                else: break
            else:
                valid += 1
        print(valid)


def day2():
    with open("d4.in") as f:
        valid = 0
        for line in f:
            seen = []
            for phrase in line.strip().split():
                bag = Counter(phrase)
                try: seen.remove(bag)
                except: seen.append(bag)
                else: break
            else:
                valid += 1
        print(valid)


if __name__ == "__main__":
    day1()
    day2()