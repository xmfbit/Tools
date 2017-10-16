Tools and configurations
---------------
## Move to trash instead of `rm`
`rm` is dangerous. This is an alternative of `rm` command. By setting alias in .bashrc/.zshrc, execute corresponding python scripts to safely move the files into a specific trash directory.

Give yourself a chance to fix the mistake!

## Sync file with `sshfs` command tool
`sshfs`(see [sshfs](https://github.com/osxfuse/sshfs) for detail) is a filesystem client based on the SSH File Transfer Protocol, especially useful when need to sync files with a remote server frequently.

With this script, it is easy to make a mirror file system for remote files. When typing:
```
python sshfs_sync.py /some/pth/on/remote/server
```
it has the same effect with the following commands:
```
mkdir /the/tail/directory
sshfs user@remote:$HOME/some/pth/on/remote/server ./the/tail/directory
```
