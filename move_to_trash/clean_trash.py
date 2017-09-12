import os, sys, shutil
from config import DST_DIR


TRASH_DIR = DST_DIR


if __name__ == '__main__':
    if not os.path.exists(TRASH_DIR):
        print('Cannot find given trash directory: {}'.format(TRASH_DIR))
        sys.exit(1)
    cnt = 0
    for name in os.listdir(TRASH_DIR):
        full_path = os.path.join(TRASH_DIR, name)
        if os.path.isfile(full_path):
            os.unlink(full_path)
            print('remove the file: {}'.format(full_path))
            cnt += 1
        elif os.path.isdir(full_path):
            shutil.rmtree(full_path)
            print('remove the directory: {}'.format(full_path))
            cnt += 1

    print('-' * 30)
    print('totally delete files/diretories: {}'.format(cnt))

