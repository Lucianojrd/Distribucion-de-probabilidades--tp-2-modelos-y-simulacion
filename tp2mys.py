import matplotlib.pyplot as plt
import numpy as np 
from scipy import stats 
from scipy.stats import poisson, binom, nbinom, norm, expon, gamma, weibull_min, lognorm
import seaborn as sns


def met_distribuciones():
    lista = []
    familia_de_distribuciones = ['triangular']
    i = 0
    datos_str = input(f"Ingrese datos de la muestra separados por coma : ")
    datos = [float(x.strip()) for x in datos_str.split(",")]
    lista.append(datos)

    media = np.mean(lista[0])
    varianza = np.var(lista[0])
    desviacion = np.std(lista[0])
    mediana = np.median(lista[0])

    coeficiente_de_simetria = stats.skew(lista[0])
    t = varianza/media 
    coeficiente_de_variacion = desviacion/media

    opcion = int(input('Presione 1 o 2 dependiendo las siguientes opciones: 1-Distribucion discreta  --  2-Distribucion continua '))
    if opcion == 1:
        # Distribuciones discretas
        if t == 1:
            familia_de_distribuciones.append('Poisson')
            distribucion_discreta = poisson
            params = distribucion_discreta.fit(lista[0])
            x_discreto = np.arange(min(lista[0]), max(lista[0]) + 1)
            y_discreto = distribucion_discreta.pmf(x_discreto, *params)
        elif t < 1:
            familia_de_distribuciones.append('Binomial')
            distribucion_discreta = binom
            params = distribucion_discreta.fit(lista[0])
            x_discreto = np.arange(min(lista[0]), max(lista[0]) + 1)
            y_discreto = distribucion_discreta.pmf(x_discreto, *params)
        elif t > 1:
            familia_de_distribuciones.append('Binomial negativa')
            distribucion_discreta = nbinom
            params = (coeficiente_de_variacion**2, 1/(t-1))
            x_discreto = np.arange(min(lista[0]), max(lista[0]) + 1)
            y_discreto = distribucion_discreta.pmf(x_discreto, *params)
        
        # Graficar histograma para distribuciones discretas
        plt.hist(lista[0], bins=10, color='blue', edgecolor='black', density=True, alpha=0.5, label='Datos')
        plt.plot(x_discreto, y_discreto, 'r--', linewidth=2, label='Distribución Discreta Teórica')
        plt.xlabel('Valores en x')
        plt.ylabel('Densidad de probabilidad')
        plt.title('Histograma y Distribución Discreta Teórica')
        plt.legend()
        plt.grid(True)
        plt.show()
        
    elif opcion == 2:
        # Distribuciones continuas
        if media == mediana:
            familia_de_distribuciones.append('Normal')
            distribucion_continua = norm
        elif coeficiente_de_variacion == 1:
            familia_de_distribuciones.append('Exponencial')
            distribucion_continua = expon
        elif coeficiente_de_variacion < 1:
            familia_de_distribuciones.append('Gamma o Weibull')
            distribucion_continua = gamma
        elif coeficiente_de_variacion > 1:
            familia_de_distribuciones.append('Lognormal')
            distribucion_continua = lognorm
    
        # Ajustar parámetros para distribuciones continuas
        params_continua = distribucion_continua.fit(lista[0])
        x_continuo = np.linspace(min(lista[0]), max(lista[0]), 1000)
        y_continuo = distribucion_continua.pdf(x_continuo, *params_continua)
        
        # Calcular límites del eje x para el histograma
        x_min_hist = min(lista[0]) - 5  # Restar un valor pequeño para ajustar el límite mínimo
        x_max_hist = max(lista[0]) + 5  # Sumar un valor pequeño para ajustar el límite máximo
        
        # Graficar histograma para distribuciones continuas con límites ajustados
        plt.hist(lista[0], bins='auto', range=(x_min_hist, x_max_hist), color='blue', edgecolor='black', density=True, alpha=0.7)
        plt.xlabel('Valores en x')
        plt.ylabel('Densidad de probabilidad')
        plt.title('Histograma y Distribución Continua Teórica')
        plt.legend()
        plt.grid(True)
        plt.show()

    else:
        print("No existe esa opcion")
        return

    return familia_de_distribuciones

resultado = met_distribuciones() 
print(resultado)
