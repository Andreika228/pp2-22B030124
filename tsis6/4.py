import time
import math
def delay(n, t, *args):
  time.sleep(t / 1000)
  return n(*args)
n=int(input())
t= int(input())
print("Square root of ",n, " after ", t,"miliseconds is ",delay(lambda x: math.sqrt(x), t, n) ) 