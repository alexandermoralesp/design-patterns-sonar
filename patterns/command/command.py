"""
Command Pattern
"""
from abc import ABC, abstractmethod

class EditorInterface(ABC):
    @abstractmethod
    def do_A(self):
        ...

    @abstractmethod
    def do_B(self):
        ...

    @abstractmethod
    def do_C(self):
        ...


class Editor(EditorInterface):
    def do_A(self):
        ...

    def do_B(self):
        ...

    def do_C(self):
        ...


class Command(ABC):
    @abstractmethod
    def execute():
        # Abstract method
        ...


class ConcreteCommandA(Command):
    def __init__(self, editor: EditorInterface):
        self._editor = editor

    def execute(self):
        print("Command A")
        self._editor.do_A()


class ConcreteCommandB(Command):
    def __init__(self, editor: EditorInterface):
        self._editor = editor

    def execute(self):
        print("Command B")
        self._editor.do_B()


class ConcreteCommandC(Command):
    def __init__(self, editor: EditorInterface):
        self._editor = editor

    def execute(self):
        print("Command C")
        self._editor.do_C()


class Application:
    def __init__(self, command_a: Command, command_b: Command, command_c: Command):
        self._command_a = command_a
        self._command_b = command_b
        self._command_c = command_c

    def do_first(self):
        self._command_a.execute()
        self._command_b.execute()

    def do_second(self):
        self._command_b.execute()
        self._command_c.execute()


if __name__ == "__main__":
    editor = Editor()
    concrete_command_a = ConcreteCommandA(editor)
    concrete_command_b = ConcreteCommandB(editor)
    concrete_command_c = ConcreteCommandC(editor)
    app = Application(concrete_command_a,
                      concrete_command_b, concrete_command_c)
    app.do_first()
    app.do_second()
