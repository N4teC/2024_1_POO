class Disciplina:
    def __init__(self, nome, semestre, media, ch, aprovado):
        self.set_nome(nome)
        self.set_semestre(semestre)
        self.set_media(media)
        self.set_ch(ch)
        self.set_aprovado(aprovado)
    def set_nome(self, nome):
        if nome == str: self.__nome = nome
        else: raise ValueError()
    def set_semestre(self, semestre):
        if semestre == str: self.__semestre = semestre
        else: raise ValueError()
    def set_media(self, media):
        if media >= 0 and media <= 100: self.__media = media
        else: raise ValueError()
    def set_ch(self, ch):
        if ch > 0: self.__ch = ch
        else: raise ValueError()
    def set_aprovado(self, aprovado):
        if aprovado == bool: self.__aprovado = aprovado
        else: raise ValueError()
    def get_nome(self):
        return self.__nome
    def get_semestre(self):
        return self.__semestre
    def get_media(self):
        return self.__media
    def get_ch(self):
        return self.__ch
    def get_aprovado(self):
        return self.__aprovado
    def __str__(self):
        return f"nome: {self.get_nome()} - semestre: {self.get_semestre()} - carga horaria: {self.get_ch()} - media: {self.get_media()} - aprovado: {self.get_aprovado()}"
    
class Historico:
    def __init__(self, aluno):
        self.set_aluno(aluno)
        self.__disciplinas = []
    def set_aluno(self, aluno):
        if aluno == str: self.__aluno = aluno
        else: raise ValueError()
    def get_aluno(self):
        return self.__aluno
    def inserir_disciplina(self, nome, semestre, media, ch, aprovado):
        d = Disciplina(nome, semestre, media, ch, aprovado)
        self.__disciplinas.append(d)
    def get_disciplinas(self):
        return self.__disciplinas
    def listar_disciplinas(self):
        for i in range(len(self.get_disciplinas())):
            print(self.get_disciplinas[i])
    def listar_semestre(self, semestre):
        for i in range(len(self.get_disciplinas())):
            if self.get_disciplinas()[i].get_semestre() == semestre: print(self.get_disciplinas()[i])
    def maior_media(self):
        maior = 0
        for i in range(len(self.get_disciplinas())):
            for j in range(1,len(self.get_disciplinas())):
                if self.get_disciplinas()[i].get_media() >= self.get_disciplinas()[j].get_media(): maior = self.get_disciplinas()[i].get_media()
        
        for i in range(len(self.get_disciplinas())):
            if self.get_disciplinas()[i].get_media() == maior: print(self.get_disciplinas()[i])
    def IRA(self):
        qtd = 0
        notas = 0
        for i in range(len(self.get_disciplinas())):
            if self.get_disciplinas()[i].get_aprovado():
                notas = notas + self.get_disciplinas()[i].get_media()
                qtd+1
        
        return notas/qtd
    def total_ch(self):
        total = 0
        for i in range(len(self.get_disciplinas())):
            if self.get_disciplinas()[i].get_aprovado():
                total = total + self.get_disciplinas()[i].get_ch()
        
        return total
    def __str__(self):
        return f"nome = {self.get_aluno()} - disciplinas = {len(self.get_disciplinas())}"
    