"""
4
vtz ud  xnm xugm itr pyy jttk gmv xt otgm xt xnm puk ti xnm fprxq
xnm fffff lrtzv iia wwwfd tsmr xnm ypwq ktj
xnm ceuob lrtzv ita hegfd tsmr xnm ypwq ktj
frtjrpgguvj otvxmdxd prm iev prmvx xnmq
"""
control = "the quick brown fox jumps over the lazy dog"
control_lens = [len(x) for x in control.split()]
n = int(input())
is_solution = None
crypto = []
text = ''
for _ in range(n):
    row = input()
    crypto.append(row)
for row in crypto:
    if len(row) != len(control):
        continue
    row_lens = [len(x) for x in row.split()]
    for cont_l, crypt_l in zip(control_lens, row_lens):
        if cont_l != crypt_l:
            break
    else:
        code_map = { k:v for (k,v) in zip(row, control)}
        result = {}
        for key, value in code_map.items():
            if value not in result.values():
                result[key] = value
        for letter in row:
            try:
                text += result[letter]
            except KeyError:
                text = ''
                continue
        else:
            if text != control:
                text = ''
                continue
        text = ''
        for row_crypto in crypto:
            for letter in row_crypto:
                try:
                    text += result[letter]
                except KeyError:
                    print("No solution")
                    exit()
            text += '\n'
        print(text[:-1])
        exit()
if not text:
    print("No solution")

