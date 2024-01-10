# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from fastapi import FastAPI
import subprocess

app = FastAPI()


class Config:
    def __init__(self, config_string):
        self.public = None
        self.preshared = None
        self.endpoint = None
        self.allowed_ips = None
        self.interface_address = None
        self.interface_privateKey = None
        self.interface_dns = None
        self.server_public_key = None

        lines = config_string.split('\n')
        for line in lines:
            if 'public: ' in line:
                self.public = line.split('public: ')[1]
            elif 'preshared: ' in line:
                self.preshared = line.split('preshared: ')[1]
            elif 'endpoint: ' in line:
                self.endpoint = line.split('endpoint: ')[1]
            elif 'allowed ips: ' in line:
                self.allowed_ips = line.split('allowed ips: ')[1]
            elif 'interface address: ' in line:
                self.interface_address = line.split('interface address: ')[1]
            elif 'interface privateKey: ' in line:
                self.interface_privateKey = line.split('interface privateKey: ')[1]
            elif 'interface dns: ' in line:
                self.interface_dns = line.split('interface dns: ')[1]
            elif 'server public key: ' in line:
                self.server_public_key = line.split('server public key: ')[1]


@app.post("/add_peer")
def run_add_peer_script():
    # script_path = '/Users/admin/Desktop/wg-fake.sh'
    script_path = '/root/wg-peer.sh add'
    try:
        result = subprocess.check_output(['sh', script_path], universal_newlines=True)
        print(result)
        config_string = result
        config = Config(config_string)
        print("Successully got new Peer!")
        print(config.public)
        print(config.preshared)
        print(config.endpoint)
        print(config.allowed_ips)
        print(config.interface_address)
        print(config.interface_privateKey)
        print(config.interface_dns)
        print(config.server_public_key)
        return config
    except Exception as e:
        print("An error occurred:", str(e))
        return None

if __name__ == '__main__':
    run_add_peer_script()
