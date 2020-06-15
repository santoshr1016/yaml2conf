from libs.yaml_dict_converter import SaveYaml


class HttpContext(object):
    def __init__(self):
        print("Constructor for HttpContext "
              "My job is to set http context")
        self.main_yaml = self.load_yaml()
        self.reverse_proxies, self.app_dict = self.get_number_of_reverse_proxies()
        self.http_context = list()
        self.get_app_directive_parsed()

    def set_http_context(self):
        print("Stage 1 - Set the global variables of http context ")
        print("Stage 2 - Set the server context ")
        print("Stage 3 - Set reverse proxy upstream context ")
        print("Stage 3 - Set upstream server context")

    def load_yaml(self):
        yaml= SaveYaml()
        yaml_dict = yaml.load_yaml()
        return yaml_dict

    def get_number_of_reverse_proxies(self):
        for key in self.main_yaml.keys():
            if 'app' in key:
                return self.main_yaml.get('app').keys(), self.main_yaml.get('app')

    def get_app_directive_parsed(self):
        upstream_dict = dict()
        for reverse_proxy in self.reverse_proxies:
            upstream_list = "upstream " + reverse_proxy
            self.http_context.append(upstream_list)
            fqdn_list = []
            for key, val in self.app_dict.get(reverse_proxy).items():
                # print(key, val)
                if key == 'fqdn':
                    if isinstance(val, list):
                        for ser in val:
                            ss = "server_name " + ser + " ;"
                            fqdn_list.append(ss)
            self.http_context.append(fqdn_list)
        print(self.http_context)
