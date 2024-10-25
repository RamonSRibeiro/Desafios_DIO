class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "Mago":
            ataque = "Magia"
            
        elif self.tipo == "Guerreiro":
            ataque = "Espada"
            
        elif self.tipo == "Monge":
            ataque = "Artes Marciais"
            
        elif self.tipo == "Ninja":
            ataque = "Shuriken"
        
        return f"{self.nome} O {self.tipo} atacou usando {ataque}."

def coletar_dados():
    while True:
        nome = input("Digite o nome do herói: ")
        idade = input("Digite a idade do herói: ")
        tipo = input("Digite o tipo do herói (Mago, Guerreiro, Monge, Ninja): ")
        
        heroi = Heroi(nome, idade, tipo)
        print(heroi.atacar())

coletar_dados()
