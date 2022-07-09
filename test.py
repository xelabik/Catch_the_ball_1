


def print_hi(name: str)-> None:
    print(f"Hi {name}") 

if __name__ == "__main__":
    friends: list = ["Dima", "Demon"]
    friends_str: str = ", ".join(friends)
    print_hi(name=friends_str)

