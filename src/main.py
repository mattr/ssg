import os
import shutil

def clean(target):
    if os.path.exists(target):
        shutil.rmtree(target)

def create(target):
    if not os.path.exists(target):
        os.mkdir(target)

def copy(source, target):
    for item in os.listdir(source):
        if os.path.isfile(os.path.join(source, item)):
            shutil.copy(os.path.join(source, item), os.path.join(target, item))
        else:
            next_source = os.path.join(source, item)
            next_target = os.path.join(target, item)
            if not os.path.exists(next_target):
                os.mkdir(next_target)
            copy(next_source, next_target)


def main():
    cwd = os.getcwd()

    source = os.path.join(cwd, "static")
    target = os.path.join(cwd, "public")

    clean(target)
    create(target)
    copy(source, target)

main()
