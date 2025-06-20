class Display:
    def __init__(self, id, message="", is_on=False):
        self.id = id
        self.message = message
        self.is_on = is_on

    def __str__(self):
        return f"Display {self.id}: {self.message}"

    def update(self, data):
        print(f"[Display {self.id}] Updated display with:")
        for key, value in data.items():
            print(f" - {key}: {value}")

