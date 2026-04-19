class CustomFileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

    def write(self, content):
        if self.file:
            self.file.write(content)
            self.file.flush()

    def read(self):
        if self.file:
            return self.file.read()

class FileManager:
    def __init__(self, filename, mode):
        self.manager = CustomFileManager(filename, mode)

    def open_file(self):
        return self.manager.__enter__()

    def close_file(self):
        self.manager.__exit__(None, None, None)

    def write_to_file(self, content):
        self.manager.write(content)

    def read_from_file(self):
        return self.manager.read()

def main():
    filename = "example.txt"
    mode = "w+"
    file_manager = FileManager(filename, mode)
    file = file_manager.open_file()
    content = "Hello, World!"
    file_manager.write_to_file(content)
    file_manager.close_file()
    file_manager = FileManager(filename, "r")
    file = file_manager.open_file()
    print(file_manager.read_from_file())
    file_manager.close_file()

if __name__ == "__main__":
    main()
    filename = "example2.txt"
    mode = "w+"
    with CustomFileManager(filename, mode) as file:
        file.write("Hello, World!")
    with CustomFileManager(filename, "r") as file:
        print(file.read())
        print(file.mode)
        print(file.name)