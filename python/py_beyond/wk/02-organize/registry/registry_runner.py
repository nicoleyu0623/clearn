import registry


registry.register('reg value A')

print('checking after update 1')
for name in registry.registered_names():
    print(name)


import registry  #registry.py is imported only once

registry.register('reg value B')


print('checking after update 2')
for name in registry.registered_names():
    print(name)

