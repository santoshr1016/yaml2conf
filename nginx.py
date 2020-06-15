import pickle

mapping_dict = {
}

class NginxConfiguration(object):
    def __init__(self):
        print("I am Nginx Configuration Builder Program")

    def build(self):
        self.generic_globals = GenericGlobalContext()
        self.generic_globals.set_generic_global_context()
        self.http = HttpContext()
        self.http.set_http_context()
        self.events = EventsContext()
        self.events.set_events_context()


class GenericGlobalContext(object):
    def __init__(self):
        print("Constructor for GenericGlobalContext "
              "My job is to set set generic global variables")

    def set_generic_global_context(self):
        print("Initialize all the Global variables of the configuration")


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
        pickle_in = open("dict.pickle", "rb")
        yaml_dict = pickle.load(pickle_in)
        return yaml_dict

    def get_number_of_reverse_proxies(self):
        for key in self.main_yaml.keys():
            if 'app' in key:
                return self.main_yaml.get('app').keys(), self.main_yaml.get('app')

    def get_app_directive_parsed(self):
        for reverse_proxy in self.reverse_proxies:
            print(self.app_dict.get(reverse_proxy).keys())


class EventsContext(object):
    def __init__(self):
        print("Constructor for EventsContext "
              "My job is to set events context")

    def set_events_context(self):
        print("Set the events context ")


class User(object):
    def __init__(self):
        print("Constructor for User")
        print("Please write nginx configuration for client: User!! ")

    def nginx_configuration_builder(self):
        print("User:: Let's Contact nginx configuration builder\n")
        ngb = NginxConfiguration()
        ngb.build()

    def __del__(self):
        print("User:: Thanks to Nginx Configuration Builder, all preparations done! Phew!")


santosh = User()
santosh.nginx_configuration_builder()
