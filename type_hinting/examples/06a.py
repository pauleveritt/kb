

class Greeter:
    def __init__(self, fmt: str):
        self.fmt = fmt

    def greet(aself, name: str) -> str:
        return self.fmt.format(name)


greeting = Greeter('Hello, {}')
greeting.greet('jane')
