def main():
    while True:
        try:
            mc = float(input("Target amount of water to apply (in): "))
            pr = float(input("Gross precipitation rate (in): "))
            sm = float(input("Scheduling multiplier: "))
            print("Minimum weekly runtime:", round(lower_bound(mc, pr)), "min")
            print("Maximum weekly runtime:", round(upper_bound(mc, pr ,sm)), "min")
        except ValueError:
            print("Type values in numeric format. Example '1.234'")
        else:
            break

def lower_bound(a, b):
    return (a * 60) / b

def upper_bound(a, b, d):
    return ((a * 60) / b) * d

main()
