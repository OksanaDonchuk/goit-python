class Meta(type):

    children_number = 0

    def __new__(mcs, name, bases, attrs):
        attrs['class_number'] = mcs.children_number
        mcs.children_number += 1
        return super(Meta, mcs).__new__(mcs, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        super(Meta, cls).__init__(name, bases, attrs)


Meta.children_number = 0


class Cls1(metaclass=Meta):

    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):

    def __init__(self, data):
        self.data = data


assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(''), Cls2('')
assert (a.class_number, b.class_number) == (0, 1)
print(a.class_number)
print(b.class_number)
