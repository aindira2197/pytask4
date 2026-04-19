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

    def read_file(self):
        if self.file:
            return self.file.read()
        return None

    def write_file(self, content):
        if self.file:
            self.file.write(content)

    def read_lines(self):
        if self.file:
            return self.file.readlines()
        return None

def main():
    filename = 'example.txt'
    with CustomFileManager(filename, 'w') as file:
        file.write('Hello, World!')
    with CustomFileManager(filename, 'r') as file:
        print(file.read())

    with CustomFileManager(filename, 'a') as file:
        file.write('\nThis is a new line')

    with CustomFileManager(filename, 'r') as file:
        print(file.read())

if __name__ == '__main__':
    main()

class CustomFileManagerWithErrorHandling:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
            return self.file
        except Exception as e:
            print(f'Error opening file: {e}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            try:
                self.file.close()
            except Exception as e:
                print(f'Error closing file: {e}')

    def read_file(self):
        if self.file:
            try:
                return self.file.read()
            except Exception as e:
                print(f'Error reading file: {e}')
        return None

    def write_file(self, content):
        if self.file:
            try:
                self.file.write(content)
            except Exception as e:
                print(f'Error writing file: {e}')

    def read_lines(self):
        if self.file:
            try:
                return self.file.readlines()
            except Exception as e:
                print(f'Error reading lines: {e}')
        return None

def main_with_error_handling():
    filename = 'example.txt'
    with CustomFileManagerWithErrorHandling(filename, 'w') as file:
        file.write('Hello, World!')
    with CustomFileManagerWithErrorHandling(filename, 'r') as file:
        print(file.read())

    with CustomFileManagerWithErrorHandling(filename, 'a') as file:
        file.write('\nThis is a new line')

    with CustomFileManagerWithErrorHandling(filename, 'r') as file:
        print(file.read())

if __name__ == '__main__':
    main()
    main_with_error_handling()