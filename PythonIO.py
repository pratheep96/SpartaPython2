# Python IO or Input Output for file handling

class ReadorWrite():

    def __init__(self, read, write):
        self.read = read
        self.write = write

    def file_opener(file):
        try:
            result = open(file, "r")
            list_lines = result.readlines()
            for line in list_lines:
                print(line+ "\n")
            result.close()
        except ValueError as msg:
            print("Something wrong occured", msg)
        except FileNotFoundError as errmsg:
            print("Something wrong occured", errmsg)
        except FileExistsError as errmsg:
            print("Something wrong occred", errmsg)

    def file_writer(file):
        try:
            result = open(file, "a")
            list_lines = result.write("jnkifwn")
            result.close()
        except ValueError as msg:
            print("Something wrong occured", msg)
        except FileNotFoundError as errmsg:
            print("Something wrong occured", errmsg)
        except FileExistsError as errmsg:
            print("Something wrong occred", errmsg)

    def perform_operation(self):
        if self.read == "r:":
            self.file_opener(self.file)
        else:
            self.file_writer(self.file)

file_operation=ReadorWrite("a", "my_file.txt")
file_operation.perform_operation()

    # file_writer("my_file1.txt")
    # file_opener("my_file1.txt")
