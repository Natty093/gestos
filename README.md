# 🎭 GestureMeme Trigger: Detector de Expresiones Faciales con IA

> Un proyecto de Visión Artificial que reacciona a tus gestos en tiempo real superponiendo memes.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=flat&logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Face%20Mesh-orange?style=flat)

## 📖 Descripción
Este proyecto utiliza técnicas de **Visión por Computadora** para detectar puntos de referencia faciales (facial landmarks) en tiempo real mediante la webcam.

El sistema analiza la geometría del rostro para identificar gestos específicos (como sonreír o sacar la lengua) y dispara una respuesta visual inmediata, reemplazando la imagen de la cámara o superponiendo un meme correspondiente al gesto detectado.

## ⚙️ Cómo funciona (Lógica Técnica)
El núcleo del proyecto se basa en **MediaPipe Face Mesh**, que mapea 468 puntos 3D en el rostro.
1.  **Extracción de Puntos Clave:** Se monitorean coordenadas específicas de los labios (puntos `61`, `291`, `13`, `14`).
2.  **Cálculo Geométrico:** Se calcula la **Distancia Euclidiana** entre estos puntos para determinar:
    * **Ancho de la boca:** Para detectar sonrisas.
    * **Apertura vertical:** Para detectar si la boca está abierta o sacando la lengua.
3.  **Umbrales Dinámicos:** Si las distancias superan ciertos valores predefinidos (calibrables), se activa el "Trigger" del meme.

## 🛠️ Tecnologías Utilizadas
* **Python 3:** Lenguaje principal.
* **OpenCV (`cv2`):** Para la captura de video y procesamiento de imágenes.
* **MediaPipe:** Para la inferencia del modelo de malla facial (Face Mesh).
* **NumPy:** Para operaciones matemáticas eficientes.

## 🚀 Instalación y Uso

### 1. Clonar el repositorio
```bash
git clone [https://github.com/Natty093/gestos.git]
cd ia-reconocimiento-gestos