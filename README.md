# Cloud Computing - Clase 5
## Aprendizaje Federado
Equipo: Comando Estelar

### Descripción
Este proyecto implementa Aprendizaje Federado utilizando cuatro métodos de agregación diferentes: FedAvg, FedBN, FedMedian y FedProx.

### Instrucciones
Antes de comenzar, es necesario dividir el set de datos en folds estratificados para entrenar los modelos locales con cada fold creado.

1. Fork it
2. Corre el archivo *local_training.ipynb* para cada fold de datos creado. (Asegúrate de descargar el archivo *TheModel.py* para poder generar las arquitecturas y córrelos de manera local pero en equipos separados.)
3. El archivo *local_training.ipynb* genera los archivos .keras necesarios para correr *global_model.ipynb*.
4. Corre el archivo *global_model.ipynb*

Nota: En la carpeta *local_implementations* se encuentran los archivos .keras requeridos para la implementación del modelo global. Se realizaron 2 pruebas: una entrenando localmente con 5 épocas y otra con 20 épocas. La diferencia se nota en el nombre de los archivos.
