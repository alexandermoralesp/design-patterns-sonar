class UniqueMeta(type):
    __instances = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls.__instances:
            instance = super().__call__(*args, **kwds)
            cls.__instances[cls] = instance
        return cls.__instances[cls]

class Unique(metaclass=UniqueMeta):
    def some_business_logic(self):
        print("Do some business logic here")