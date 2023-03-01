import datetime


class Ambiente:
    def __init__(self, size: int, timestamp: type(datetime.datetime), agentes: list):
        self.size = size
        self.timestamp = timestamp
        self.agentes = agentes

