def fib(n):
    result_fib = 0
    x_ray = [1, 3, 7, 14, 29, 59, 118, 236, 472, 944, 1889, 3779, 7558, 15117, 30234, 60469, 120938, 241876, 483752,
             967505, 1935011, 3870023, 7740046, 15480093, 30960187, 61920374, 123840749, 247681498]
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        print(i)
        if i < 123840750:
            if i + 1 in x_ray:
                result_fib += a
    return a + result_fib


def get_hash_sum(number_user):
    return number_user & 0xffffffffffffffff

print(f'Flag is Course{{{get_hash_sum(247681498446548413846321354958955874596132479568273333149765461321)}}}')
print(bin(0xffffffffffffffff))