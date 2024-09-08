


def int_to_base(n, base):
    to_str = "0123456789ABCDEF"
    if n < base: 
        return to_str[n]
    
    print(n//base, n % base)
    return int_to_base(n // base, base) + to_str[n % base]

# ans = int_to_base(2563, 10)
ans = int_to_base(928, 16)
print(ans)

