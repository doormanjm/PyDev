wkday = dict()
wkday = {"Fri": 20, "Thu": 6, "Sat": 1}
wkday["Thu"] = 13
wkday["Sat"] = 2
wkday["Sun"] = 9
print(wkday)

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    # both the commented solution and uncommented solution are equivalent
    counts[name] = counts.get(name, 0) + 1
    #if name not in counts:
        #counts[name] = 1
    #else :
       #counts[name] = counts[name]+ 1
print(counts)

counts2 = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts2.get('kris', 0))