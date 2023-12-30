
from socket import *
import os


class IpConfig:

    def __init__(self):

        self.hostname = self.get_hostname()

    def get_dynamic_port(self):
        # Create a socket

        s = socket(AF_INET, SOCK_STREAM)
        s.bind((self.hostname, 0))
        _, port = s.getsockname()
        s.close()
        return port




    def get_hostname(self):

            hostname = gethostname()
            host = gethostbyname(hostname)

            return host

# Example usage
ip_config = IpConfig()
print(ip_config.get_dynamic_port())