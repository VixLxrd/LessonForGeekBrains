import decimal
import time
def fib(n):
    decimal.getcontext().prec = 1000000000
    root_5 = decimal.Decimal(5).sqrt()
    phi = ((1 + root_5) / 2)
    a = ((phi ** n) - ((-phi) ** -n)) / root_5
    return round(a)

def get_hash_sum():
    n = 247681498
    res = 0
    while n > 0:
        res += fib(n)
        n = n // 2 if n % 2 == 0 else (n - 1) // 2

    return res & 0xffffffffffffffff

#
# def main():
#     print(f'Flag is Course{{{get_hash_sum()}}}')
#
#
# if __name__ == '__main__':
#     main()
start_time = time.time()
print(fib(247681498))
print("--- %s seconds ---" % (time.time() - start_time))
