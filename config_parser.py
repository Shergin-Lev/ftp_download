import configparser
import os


class Config:
    __CONFIG_FILE = 'config.ini'
    server_host = ''
    username = ''
    password = ''
    server_folders = []
    local_folder = ''
    config_dict = {}
    storage_time_days = 30
    refresh_rate_seconds = 5

    def __init__(self):
        self.read_config_file()

    def create_config_file(self, path):
        config_pars = configparser.ConfigParser()
        config_pars.add_section('SFTP_settings')
        config_pars.set('SFTP_settings', 'server_host', '')
        config_pars.set('SFTP_settings', 'username', '')
        config_pars.set('SFTP_settings', 'secret', '')
        config_pars.add_section('SERVER_folders')
        config_pars.set('SERVER_folders', 'folder1', '/123456789/AIR/')
        config_pars.add_section('LOCAL_folder')
        config_pars.set('LOCAL_folder', 'folder', 'C:/AIR/')
        config_pars.add_section('ARCHIVE_settings')
        config_pars.set('ARCHIVE_settings', 'storage_time_days', '30')
        config_pars.set('ARCHIVE_settings', 'refresh_rate_seconds', '5')
        with open(path, 'w') as config_file:
            config_pars.write(config_file)

    def read_config_file(self):
        if not os.path.exists(self.__CONFIG_FILE):
            self.create_config_file(self.__CONFIG_FILE)
        config_pars = configparser.ConfigParser()
        config_pars.read(self.__CONFIG_FILE)

        self.server_host = config_pars.get('SFTP_settings', 'server_host')
        self.username = config_pars.get('SFTP_settings', 'username')
        self.password = config_pars.get('SFTP_settings', 'secret')
        self.server_folders = [item[1] for item in config_pars.items('SERVER_folders')]
        self.local_folder = config_pars.get('LOCAL_folder', 'folder')
        self.storage_time_days = config_pars.get('ARCHIVE_settings', 'storage_time_days')
        self.refresh_rate_seconds = config_pars.get('ARCHIVE_settings', 'refresh_rate_seconds')


    def get_config(self):
        return self.read_config_file


if __name__ == '__main__':
    config = Config()
