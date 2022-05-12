import paramiko
import os
from sftp_connect import SftpConnect


class CopyFile:
    def __init__(self, config, window):
        self.folders = config.server_folders
        self.local_folder = config.local_folder
        self.storage_time_days = config.storage_time_days
        self.window = window
        self.create_local_folder()
        self.sc = SftpConnect(username=config.username,
                              host=config.server_host,
                              port=config.server_port,
                              password=config.password)

    def create_local_folder(self):
        if not os.path.exists(self.local_folder):
            os.mkdir(self.local_folder)

    def get_server_files_list(self, folder) -> list:
        files = self.sc.sftp.listdir(folder)
        return files

    def get_local_files_list(self) -> list:
        for _, _, files in os.walk(self.local_folder):
            return files

    def copy_files(self):
        self.sc.get_connect()
        local_files = self.get_local_files_list()

        for folder in self.folders:
            # TODO: Try Except на переход в папку
            self.sc.sftp.chdir(folder)
            server_files = self.get_server_files_list(folder)
            diff_files = set(server_files) - set(local_files)
            print(list(diff_files)[:5])

        self.sc.sftp_disconnect()

    def del_old_files(self):
        pass


# host = "example.com"
# port = 22
# transport = paramiko.Transport((host, port))
# transport.connect(username='login', password='password')
# sftp = paramiko.SFTPClient.from_transport(transport)
#
# remotepath = '/path/to/remote/file.py'
# localpath = '/path/to/local/file.py'
#
# sftp.get(remotepath, localpath)
# sftp.put(localpath, remotepath)
#
# sftp.close()
# transport.close()