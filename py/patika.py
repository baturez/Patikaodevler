import itertools
l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
def flatten(x):
   result = []
   for item in x:
      if isinstance(item, list):
         result.extend(flatten(item))
      else:
         result.append(item)
   return result
print(flatten(l))
ll =  [[1, 2], [3, 4], [5, 6, 7]]
ll = list(reversed(ll))
def reverse(x):
   lx = []
   ly = []
   for i in x:
      s = int(len(i))
      lx.append(list(reversed(i)))
   return lx
m = reverse(ll)
print(list(m))

