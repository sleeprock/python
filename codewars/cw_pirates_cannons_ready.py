a = {'Mike':'aye','Joe':'aye','Johnson':'aye','Peter':'aye'}
b = {'Mike':'aye','Joe':'nay','Johnson':'aye','Peter':'aye'}

def cannons_ready(gunners):
    return [print('Fire!') if 'nay' not in gunners.values() else 'Shiver me timbers!']


cannons_ready(a)


""" if 'nay' not in b.values():
    print('Y')
else:
    print('N') """