import logging
import unittest

class mainClass:
    def __init__(self, file, mode):
        self.file = file
        self.mode = mode
        self.counter = 0
        self.logger = logging.getLogger(__name__)

    def __enter__(self):
        self.file = open(self.file, self.mode)
        self.counter += 1
        self.logger.info(f'Opened file: {self.file}')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        self.counter -= 1
        self.logger.info(f'Closed file: {self.file}')
        if self.counter == 0:
            self.logger.info('All files closed')


logging.basicConfig(level=logging.INFO)

# Example usage
with mainClass('example.txt', 'w') as file:
    file.write('asdfghjkl')

with mainClass('example.txt', 'r') as file:
    contents = file.read()
    print(contents)


