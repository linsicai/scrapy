from ftplib import error_perm

from posixpath import dirname

# cwd 到指定目录，如不存在则自动创建
def ftp_makedirs_cwd(ftp, path, first_call=True):
    """Set the current directory of the FTP connection given in the `ftp`
    argument (as a ftplib.FTP object), creating all parent directories if they
    don't exist. The ftplib.FTP object must be already connected and logged in.
    """

    try:
        # 尝试cd
        ftp.cwd(path)

    except error_perm:
        # 尝试cd子目录
        ftp_makedirs_cwd(ftp, dirname(path), False)

        # 创建当前目录
        ftp.mkd(path)

        # cd目录
        if first_call:
            ftp.cwd(path)
