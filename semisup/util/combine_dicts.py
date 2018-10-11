
# get over fact we do not use python 3.5+
def combine_dicts(dicts):
    new_dict = {}
    for d in dicts:
        for k in d:
            new_dict[k] = d[k]
    return new_dict