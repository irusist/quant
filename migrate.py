import os
import shutil

if __name__ == 'main':
    base_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_path, "data", "xueqiu", "hk")
    dest_path = os.path.join(base_path, "backup", "xueqiu", "hk")
    shutil.move(data_path, dest_path)


def move(src, dest):
    shutil.move(src, dest)


def copy(src, dest):
    shutil.copy(src, dest)