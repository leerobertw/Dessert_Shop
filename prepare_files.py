import os
import shutil
import itertools
import glob
import re


def create_folders(dirname):
    files = glob.glob("*.py", root_dir=dirname)
    dirs = itertools.groupby(sorted(files), lambda file: file[0:file.find("_")])
    for key, group in dirs:
        new_dir = os.path.join(dirname, key)
        os.mkdir(new_dir)
        for filename in group:
            old_path = os.path.join(dirname, filename)
            new_path = os.path.join(dirname, key, filename)
            shutil.move(old_path, new_path)


def update_filename(dirname):
    home = os.getcwd()
    folders = os.listdir(dirname)
    for folder in folders:
        path = os.path.join(home, dirname, folder)
        os.chdir(path)
        student_files = os.listdir()
        for filename in student_files:
            new_filename = re.sub("^[a-z]+_[0-9]+_[0-9]+_", "", filename)
            new_filename = re.sub("-[]0-9]+\.py$", ".py", new_filename)
            os.rename(filename, new_filename)


def main():
    files_folder = "student files"
    create_folders(files_folder)
    update_filename(files_folder)


if __name__ == '__main__':
    main()
