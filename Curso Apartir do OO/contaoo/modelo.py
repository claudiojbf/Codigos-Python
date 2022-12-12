class Progama:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0

    def dar_like(self):
        self._like += 1

    @property
    def like(self):
        return self._like
        
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._like} likes'

class Filme(Progama):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._like} likes'
       

class Serie(Progama):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._like} likes'

class Playlist:
    def __init__(self, nome, progamas):
        self.nome = nome
        self._progamas = progamas

    def __getitem__(self, item):
        return self._progamas[item]

    @property
    def listagem(self):
        return self._progamas

    
    def __len__(self):
        return len(self._progamas)
        
vingadores = Filme("vingadores - gerra infinita", 2018, 160)
atlanta = Serie("atlanta", 2018, 2)
tmep = Filme('Todo Mundo Em Panico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)


vingadores.dar_like()
vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()


atlanta.dar_like()
atlanta.dar_like()
demolidor.dar_like()
demolidor.dar_like()


filmes_e_serie = [vingadores, atlanta, demolidor, tmep]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_serie)

print(f'Tamanho da Playlist:{len(playlist_fim_de_semana)}')

print(vingadores in playlist_fim_de_semana)

for progama in playlist_fim_de_semana.listagem:
    print(progama)


