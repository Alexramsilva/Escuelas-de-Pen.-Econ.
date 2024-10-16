# -*- coding: utf-8 -*-
"""streamlit_app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a7ZReKK7Pvmit7thnomKCgwbeFw3aS8Y
"""

import streamlit as st

# Título de la aplicación
st.title("Escuelas de Pensamiento Económico")

st.image("URC.png", caption="UST-URC Universidad Rosario Castellanos", width=300)

# Menú desplegable con opciones de escuelas de pensamiento económico
escuelas = [
    "Clásica (1776 - 1870)",
    "Keynesiana (1930s - Presente)",
    "Neoclásica (1870 - Presente)",
    "Marxista (1850s - Presente)",
    "Austriaca (1870s - Presente)",
    "Monetarista (1950s - Presente)",
    "Escuela de Chicago (1950s - Presente)",
    "Institucionalismo (1890s - Presente)",
    "Economía de la Información (1970s - Presente)"
]

# Selección de la escuela de pensamiento económico
escuela_seleccionada = st.selectbox("Selecciona una escuela de pensamiento económico:", escuelas)

# Descripciones de las escuelas de pensamiento económico
descripciones = {
    "Clásica (1776 - 1870)": """
        La escuela clásica, encabezada por economistas como Adam Smith y David Ricardo,
        sostiene que los mercados son autorreguladores y que la intervención del gobierno debe ser mínima.
        Surgió en el siglo XVIII con la publicación de *La riqueza de las naciones* (1776)
        de Adam Smith [DIvisión del  trabajo, Egoismo de los empresarios, Mano invisible, seguridad al empresario],
        y dominó hasta finales del siglo XIX.
    """,
    "Keynesiana (1930s - Presente)": """
        Fundada por John Maynard Keynes en respuesta a la Gran Depresión de los años 1930,
        esta escuela defiende que el gobierno debe intervenir para estabilizar la economía mediante
        políticas fiscales y monetarias, especialmente en tiempos de recesión. Su obra más influyente es
        *La Teoría General del Empleo, el Interés y el Dinero* (1936).
    """,
    "Neoclásica (1870 - Presente)": """
        La escuela neoclásica surgió en la década de 1870, enfocándose en el análisis marginal
        y la idea de que los individuos son racionales y maximizan su utilidad. La oferta y la demanda
        determinan el equilibrio en los mercados. Esta escuela sigue influyendo fuertemente en la teoría económica moderna.
    """,
    "Marxista (1850s - Presente)": """
        Basada en las teorías de Karl Marx, esta escuela critica el capitalismo y aboga por la lucha de clases
        como motor del cambio social y económico. Propone una transición hacia una sociedad sin clases.
        La obra clave es *El Capital* (1867) [Mercancia: Valor de Cambio y Valor de Uso, Trabajo socialmente necesario,
        Valor de la mercancia= c+v+p,Tasa de plusvalor=p/v, M-M, M-D-M vs D-M-D',D-D'].
        Durante una parte del proceso laboral el obrero se limita a producir el valor de su fuerza de trabajo (medios de subsistencia).
        El proceso de consumo de la fuerza de trabajo se efectua fuera de la esfera de circulación.
        La mercancia como medida de valor y tambien de circulación es el dinero.
        Aunque nació en el siglo XIX, sigue vigente en debates contemporáneos.
    """,
    "Austriaca (1870s - Presente)": """
        Esta escuela se originó en Austria a fines del siglo XIX con Carl Menger y se centra en la importancia del
        individualismo, el mercado libre y la función empresarial. Economistas como Friedrich Hayek y Ludwig von Mises
        son sus principales exponentes. Ha influido en el pensamiento económico liberal.
    """,
    "Monetarista (1950s - Presente)": """
        Liderada por Milton Friedman a partir de la década de 1950, esta escuela sostiene que la política monetaria
        es la principal herramienta para controlar la inflación y que la oferta de dinero debe ser gestionada cuidadosamente.
        El monetarismo fue influyente en las políticas económicas de los años 1970 y 1980.
    """,
    "Escuela de Chicago (1950s - Presente)": """
        Asociada a Milton Friedman y otros economistas de la Universidad de Chicago a partir de los años 1950,
        defiende los mercados libres, la mínima intervención del gobierno y el control de la inflación a través
        de políticas monetarias. Es una de las principales corrientes del pensamiento económico contemporáneo.
    """,
    "Institucionalismo (1890s - Presente)": """
        La escuela institucionalista, fundada por economistas como Thorstein Veblen y John R. Commons,
        sostiene que las instituciones sociales, políticas y económicas son cruciales para entender el comportamiento económico.
        Critica el individualismo de las teorías neoclásicas y pone énfasis en la evolución de las normas y reglas que guían las economías.
        Surgió a finales del siglo XIX y sigue siendo influyente en campos como la economía del desarrollo y la economía política.
    """,
    "Economía de la Información (1970s - Presente)": """
        La economía de la información, desarrollada principalmente a partir de los trabajos de Joseph Stiglitz, George Akerlof
        y Michael Spence, estudia cómo la información imperfecta afecta el comportamiento de los mercados. Surgió en la década de 1970
        y explica fenómenos como la selección adversa y el riesgo moral. Es clave para entender problemas como los mercados de seguros
        y el desempleo.
    """
}

# Mostrar la descripción de la escuela seleccionada
st.write(f"### {escuela_seleccionada}")
st.write(descripciones[escuela_seleccionada])