from sys import argv, path
import os
import shutil

# file given in os args
#
# append folder path
#
# write file
#
# todo: folder backups
#


if __name__ == '__main__':
    _argv = argv.copy()
    del (_argv[0])

    try:
        os.mkdir("backup", 0o666)
    except OSError as error:
        print(error)
        input(f"{error}\n")

    for arg in [e for e in _argv]:
        _dir, file = path.split(arg)
        print(_dir + "/backup/" + file)

        with open(file, "rb") as a_file:
            with open(_dir + "/backup/" + file, "wb") as write_file:
                write_file.write(a_file.read())
    input("")


def move_file(file_name, src, destination):
    for dirpath, dirnames, fnames in os.walk(src):
        for afile in fnames:
            if afile.endswith(file_name):
                shutil.copy(os.path.join(dirpath, afile), destination)

