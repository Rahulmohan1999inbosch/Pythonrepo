#============================Function caching======================================================#
#when you have function which has complex computatio and assume you want for certain range of values are limited , using functioing it's a kind of  temporary cache storing element

from functools import lru_cache  #this method from functools is used for storing the cache data
import time

@lru_cache(maxsize=None)  #maxsize means the cache size can be as max as possible
def fx(n):
    time.sleep(5)
    return 5*n
# memoization is a technique where the computer stores the data and need not generate again rather it can use it from cache


print(fx(20))
print(fx(24))
print(fx(24))
print(fx(24))
print(fx(24))
print(fx(24))
print(fx(24))

