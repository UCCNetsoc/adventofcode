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



if __name__ == "__main__":
    day1()