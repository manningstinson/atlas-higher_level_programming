import dis
import types


def print_names(module):
    for name, value in module.__dict__.items():
        if not name.startswith("__"):
            print(name)


if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as file:
        code_object = compile(file.read(), "hidden_4.pyc", "exec")
        module = types.ModuleType("hidden_4")
        exec(code_object, module.__dict__)

    print_names(module)
