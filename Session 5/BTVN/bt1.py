inventory = {
    'gold': 500,
    'pounch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket'] = ['seashell', 'strange berry', 'lint']

del inventory ['backpack'][1]

inventory ['gold'] = [ inventory['gold'], 50 ]

print (inventory)
