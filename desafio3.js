class Classe_Heroi{
    constructor(nome, idade, tipo){
        this.nome = nome;
        this.idade = idade;
        this.tipo = tipo;
    }
    atacar(){
        if (this.tipo === "Mago") {
            const ataque = "Magia";
            console.log(`O ${this.tipo} atacou usando ${ataque}`);

        } else if (this.tipo === "Guerreiro") {
            const ataque = "Espada";
            console.log(`O ${this.tipo} atacou usando ${ataque}`);

        } else if (this.tipo === "Monge") {
            const ataque = "Artes Marciais";
            console.log(`O ${this.tipo} atacou usando ${ataque}`);
            
        } else if (this.tipo === "Ninja") {
            const ataque = "Shuriken";
            console.log(`O ${this.tipo} atacou usando ${ataque}`);

        } 
        }
    }

const heroi1 = new Classe_Heroi("Merlin", 150, "Mago");
heroi1.atacar();

const heroi2 = new Classe_Heroi("Elend", 25, "Guerreiro");
heroi2.atacar();

const heroi3 = new Classe_Heroi("Sazed", 34, "Monge");
heroi3.atacar();

const heroi4 = new Classe_Heroi("Sasuke", 23, "Ninja");
heroi4.atacar();
