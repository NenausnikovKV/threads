"""Clear directory"""
import os


def clear_dir(dir_path):
    """Remove all files from directory."""
    for (_, __, file_names) in os.walk(dir_path):
        for file_name in file_names:
            os.remove(os.path.join(dir_path, file_name))


if __name__ == '__main__':
    clear_dir(dir_path="files")
