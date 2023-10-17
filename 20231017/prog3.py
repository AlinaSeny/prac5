import timeit
import string


def inp(s):
    s = set(s)
    vow = set('aeouyi')
    con = set(string.ascii_lowercase) - vow
    return "vowels:" + str(len(s & vow))+ "\ncons:" + str(len(s & con))


print(timeit.Timer('inp("asdfghjklhgftfyhkjb")', globals=globals()).autorange())
