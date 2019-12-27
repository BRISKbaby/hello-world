class HelloWorld:
    def __init__(self, name: str):
        print(f"Hello world, I am from the class: {self.__class__.__name__}")
        print(f"I bring you {name}.")

    def shout(self, msg: str = None):
        if msg:
            print(f"My message is: {msg}.")
        else:
            print("No message given.")


if __name__ == "__main__":
    hw1 = HelloWorld("peace")
    hw2 = HelloWorld("love")
