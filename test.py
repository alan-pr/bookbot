def sort_on(dict):
    return dict["count"]

l = []
d1 = {"char": 'a', "count": 3}
d2 = {"char": 'b', "count": 1}

l.append(d1)
l.append(d2)
l.sort(key=sort_on)

print(l)