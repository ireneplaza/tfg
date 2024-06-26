# Análisis de los benchmarks para la evaluación de LLM en español.
## TFG del GRADO EN INGENIERÍA DE TECNOLOGÍAS Y SERVICIOS DE TELECOMUNICACIÓN de la ETSIT, UPM.
### Realizado por Irene Plaza Ortiz en 2023-2024.

Este repositorio incluye todo el código empleado durante el Trabajo de Fin de Grado "Análisis de los benchmarks para la evaluación de LLM en español". El propósito general de este TFG es estudiar las implicaciones que se derivan de emplear benchmarks diseñados en inglés y traducidos, mediante herramientas de traducción automática, al español en la evaluación de las capacidades de los Large Language Models (LLMs). De este modo, el trabajo busca poner de manifiesto la importancia real de evaluar de manera precisa y específica las habilidades de los LLMs, para seguir promoviendo su desarrollo. 

Para conseguir ese objetivo, ha diseñado un método de evaluación de modelos LLM que permita extraer información acerca de su comportamiento al enfrentarse a distintos benchmarks seleccionados. Dicho método emplea los archivos incluidos en este repositorio.

El archivo principal "test_MMLU.py" envía a la API de ChatGPT los tests que se han seleccionado, obteniendo y guardando las respuestas del modelo que se haya solicitado, así como la probabilidad de respuesta y los top_tokens de mayor probabilidad. Después, el fichero que almacena las respuestas se analiza con otros archivos como "analisis.py" o "normal_func.py".

El siguiente paso implica obtener las traducciones con los servicios automáticos de ChatGPT y Microsoft (Azure Translator), para lo que se ejecutan "traductor_azure.py" y "traductor_chatgpt.py". Una vez obtenidas, se repite el proceso anterior, ejecutando los mismos ficheros.

Finalmente, el resto de archivos python constituyen un conjunto de herramientas que facilitan el análisis general y la comparación de las tres versiones de cada test que se somete a estudio: la versión en inglés original, y las versiones en español obtenidas con los traductores. De este modo, se estudia si las versiones traducidas cometen errores debido a fallos de traducción o por factores culturales. El trabajo se completa con un posterior análisis manual de los resultados.
