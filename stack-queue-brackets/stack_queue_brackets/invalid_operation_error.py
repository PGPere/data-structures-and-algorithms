class InvalidOperationError(Exception):

    def __init__(self) -> None:
        self.message = "Method not allowed on empty collection"

    def __str__(self):
        return self.message
