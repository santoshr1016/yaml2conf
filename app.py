from libs.nginx_configuration import NginxConfiguration
from libs.yaml_dict_converter import SaveYaml


class App(object):
    def __init__(self):
        print("Constructor for User")
        print("Please write nginx configuration for client: User!! ")

    def nginx_configuration_builder(self):
        print("User:: Let's Contact nginx configuration builder\n")
        ngb = NginxConfiguration()
        ngb.build()

    def __del__(self):
        print("User:: Thanks to Nginx Configuration Builder, all preparations done! Phew!")


yaml = SaveYaml()
yaml.save_items()
app = App()
app.nginx_configuration_builder()
