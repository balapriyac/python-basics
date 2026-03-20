

class Document:
    def __init__(self):
        self.content = ""

    def insert(self, text: str, position: int) -> None:
        self.content = (
            self.content[:position] + text + self.content[position:]
        )

    def delete(self, position: int, length: int) -> None:
        self.content = (
            self.content[:position] + self.content[position + length:]
        )

    def show(self) -> None:
        print(f'Document: "{self.content}"')

from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass

class InsertCommand(Command):
    def __init__(self, document: Document, text: str, position: int):
        self.document = document
        self.text = text
        self.position = position

    def execute(self) -> None:
        self.document.insert(self.text, self.position)

    def undo(self) -> None:
        self.document.delete(self.position, len(self.text))

class DeleteCommand(Command):
    def __init__(self, document: Document, position: int, length: int):
        self.document = document
        self.position = position
        self.length = length
        self._deleted_text = ""  # stored on execute, used on undo

    def execute(self) -> None:
        self._deleted_text = self.document.content[
            self.position : self.position + self.length
        ]
        self.document.delete(self.position, self.length)

    def undo(self) -> None:
        self.document.insert(self._deleted_text, self.position)

class EditorInvoker:
    def __init__(self):
        self._history: list[Command] = []

    def run(self, command: Command) -> None:
        command.execute()
        self._history.append(command)

    def undo(self) -> None:
        if not self._history:
            print("Nothing to undo.")
            return
        command = self._history.pop()
        command.undo()
        print("Undo successful.")

doc = Document()
editor = EditorInvoker()

# Type a title
editor.run(InsertCommand(doc, "Quarterly Report", 0))
doc.show()

# Add a subtitle
editor.run(InsertCommand(doc, " - Finance", 16))
doc.show()

# Oops, wrong subtitle — undo it
editor.undo()
doc.show()

# Delete "Quarterly" and replace with "Annual"
editor.run(DeleteCommand(doc, 0, 9))
doc.show()

editor.run(InsertCommand(doc, "Annual", 0))
doc.show()

# Undo the insert
editor.undo()
doc.show()

# Undo the delete (restores "Quarterly")
editor.undo()
doc.show()

class MacroCommand(Command):
    def __init__(self, commands: list[Command]):
        self.commands = commands

    def execute(self) -> None:
        for cmd in self.commands:
            cmd.execute()

    def undo(self) -> None:
        for cmd in reversed(self.commands):
            cmd.undo()

# Apply a heading format in one shot: clear content, insert formatted title
macro = MacroCommand([
    DeleteCommand(doc, 0, len(doc.content)),
    InsertCommand(doc, "== Annual Report ==", 0),
])

editor.run(macro)
doc.show()

editor.undo()
doc.show()

