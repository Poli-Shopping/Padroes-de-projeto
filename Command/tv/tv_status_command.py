from command import Command
from .tv import TV

class TVStatusCommand(Command):

    def __init__(self, tv:TV) -> None:
        self.tv = tv

    def execute(self):
        print(self.tv)

    def undo(self):
        print("Essa classe não possui um método undo.")
