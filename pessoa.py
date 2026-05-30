class Pessoa:
    def __init__(self, nome, idade, telefone, endereco, hobby):
        self.__nome = nome # private
        self.__idade = idade # private 
        self.__telefone = telefone # private
        self.__hobbies = [hobby] # private
        self.__endereco = endereco # private

    # métodos de acesso (getters e setters)
    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome
    
    def get_idade(self):
        return self.__idade
    
    def set_idade(self, idade):
        self.__idade = idade
    
    def get_telefone(self):
        return self.__telefone
    
    def set_telefone(self, telefone):
        self.__telefone = telefone
    
    def get_hobbies(self):
        return self.__hobbies
    
    def set_hobbies(self, hobbies):
        self.__hobbies = hobbies

    def get_endereco(self):
        return self.__endereco
    
    def set_endereco(self, endereco):
        self.__endereco = endereco