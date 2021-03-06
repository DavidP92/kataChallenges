##Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
##invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
##invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
##invert([]) == []
##You can assume that all values are integers.



def invert(list):
  for x in range(len(list)):
      list[x] = -list[x]
  return list


##Second Solution
def invert(lst):
    return [-x for x in lst]
