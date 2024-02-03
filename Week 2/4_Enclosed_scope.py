# Global scope
my_global = 10


def fn1():
    enclosed_v = 8

    def fn2():
        local_v = 5
        print("Access to global:", my_global)
        # Local scope access
        print("Access to local:", local_v)

    fn2()


fn1()
