class Sample:
    def __enter__(self):
        print("start...")
        # 获取资源
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        print("end...")

    def do_something(self):
        print("doing something")

with Sample() as sample:
    sample.do_something()