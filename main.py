# main.py

def saludar(name):
    print(f"Hello, {name}")

def add(a, b):
    return a + b

def main():
    saludar("World")
    result = add(1, 2)
    print(f"The result is {result}")

if __name__ == "__main__":
    main()