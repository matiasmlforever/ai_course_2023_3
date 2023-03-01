import datetime


class Ambiente:
    def __init__(self, **kwargs):
        self.size = kwargs['size']
        self.timestamp = kwargs['timestamp']
        self.agentes = kwargs['agentes']

    def __str__(self):
        return f'size = {self.size}, ' \
               f'timestamp = {self.timestamp}, ' \
               f'agentes = {self.agentes}'
