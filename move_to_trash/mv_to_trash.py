#!/usr/bin/env python
import os, sys, shutil, glob
import time
from time import localtime, strftime

from config import DST_DIR
def get_cur_time_as_string():
    return strftime('%H-%M-%S@%Y-%m-%d', localtime())

def mv_src_file(name, dst):
    if os.path.isfile(name):
        file_type = 'file'
    elif os.path.isdir(name):
        file_type = 'directory'
    else:
        file_type = 'unknown'
    # to avoid rm files with the same name in the DST_DIR
    pure_name = os.path.split(name)[1]
    dst_name = os.path.join(DST_DIR, pure_name)
    # mv directly
    if not os.path.exists(dst_name):
        shutil.move(name, dst_name)
    else:
        name_with_time = pure_name + '@' + get_cur_time_as_string()
        dst_name = os.path.join(DST_DIR, name_with_time)
        shutil.move(name, dst_name)

    print('mv {} {} to {}'.format(file_type, name, dst_name))


if __name__ == '__main__':
    if not os.path.exists(DST_DIR):
        print('Cannot find dst dir: {}'.format(DST_DIR))
        sys.exit(1)
    argc = len(sys.argv)
    if argc == 1:
        print('File/Directory name(s) should be given')
        sys.exit(1)
    else:
        src_names = sys.argv[1:]
        if len(src_names) > 1:
            print('multi files will be moved. total number: {}'.format(len(src_names)))
            print('-' * 30)
        for src_name in src_names:
            if not os.path.exists(src_name):
                print('Cannot find src file: {}, Stop!'.format(src_name))
                sys.exit(1)
            else:
                mv_src_file(src_name, DST_DIR)

        sys.exit(0)
