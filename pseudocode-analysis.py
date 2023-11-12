def txt_analysis(parameter):
    index = 0
    command = ""
    with open("pseudocode.txt", "r") as f:
        code_list = f.readlines()
        if parameter == 1:
            for i in code_list:
                for x in i:
                    if x == " ":
                        break
                    else:
                        command+=x
        elif parameter == 2:
            for i in code_list:
                for x in i:
                    if x == " " and index == 0:
                        index += 1
                    elif index == 0 and x != " ":
                        pass
                    elif index == 1:
                        if x == ":" or x == "(":
                            break
                        else:
                            command+=x
        f.close()
    return command

class command_analysis:
    def __init__(self, first_command, second_command) -> None:
        self.first_command = first_command
        self.second_command = second_command
        self.command_interpreter = ""
    def first(self, first_command):
        if self.first_command == "declare":
            self.command_interpreter = "variable"
        elif self.first_command == "function":
            self.command_interpreter = "def"
        elif self.first_command == "procedure":
            self.command_interpreter = "def"
        else:
            self.command_interpreter = -1
        return self.command_interpreter
    def second(self, second_command):
        if self.command_interpreter == "variable":
            return second_command

class generate_code:
    def __init__(self, type, name, path) -> None:
        self.type = type
        self.name = name
        self.path = path
    def code(self):
        if self.type == "variable":
            python_code = self.name + " = " + "0"
        return python_code
    def write_file(self, code):
        with open(self.path, "w") as f:
            f.write(code)
            f.close()
command1 = txt_analysis(1)
command2 = txt_analysis(2)
analysis = command_analysis(command1, command2)
final_command = analysis.first(command1)
command = analysis.second(command2)
final_code = generate_code(final_command, command, "pycode.txt")
code = final_code.code()
final_code.write_file(code)