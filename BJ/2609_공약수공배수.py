'''
https://www.acmicpc.net/problem/2609
'''

n, m = map(int, input().split())

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r

    return a

def lcm(a, b):
    return int((a * b) / gcd(a, b))

print(gcd(n,m))
print(lcm(n,m))