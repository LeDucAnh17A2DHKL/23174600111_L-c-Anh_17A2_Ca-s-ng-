# Bắt đầu với inventory đã được cho
inventory = {
'gold': 500,
'pouch': ['flint', 'twine', 'gemstone'],
'backpack': ['xylophone','dagger', 'bedroll', 'bread loaf']
}

# Thêm 'pocket' vào dictionary với danh sách các mục
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

# Sắp xếp các mục trong danh sách 'backpack'
inventory['backpack'].sort()

# Loại bỏ 'dagger'
if 'dagger' in inventory['backpack']:
    inventory['backpack'].remove('dagger')

# Thêm 50 vào 'gold' key
inventory['gold'] = inventory['gold'] + 50

# In ra inventory để kiểm tra
print(inventory)