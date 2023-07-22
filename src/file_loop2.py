counts = {'Jan' : 100, 'Fred' : 42, 'Chuck' : 1}

#for key in counts:
#        print(key, counts[key])

t = sorted(counts.items())
for k, v in t:
    print(k, v)
    