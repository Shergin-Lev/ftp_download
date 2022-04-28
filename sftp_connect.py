import paramiko


class SftpConnect:
    def __init__(self, username, host, port, password):
        self.username = username
        self.host = host
        self.port = port
        self.password = password

    def get_connect(self):
        self.transport = paramiko.Transport((self.host, self.port))
        self.transport.connect(username=self.username,
                               password=self.password)
        self.connect = paramiko.SFTPClient.from_transport(self.transport)
        return self.connect

    def sftp_disconnect(self):
        self.connect.close()
        self.transport.close()
