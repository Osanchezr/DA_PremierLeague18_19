# Premier League 2018-2019 Database Analysis
![premiere-league-premiere-league-logo](https://github.com/user-attachments/assets/4fd16f51-11d8-4b1e-a685-e63ac07af7ac)
## Descripción del Proyecto

Este proyecto forma parte del bootcamp de análisis de datos de Ironhack, y se centra en la construcción y análisis de una base de datos usando **MySQL**. El objetivo principal ha sido limpiar y organizar un conjunto de datos en **Python**, para luego estructurarlo en una base de datos relacional que permita realizar análisis avanzados a través de consultas SQL.

La base de datos utilizada en este proyecto está basada en datos reales de la temporada 2018-2019 de la **Premier League inglesa** e incluye tablas relacionadas con jugadores, equipos, partidos, estadios, árbitros y calendario de partidos. Los datos fueron obtenidos de [Footystats](https://footystats.org/download-stats-csv), y posteriormente procesados para su uso en este análisis.

## Objetivos del Proyecto

### 1. Limpieza de Datos en Python
   - Se realizó una exhaustiva limpieza y preparación de los datos para garantizar su calidad y coherencia. Esto incluyó el manejo de columnas, datos duplicados, creacion de codigos únicos.
   
### 2. Modelado de Base de Datos Relacional
   - Una vez los datos estuvieron listos, se exportaron a **MySQL**, donde se creó un **Modelo Entidad-Relación (ER)** que representó las relaciones entre equipos, jugadores, partidos, estadios y calendario.
![model](https://github.com/Osanchezr/DA_PremierLeague18_19/blob/554ddfa3d30ade24ecaf9d1e5375e1546ff0a047/images/model.JPG)
   
### 3. Análisis SQL Avanzado
   - Se realizaron diversas consultas SQL para analizar diferentes aspectos de la temporada, relacion de puntaje y goles por equipo, los jugadores con más goles y la influencia de los estadios en el rendimiento de los equipos,etc.
   
### 4. Visualización de Datos en Python
   - Finalmente, los resultados de las consultas SQL se exportaron a Python, donde se crearon gráficos visuales utilizando **matplotlib** y **seaborn**. Estos gráficos ayudaron a visualizar patrones y tendencias clave de la temporada.
![g1](https://github.com/Osanchezr/DA_PremierLeague18_19/blob/554ddfa3d30ade24ecaf9d1e5375e1546ff0a047/images/grafico1.JPG)
![g2](https://github.com/Osanchezr/DA_PremierLeague18_19/blob/554ddfa3d30ade24ecaf9d1e5375e1546ff0a047/images/grafico2.JPG)
![g3](https://github.com/Osanchezr/DA_PremierLeague18_19/blob/554ddfa3d30ade24ecaf9d1e5375e1546ff0a047/images/grafico3.JPG)
![g4](https://github.com/Osanchezr/DA_PremierLeague18_19/blob/554ddfa3d30ade24ecaf9d1e5375e1546ff0a047/images/grafico4.JPG)

## Herramientas Utilizadas

- **Python**: Para la limpieza y preprocesamiento de datos.
- **MySQL**: Para la creación y gestión de la base de datos.
- **SQL**: Para consultas y análisis de los datos.
- **Matplotlib y Seaborn**: Para la creación de visualizaciones y gráficos.
- **GitHub**: Para compartir código y colaborar con el equipo.

## Entregables

1. **Data Cleaning Notebook (Python)**: Limpieza y preprocesamiento de los datos.
2. **MySQL Database**: Base de datos con el modelo ER estructurado y relaciones definidas.
3. **Consultas SQL**: Series de queries realizadas para análisis de los datos.
4. **Python Visualizations**: Gráficos que muestran resultados clave.

## Desafíos Encontrados

- **Integración de Datos**: La estructuración de los datos en un modelo relacional representó un desafío debido a la complejidad de las relaciones entre las distintas entidades, como jugadores, partidos y equipos.
  
- **Optimización de Consultas**: Algunas consultas SQL requerían ser optimizadas para obtener resultados de forma eficiente en bases de datos grandes.

## Ejemplos de Consultas SQL Realizadas

- Jugadores con más goles durante la temporada.
- Relación entre la capacidad del estadio y victorias locales.
- ¿Tener mayor posesión asegura más victorias?

## Participantes

- **[Oscar Sanchez](https://github.com/Osanchezr)**
- **[Beatriz Tranche](https://github.com/beatranche)**

## Presentación

- **[Link](https://prezi.com/p/edit/hmmazzaliqrl/?lid=x1kxl8roj2s0&utm_source=braze&utm_medium=email&utm_content=Tokenization+Variant&utm_campaign=Next_Share_A_Prezi_v2&UID=338042680)**

Este proyecto refleja el trabajo colaborativo y el aprendizaje adquirido durante la cuarta semana del bootcamp, aplicando conocimientos de **Python**, **MYSQL** y **visualización de datos** en un contexto del mundo real.

