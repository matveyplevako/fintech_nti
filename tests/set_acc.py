from sys import argv

with open('account_id', 'w') as id:
    id.write(argv[1])
print("set to " + argv[1])