import random

paises = {
    "Brasil": "É o maior país da América do Sul.",
    "Estados Unidos": "Possui a Estátua da Liberdade e a Casa Branca.",
    "Canadá": "É conhecido pelas suas paisagens frias e montanhosas.",
    "França": "É famosa pela Torre Eiffel e pela culinária refinada.",
    "Alemanha": "É conhecida por sua engenharia e cervejas.",
    "Japão": "É um país tecnologicamente avançado com uma rica cultura.",
    "Austrália": "Tem cangurus e coalas como animais icônicos.",
    "China": "Possui a Grande Muralha e uma rica história.",
    "Índia": "É conhecida por suas cores vibrantes e cultura diversificada.",
    "Rússia": "É o maior país do mundo em extensão territorial."
}

vidas_iniciais = 3

def escolher_pais_aleatorio():
    return random.choice(list(paises.keys()))

def main():
    vidas = vidas_iniciais
    
    print("Bem-vindo ao Jogo de Adivinhação de Países!")
    print("Você tem", vidas, "vidas.")
    
    while vidas > 0:
        pais_alvo = escolher_pais_aleatorio()
        dica = paises[pais_alvo]
        
        print("\nDica:", dica)
        palpite = input("Digite o nome do país: ")
        
        if palpite.capitalize() == pais_alvo:
            print("Parabéns! Você acertou:", pais_alvo)
        else:
            vidas -= 1
            if vidas == 0:
                print("Você perdeu todas as vidas. Fim de jogo!")
            else:
                print("Errado! Você perdeu uma vida. Vidas restantes:", vidas)
                print("A resposta correta era:", pais_alvo)
    
if __name__ == "__main__":
    main()
