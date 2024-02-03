# Global scope
my_global = 10

def fn1():
    local_v = 5
    print("Access to global:",my_global)
    # Local scope access
    print("Access to local:",local_v)


fn1()
# Local scope restrictions/ Will return an error
print("Can't access the local scope",local_v)