from libs.generic_global_context import GenericGlobalContext
from libs.http_context import HttpContext
from libs.events_context import EventsContext


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