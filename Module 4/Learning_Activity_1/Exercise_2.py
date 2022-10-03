party = {
    'money': 1000,
    'cake': ['cheesecake', 'sponge cake', 'flourless cake', 'biscuit cake'],
    'guests': ['Bob', 'Alicia', 'Eve', 'Tom', 'Harry'],
    'venue': ['outdoor', 'indoor']
}
# To add a key 'gifts' with the given string values
party['gifts'] = ['phone', 'laptop', 'camera', 'DIY card', 'chocolates']
# To add $500 more to 'money'
party['money'] = party['money'] + 500
# To remove Bob from the 'guests' list
party['guests'].remove('Bob')
# To check all the updates
print(party)
