tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}

def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}

def assign_food_items(table_number, **order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks

print(' --- tables available --- \n')
assign_table(2, 'Douglas', True)
assign_table(3, "Arwa", True)
assign_table(4, 'Jiho')
assign_food_items(4, drinks='Orange Juice, Apple Juice')
assign_food_items(3, food='Steak, Seabass', drinks='Wine Bottle')
assign_food_items(2, food='Seabass, Gnocchi, Pizza', drinks='Margarita, Water')
print(tables)
