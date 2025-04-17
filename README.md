## 🎯 Detección de Objetos en Tiempo Real

Este programa realiza **detección de objetos en tiempo real** utilizando el modelo **EfficientDet Lite0** de MediaPipe. Captura video desde la cámara, procesa cada frame y muestra los resultados en una ventana con cuadros delimitadores y etiquetas que indican el nombre del objeto detectado y su nivel de confianza.

---

## ⚙️ Características principales

### 📦 Modelo utilizado:
- **EfficientDet Lite0**: Un modelo ligero y eficiente para la detección de objetos.
- Detecta objetos comunes como personas, portátiles, sillas, tazas, entre otros.

### 🛠️ Configuración personalizada:
- Solo detecta las categorías especificadas en:
  \`\`\`
  category_allowlist = ["person", "laptop", "chair"]
  \`\`\`
- Filtra detecciones con una confianza mínima de **50%** (\`score_threshold=0.5\`).

---

## 🔄 Flujo del programa

1. Captura video en tiempo real desde la cámara.
2. Convierte cada frame al formato requerido por MediaPipe.
3. Realiza la detección de objetos de forma asíncrona.
4. Dibuja cuadros delimitadores y etiquetas.
5. Muestra el resultado en una ventana.
6. Puedes salir presionando la tecla **ESC**.

---

## 📦 Dependencias

- \`OpenCV\`: Para captura y visualización de video.
- \`MediaPipe\`: Para la detección de objetos con EfficientDet.
- Modelo **EfficientDet Lite0** en formato \`.tflite\`.
- Python >= **3.9**

---

## ⚠️ Limitación del rendimiento

> ⚠️ El programa está limitado a detectar solo **3 objetos** debido a limitaciones de procesamiento.  
Detectar más objetos puede causar sobrecarga o cuellos de botella, dependiendo de tu equipo.

---

## 📝 Lista de objetos disponibles para detectar

<details>
<summary><strong>Haz clic para expandir</strong></summary>

### 👤 Personas y animales:
- person, dog, cat, bird, horse, sheep, cow, elephant, bear, zebra, giraffe

### 🚗 Vehículos:
- bicycle, car, motorcycle, airplane, bus, train, truck, boat

### 🪑 Objetos de uso diario:
- chair, couch, potted plant, bed, dining table, toilet, tv, laptop, mouse, remote, keyboard, cell phone, microwave, oven, toaster, sink, refrigerator

### 🍽️ Comida y utensilios:
- knife, fork, spoon, bowl, banana, apple, sandwich, orange, broccoli, carrot, hot dog, pizza, donut, cake

</details>

---

## ✏️ Personalización

Para cambiar los objetos que deseas detectar, edita esta línea:

\`\`\`
category_allowlist = ["person", "laptop", "chair"]
\`\`\`

Para detectar **todos los objetos posibles**, elimina esa línea.  
Sin embargo, esto **no es recomendable** si tu equipo tiene recursos limitados, ya que puede afectar el rendimiento significativamente.

---

## 🧠 Recomendación

Optimiza la selección de objetos según tu caso de uso y las capacidades de tu equipo. Reducir la cantidad de categorías mejora el rendimiento y la precisión en tiempo real.


