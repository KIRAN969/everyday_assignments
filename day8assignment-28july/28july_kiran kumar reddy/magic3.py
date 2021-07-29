class Example:
    def __init__(self):
        print("instance created")
    def __call__(self):
        print("instance is called via speciall method")
e=Example()
e()
    