def main():
    while True:
        try:
            dulq = float(input("Lower quarter distribution uniformity: "))
            print("Scheduling multiplier:", round(schedule(dulq),2))
        except ValueError:
            print("Type values in numeric format. Example '1.234'")
        else:
            break

def schedule(a):
    return 1/(.4+(.6*a))

main()