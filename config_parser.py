import configparser
import os


class Config:
    __CONFIG_FILE = 'config.ini'
    server_host = ''
    server_port = '22'
    username = ''
    password = ''
    server_folders = []
    server_folder_descriptions = []
    local_folder = ''
    storage_time_days = 30
    refresh_rate_seconds = 5

    def __init__(self):
        self.read_config_file()

    def __create_config_file(self, path):
        config_pars = configparser.ConfigParser()
        config_pars.add_section('SFTP_settings')
        config_pars.set('SFTP_settings', 'server_host', '')
        config_pars.set('SFTP_settings', 'server_port', '22')
        config_pars.set('SFTP_settings', 'username', '')
        config_pars.set('SFTP_settings', 'secret', '')
        config_pars.add_section('SERVER_folders')
        config_pars.set('SERVER_folders', 'folder1', '')
        config_pars.add_section('SERVER_folder_descriptions')
        config_pars.set('SERVER_folder_descriptions', 'description1', '')
        config_pars.add_section('LOCAL_folder')
        config_pars.set('LOCAL_folder', 'folder', '')
        config_pars.add_section('ARCHIVE_settings')
        config_pars.set('ARCHIVE_settings', 'storage_time_days', '30')
        config_pars.set('ARCHIVE_settings', 'refresh_rate_seconds', '5')
        with open(path, 'w') as config_file:
            config_pars.write(config_file)

    def read_config_file(self):
        if not os.path.exists(self.__CONFIG_FILE):
            self.__create_config_file(self.__CONFIG_FILE)
        config_pars = configparser.ConfigParser()
        config_pars.read(self.__CONFIG_FILE)
        self.server_host = config_pars.get('SFTP_settings', 'server_host')
        # TODO: Добавить проверку int для server_port
        self.server_port = int(config_pars.get('SFTP_settings', 'server_port'))
        self.username = config_pars.get('SFTP_settings', 'username')
        self.password = config_pars.get('SFTP_settings', 'secret')
        self.server_folders = [item[1] for item in config_pars.items('SERVER_folders')]
        self.server_folder_descriptions = [item[1] for item in config_pars.items('SERVER_folder_descriptions')]
        self.local_folder = config_pars.get('LOCAL_folder', 'folder')
        self.storage_time_days = int(config_pars.get('ARCHIVE_settings', 'storage_time_days'))
        self.refresh_rate_seconds = int(config_pars.get('ARCHIVE_settings', 'refresh_rate_seconds'))


if __name__ == '__main__':
    config = Config()
    print(config.username)
