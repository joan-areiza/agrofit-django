# core/utils/medidas.py 
def calcular_imc(peso, altura):
    if not peso or not altura or float(altura) <= 0:
        return None
    return round(float(peso) / (float(altura) ** 2), 2)