class NginxConfiguration(object):
    def __init__(self):
        print("I am Nginx Configuration Creator File")

    def build(self):
        self.generic_globals = GenericGlobalContext()
        self.generic_globals.set_generic_global_context()
        self.http = HttpContext()
        self.http.set_http_context()
        self.events = EventsContext()
        self.events.set_events_context()


class GenericGlobalContext(object):
    def __init__(self):
        print("My job is to set set generic global variables")

    def set_generic_global_context(self):
        print("Initialize all the Global variables of the configuration")


class HttpContext(object):
    def __init__(self):
        print("My job is to set http context")

    def set_http_context(self):
        print("Stage 1 - Set the global variables of http context ")
        print("Stage 2 - Set the server context ")
        print("Stage 3 - Set upstream context ")
        print("Stage 3 - Set upstream server context")


class EventsContext(object):
    def __init__(self):
        print("My job is to set ")

    def set_events_context(self):
        print("Set the events context ")


class User(object):
    def __init__(self):
        print("You:: Whoa! Nginx Configuration Builder !!!")

    def nginx_configuration_builder(self):
        print("User:: Let's Contact nginx configuration builder\n\n")
        ngb = NginxConfiguration()
        ngb.build()

    def __del__(self):
        print("User:: Thanks to Nginx Configuration Builder, all preparations done! Phew!")


santosh = User()
santosh.nginx_configuration_builder()

