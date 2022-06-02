def main():
    while True:
        try:
            a = float(input("Area of zone (sf): "))
            q = float(input("Total zone flow rate (gpm): "))
            print('Average precipitation rate in zone:', round(precip(q,a),3), 'in')
        except ValueError:
            print("Type values in numeric format. Example: 1.234")
        else:
            break

def precip(x, y):
    return (96.3 * x) / y

main()