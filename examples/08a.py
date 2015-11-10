from typing import Union


class Greeter:
    fmt = 'Hi there, {}'  # type Union[str, bool]

    def greet(self, name: str) -> str:
        return self.fmt.format(name)


greeting = Greeter()
greeting.fmt = 42
print(greeting.greet('jane'))
