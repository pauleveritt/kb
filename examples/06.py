class Greeter:
    def __init__(self, fmt: str):
        self.fmt = fmt

    def say_hi(self, name: str) -> str:
        return self.fmt.format(name)


greeting = Greeter('Hello, {}')
greeting.greet('jane')
