# Type your code here

auto_service_dict = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12}

print('Davy\'s auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12')
print('')
service_one = input('Select first service: ')
print('')
print('')
service_two = input('Select second service: ')
print('')
print('')
print('')
print('Davy\'s auto shop invoice')
print('')
if service_one in auto_service_dict:
    print('Service 1: %s, $%d' %(service_one, auto_service_dict[service_one]))
elif service_one == '-':
    print('Service 1: No service')
else:
    print('Not a service')
if service_two in auto_service_dict:
    print('Service 2: %s, $%d' %(service_two, auto_service_dict[service_two]))
elif service_two == '-':
    print('Service 2: No service')
else:
    print('Not a service')
print('')


if (service_one != '-') and (service_two != '-'):
    print('Total: $%d' % (auto_service_dict[service_one]+auto_service_dict[service_two]))
elif service_one == '-':
    print('Total: $%d' % (auto_service_dict[service_two]))
elif service_two == '-':
    print('Total: $%d' % (auto_service_dict[service_one]))
else:
    print('Please speak to a representative for a list of available services')