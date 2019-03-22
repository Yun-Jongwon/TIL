data=[1,1,2,2,3,3]

def baby():
    for a in range(6):
        for b in range(6):
            if a!=b:
                for c in range(6):
                    if a!=c and b!=c:
                        for d in range(6):
                            if a!=d and b!=d and c!=d:
                                for e in range(6):
                                    if a!=e and b!=e and c!=e and d!=e:
                                        for f in range(6):
                                            if a!=f and b!=f and c!=f and d!=f and e!=f:
                                                new_data=[data[a],data[b],data[c],data[d],data[e],data[f]]
                                                if ((new_data[0]==new_data[1] and new_data[1]==new_data[2]) or (new_data[0]+1==new_data[1] and new_data[1]+1==new_data[2])) and ((new_data[3]==new_data[4] and new_data[4]==new_data[5]) or (new_data[3]+1==new_data[4] and new_data[4]+1==new_data[5])):
                                                    return 'babygin'
    return 'False'

print(baby())