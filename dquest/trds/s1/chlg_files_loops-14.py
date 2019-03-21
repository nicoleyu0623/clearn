
fn="dq_unisex_names.csv"
f = open(fn, mode="rt", encoding='utf-8')
names = f.read()
f.close()

names_list = names.split('\n')
first_five = names_list[:5]
print(first_five)

nested_list = [el.split(',') for el in names_list ]

#print(nested_list[:4])

numerical_list = [ [x[0], float(x[1])] for x in nested_list  ]

#print(numerical_list[:4])

thousand_or_greater = [x[0] for x in numerical_list if x[1] > 1000]

print(thousand_or_greater[:10])