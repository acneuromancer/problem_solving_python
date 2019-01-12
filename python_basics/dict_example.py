my_dict = {"Jim": 10, "Tim": 20, "John" : 30}
my_dict['Sam'] = 40
for k in my_dict:
    print('%s is %d year(s) old' % (k, my_dict[k]))

prices = {"apple" : 100, "melon" : 150, "pear" : 200}
item_dict = {"item":"melon", "cost":24}
print("The %(item)s costs %(cost)7.1f cents" % item_dict)

phone_reg = {'Tim':1111, 'Jim':2222, 'Sam':3333}
if 'Sam' in phone_reg:
    print("Sam's phone number is %d" % (phone_reg['Sam']))

print('John' in phone_reg)
