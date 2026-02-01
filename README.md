
<<<<<<< HEAD
# Smart Irrigation System for Avocados in Mexico

Decision-support system for irrigation scheduling using
remote sensing, meteorological data, and ML models.

## Structure
- data/raw: external datasets (SMAP, Open-Meteo, SPEI)
- data/processed: cleaned & merged data
- src/: core pipeline (features, model, decision logic)
- notebooks/: demo and exploration

## Setup
pip install -r requirements.txt
EOF
=======

# 🌱 Sistema Inteligente de Recomendación para Cultivo de Aguacate

Este proyecto tiene como objetivo **optimizar el riego y el manejo del cultivo de aguacate** mediante recomendaciones inteligentes basadas en **datos obtenidos de APIs climáticas y agrícolas**, ayudando a productores a tomar mejores decisiones y reducir el desperdicio de agua y recursos.

---

## 📌 Objetivo del Proyecto

Desarrollar un sistema que:

* Analice datos climáticos (temperatura, lluvia, humedad, etc.).
* Evalúe las condiciones del suelo.
* Genere **recomendaciones automáticas de riego y manejo del cultivo**.
* Ayude a mejorar la productividad y sostenibilidad del cultivo de aguacate.

---

## 🌳 Requerimientos del Cultivo de Aguacate

A continuación, se muestran las **condiciones óptimas** necesarias para el cultivo del aguacate, las cuales son la base del sistema de recomendaciones:

### 🌡️ Temperatura

* **Temperatura ideal:** 20 °C a 25 °C

### 💧 Humedad del Suelo

* **Humedad óptima:** 40 %

### 🌧️ Consumo de Agua

* **Agua requerida al año:** 130 cm

### 🧪 pH del Suelo

* **pH ideal:** entre 6 y 7
* **pH mínimo tolerado:** 5

---

## 🚿 Recomendaciones de Riego

### 🌱 Etapa Inicial (0 a 1 año)

* **Frecuencia:** 2 a 3 veces por semana
* Riego constante para favorecer el desarrollo de raíces

### 🌳 Etapa Adulta (más de 1 año)

* **Frecuencia:** 1 vez por semana
* **Cantidad:** aproximadamente 5 cm de agua por riego

---

## 🌧️ Manejo en Temporada de Lluvias

* Cuando hay **lluvias abundantes**, se recomienda:

  * Aumentar el **nitrógeno**
  * Reforzar **nutrientes del suelo**
* Esto ayuda a compensar la lixiviación de nutrientes causada por el exceso de agua.

---

## 🤖 ¿Cómo Funciona el Sistema?

1. Obtiene datos en tiempo real desde **APIs climáticas**.
2. Analiza:

   * Temperatura
   * Precipitación
   * Humedad
   * Condiciones del suelo
3. Compara los datos con los requerimientos del cultivo.
4. Genera **recomendaciones personalizadas** de:

   * Riego
   * Fertilización
   * Manejo del cultivo

---



## 🌎 Impacto

* Uso eficiente del agua 💧
* Mejora del rendimiento del cultivo 🌱
* Apoyo a la agricultura sostenible ♻️

---




>>>>>>> 24d9e85b5448991a02991ad28c3005d8db80d167

