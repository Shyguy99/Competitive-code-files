n = input()
c = 0
sr_dict = dict(dict())
m = 0
inda = -1
for i in range(len(n)):
    if n[i] not in sr_dict:
        sr_dict[n[i]] = dict({str(i): 1})
        c += 1
    else:
        idx = int((list(sr_dict[n[i]].keys())[0]))
        if idx < inda:
            sr_dict[n[i]][str(i)] = sr_dict[n[i]][str((list(sr_dict[n[i]].keys())[0]))]
            del sr_dict[n[i]][str((list(sr_dict[n[i]].keys())[0]))]
            c += 1
        else:
            c -= (int((list(sr_dict[n[i]].keys())[0])) - inda - 1)
            inda = int((list(sr_dict[n[i]].keys())[0]))
            sr_dict[n[i]][str(i)] = sr_dict[n[i]][str((list(sr_dict[n[i]].keys())[0]))]
            del sr_dict[n[i]][str((list(sr_dict[n[i]].keys())[0]))]
    m = max(m, c)

print(m)




