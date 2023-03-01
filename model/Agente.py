class Agente:
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']

    def __str__(self):
        return f'id = {self.id}, ' \
               f'name = {self.name}, '
