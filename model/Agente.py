class Agente:
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']

    def __str__(self): # TODO: not working!
        print(f'id = {self.id}, name = {self.name}')

