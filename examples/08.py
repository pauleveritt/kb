class Greeter:
    fmt = 'Hi there, {}'

    def greet(self, name: str) -> str:
        return self.fmt.format(name)


greeting = Greeter()
greeting.fmt = 42
print(greeting.greet('jane'))
