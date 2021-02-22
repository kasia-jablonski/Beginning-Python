class Protected:
    __name = "Security"

    def __method(self):
        return self.__name

prot = Protected()
# can't be accessed by prot.__method()
prot._Protected__method() 