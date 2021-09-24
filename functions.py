from CONST import SWAP_DICT


def replace(x: str):
    if x is None:
        return 'Wanni chi kaim chalan'
		
    for key, value in SWAP_DICT.items():
        x = x.replace(key, value)

    return x
