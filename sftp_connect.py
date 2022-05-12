import paramiko


class SftpConnect:
    def __init__(self, username, host, port, password):
        self.username = username
        self.password = password
        print(host)
        self.transport = paramiko.Transport(host, port)
        self.sftp = None

    def get_connect(self):
        self.transport.connect(username=self.username, password=self.password)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)

    def sftp_disconnect(self):
        self.transport.close()
