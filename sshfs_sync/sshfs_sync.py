import sys
import subprocess
import pipes
import os

# configration
host = 'your_host'
usr_name = 'user_name on remote server'

def exists_remote(host, path):
    """Test if a file exists at path on a host accessible with SSH."""
    status = subprocess.call(
        ['ssh', host, 'test -e {}'.format(pipes.quote(path))])
    if status == 0:
        return True
    if status == 1:
        return False
    raise Exception('SSH failed')

def help():
    print("""Usage:
python sshfs_sync path/on/romote/host""")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        help()
        sys.exit(-1)

    dir_name = os.path.split(sys.argv[1])[-1]
    ssh_host = usr_name + '@' + host
    usr_home = '/home/' + usr_name

    path = os.path.join(usr_home, sys.argv[1])

    status = exists_remote(ssh_host, path)

    if not status:
        print('Cannot find {} on remote {}'.format(path, ssh_host))
        sys.exit(-1)

    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

    command = 'sshfs {}:{} {}'.format(ssh_host, path, dir_name)
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    if error is not None:
        print('error occurs!')
        sys.exit(-1)
