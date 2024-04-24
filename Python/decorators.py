
"""
https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem?isFullScreen=true

"""

def wrapper(f):
    def fun(l):
        # complete the function 
        return f(["+91 " + c[-10:-5] + " " + c[-5:] for c in l])
        
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
