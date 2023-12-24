import dcalc


def create_list_degrees(*args, **kwargs):
    d = {}
    for i in range(len(args)):
        d[f"Point_{i}"] = args[i]
    d.update(kwargs)
    ans = []
    for k, v in d.items():
        ans.append(f"{k} = {dcalc.deg_to_gms(v)}")
    return ans


print(create_list_degrees(172.25899161, 321.42304971, 12.697987681352, pole=21.89617856, put_1=140.85706440))
