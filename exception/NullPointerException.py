class NullPointerException(Exception):
    def __init__(self, message="Null value found for a required field!"):
        self.message = message
        super().__init__(self.message)