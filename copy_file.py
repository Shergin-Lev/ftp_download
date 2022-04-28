import paramiko
import os
from sftp_connect import SftpConnect


class CopyFile:
    def __init__(self, config, window):
        self.username = config.username
        self.host = config.server_host
        self.port = config.server_port
        self.password = config.password
        self.folders = config.server_folders
        self.local_folder = config.local_folder
        self.storage_time_days = config.storage_time_days
        self.window = window
        self.create_local_folder()

    def create_local_folder(self):
        if not os.path.exists(self.local_folder):
            os.mkdir(self.local_folder)

    # def get_connect(self):
    #     transport = paramiko.Transport((self.host, self.port))
    #     transport.connect(username=self.username,
    #                       password=self.password)
    #
    #     return paramiko.SFTPClient.from_transport(transport), transport

    def get_server_files_list(self, folder, connect) -> list:
        files = connect.listdir(folder)
        return files

    def get_local_files_list(self) -> list:
        for _, _, files in os.walk(self.local_folder):
            return files

    def copy_files(self):
        sftp_connect = SftpConnect(username=self.username,
                                   host=self.host,
                                   port=self.port,
                                   password=self.password)
        sftp_connect = sftp_connect.get_connect()
        local_files = self.get_local_files_list()

        for folder in self.folders:
            # TODO: Try Except на переход в папку
            sftp_connect.chdir(folder)
            server_files = self.get_server_files_list(folder, sftp_connect)
            diff_files = set(server_files) - set(local_files)
            print(list(diff_files)[:5])

        sftp_connect.sftp_disconnect()

    # def sftp_disconnect(self, connect, transport):
    #     connect.close()
    #     transport.close()

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