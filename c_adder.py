def color_adder(color1, color2, return_as_string=True):
	
    if type(color1) == str:
        color1 = int("0x"+color1[1:], 16)

    if type(color2) == str:
        color2 = int("0x"+color2[1:], 16)

    added = hex(int(color1) + int(color2))
	
    if return_as_string: 
        return ("#" + str(added)[2:])
    else:
        return added
