class Display:
    def __init__(self, id, message="", is_on=False):
        self.id = id
        self.message = message
        self.is_on = is_on

    def __str__(self):
        return f"Display {self.id}: {self.message}"

    def update(self, data):
        if "message" in data:
            self.message = data["message"]
        for key, value in data.items():
            print(f" - {key}: {value}")

