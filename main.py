import os
import sys

# file given in os args
#
# append folder path
#
# write file
#
# todo: folder backups
#


if __name__ == '__main__':
    try:
        os.mkdir("backup", 0o666)
    except OSError as error:
        print(error)

    del(sys.argv[0])
    for arg in [e for e in sys.argv]:
        _dir, file = os.path.split(arg)
        with open(file, "rb") as a_file:
            print(_dir + "/backup/" + file)
            with open(_dir + "/backup/" + file, "wb") as write_file:
                write_file.write(a_file.read())
    input("")
