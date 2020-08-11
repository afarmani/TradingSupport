def cal_tr(d, c, h, l, o, pc):
    x = h - l
    y = abs(h - pc)
    z = abs(l - pc)

    if y <= x >= z:
        tr = x
    elif x <= y >= z:
        tr = y
    elif x <= z >= y:
        tr = z
    return d, tr


class SetupAtr:
    def __init__(self, window):
        self.window = window
        self.setup_atr()

    def setup_atr(self):
        any()
