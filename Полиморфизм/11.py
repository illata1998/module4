from dispatcher import defmethod


# BEGIN
def init():
    defmethod(__name__, 'get_area', lambda self: self['data']['side'] ** 2)


def make(side):
    return {'name': __name__, 'data': {'side': side}}


def get_square_side(self):
    return self['data']['side']
# END
