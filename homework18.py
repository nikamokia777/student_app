class Mymeta(type):
    def __new__(mcls, name, bases, attrs):
        for key, value in attrs.items():
            if callable(value):
                if not key.startswith('_'):
                    raise ValueError(f"Method {key} must start with '_'")

        return super().__new__(mcls, name, bases, attrs)


class First(metaclass=Mymeta):
    def _gamarjoba(self):
        print("hello")

    def _nakhvamdis(self):
        print("goodbye")

    person = "buba"