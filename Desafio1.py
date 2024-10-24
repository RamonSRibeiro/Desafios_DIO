heroi = input("Digite o Nome do Heroi: ")
exp = int(input("Digite a quantidade de Experiência do Heroi: "))

if exp < 1000:
    nivel = "Ferro"
    
elif 1001 <= exp <= 2000:
    nivel = "Bronze"
    
elif 2001 <= exp <= 5000:
    nivel = "Prata"
    
elif 5001 <= exp <= 7000:
    nivel = "Ouro"
    
elif 7001 <= exp <= 8000:
    nivel = "Platina"
    
elif 8001 <= exp <= 9000:
    nivel = "Ascendente"
    
elif 9001 <= exp <= 10000:
    nivel = "Imortal"
    
else:
    nivel = "Radiante"

print(f"O Herói de nome {heroi} está no nível de {nivel}")