"""
Write files using one or mane threads.
Compare processing time.
"""
import os
from threading import Thread
from time import perf_counter

from threads.rewrite_files.clear_files import clear_dir


class FilesWriter:
    """create files and rewrite with one or many threads"""
    def __init__(self, dir_path):
        self.dir_path = dir_path
        self.dir_file_paths = self._get_dir_file_paths(self.dir_path)

    def upgrade_dir(self, file_num=20000):
        """
        Clear directory and create files.
        Create given number files.
        """
        self._clear_dir()
        self._create_files(file_num)
        self.dir_file_paths = self._get_dir_file_paths(self.dir_path)

    def single_thread_file_replacing(self, old_substr, new_substr):
        """
        Replace all substr from old_substr to new_substr.
        One thread processing.
        """
        for file_path in self.dir_file_paths:
            self._replace_subst_for_files(file_path, old_substr, new_substr)

    def multi_thread_file_replacing(self, old_substr, new_substr):
        """
        Replace all substr from old_substr to new_substr.
        Multi thread processing. One thread processes one file.
        """
        threads = []
        for file_name in self.dir_file_paths:
            thread = Thread(target=self._replace_subst_for_files, args=(file_name, old_substr, new_substr))
            threads.append(thread)
        # запускаем потоки
        for thread in threads:
            thread.start()

        # ждем завершения потоков
        for thread in threads:
            thread.join()

    @staticmethod
    def _get_dir_file_paths(dir_path):
        """Get file paths for class instance directory path."""
        file_paths = []
        for (_, __, file_names) in os.walk(dir_path):
            for file_name in file_names:
                file_paths.append(os.path.join(dir_path, file_name))
        return file_paths

    @staticmethod
    def _replace_subst_for_files(file_path, old_substring, new_substring):
        """
        Rewrite all files.
        Replace given old substring to given new substring.
        """
        with open(file_path, "r", errors='ignore', encoding="utf-8") as file:
            content = file.read()
        content = content.replace(old_substring, new_substring)
        with open(file_path, "w", errors='ignore', encoding="utf-8") as file:
            file.write(content)

    def _clear_dir(self):
        """Remove all files from directory."""
        for file_path in self.dir_file_paths:
            os.remove(file_path)

    def _create_files(self, file_num):
        """Create file_count files."""
        for num in range(file_num):
            with open(os.path.join(self.dir_path, str(num)), "w", encoding="utf-8") as file:
                file.write("hello")


if __name__ == '__main__':
    writer = FilesWriter(dir_path="files")

    # create files
    start_time = perf_counter()
    writer.upgrade_dir(file_num=1000)
    end_time = perf_counter()
    print(f'Обновление файлов заняло {end_time - start_time:0.2f} секунд.')

    # single thread processing
    start_time = perf_counter()
    writer.single_thread_file_replacing("hello", "goodbye")
    end_time = perf_counter()
    print(f'Обработка одним потоком заняло {end_time - start_time:0.2f} секунд.')

    # multi thread processing
    start_time = perf_counter()
    writer.multi_thread_file_replacing("goodbye", "hello")
    end_time = perf_counter()
    print(f'Выполнение несколькими потоками заняло {end_time-start_time:0.2f} секунд.')

    # clear dir
    clear_dir(dir_path="files")
