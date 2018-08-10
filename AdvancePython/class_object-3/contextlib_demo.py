import contextlib

@contextlib.contextmanager
def file_open(file_name):
    print("open")
    yield {}
    print("end")

with file_open("abc") as fp:
    print("file processing")