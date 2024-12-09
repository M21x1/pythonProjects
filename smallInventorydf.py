import pandas as pd

inventory = pd.read_csv('inventory.csv')

inventory.head(10)

staten_island = inventory.head(10).copy()

product_request = staten_island.product_description

#print(product_request)

seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')] # do not forget the parenthesis

#print(seed_request)

inventory['in_stock'] = inventory.quantity.apply(lambda x: True if x > 0 else False )

#print(inventory.in_stock)

inventory['total_value'] = inventory.price * inventory.quantity

print(inventory)

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

inventory['full_description'] = inventory.apply(combine_lambda, axis = 1) # do not forget to specify the axis = 1 to get outputs in rows

print(inventory)