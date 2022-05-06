import string


class Usuario:
    def __init__(self,nome,dat_nasc,cpf,endereco,login,senha):
        self.nome = nome
        self.dat_nasc = dat_nasc
        self.cpf = cpf
        self.endereco = endereco
        self.login = login
        self.senha = senha

