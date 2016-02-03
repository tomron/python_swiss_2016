'''
d = {}
d[42] += 1
'''
# Error

from collections import defaultdict

d= defaultdict(int)
d[42] += 1
#defaultdict(<type 'int'>, {42: 1})

from collections import Counter

d = Counter()
d[42] += 1
#Counter({42: 1})
