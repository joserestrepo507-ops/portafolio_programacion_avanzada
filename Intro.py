import streamlit as st
from PIL import Image
st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
  st.subheader("Portafolio José Daniel Restrepo Ramírez.")
  parrafo = (
    "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
    "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
    "resulta en una mayor eficiencia y precisión en diversos campos."
  )
  st.write(parrafo)

url_ia="https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("¿Qué fruta es más parecida?")
 image = Image.open('txt_to_audio2.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace usaremos una de las aplicaciones de Inteligencia Artificial") 
 url = "https://classfruta-btgmcsws8r7zumh7qhwtuc.streamlit.app"
 st.write(f"Texto a voz: [Enlace]({url})")

 st.subheader(" Descenso de Gradiente Interactivo")
 image = Image.open('txt_to_audio.png')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como se detectan objetos en Imágenes.") 
 url = "https://compuavanzadagradiente-gxnut9hj5byu8wdjrwcgds.streamlit.app"
 st.write(f"YOLO: [Enlace]({url})")

 st.subheader("Detector de Anomalías: Lógica + Big-O + NumPy")
 image = Image.open('OIG5.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como puedes usar tu modelo entrenado.") 
 url = "https://detectoranomalias-nqhdajsavrdjkkymnjblsj.streamlit.app"
 st.write(f"YOLO: [Enlace]({url})")

with col2: 
 st.subheader("Datos: preparación y estructura")
 image = Image.open('OIG8.jpg')
 st.image(image, width=200)
 st.write("En la siguiente veremos una aplicación que usa la conversión de voz a texto.") 
 url = "https://appdedatos-zjqbt9mw7kcjyyzvebipmu.streamlit.app"
 st.write(f"Voz a texto: [Enlace]({url})")

 st.subheader("Guarne, Quebrada La Mosca, Vía Guarne Aeropuerto José María Cordova Estación 23")
 image = Image.open('data_analisis.png')
 st.image(image, width=190)
 st.write("En la siguiente enlace veremos como se pueden analizar datos usando agentes.") 
 url = "https://nivelcornare-2u26pudtubo8mouvxd5qmb.streamlit.app"
 st.write(f"Datos: [Enlace]({url})")

 st.subheader("Trasnscriptor Audio y Video")
 image = Image.open('OIG3.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como realizamos transcripciones de audio/video.") 
 url = "https://transcript-whisper.streamlit.app/"
 st.write(f"Transcriptor: [Enlace]({url})")


with col3: 
 st.subheader("Regresión conceptos clave")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://regresionconceptos-rheeg8nqvdq95r4ufs7n85.streamlit.app"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Series de Tiempo Sensor IoT interactivo")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://seriestiempo-jg7zlzjahxwmmcpnvvruoi.streamlit.app"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Predictor de calidad del aire CORNARE (MARCO)")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://pronosticocornare-geewhjfvz77suqqbdhtvuh.streamlit.app"
 st.write(f"Vision: [Enlace]({url})")

with col4:
 st.subheader("Predictor de Sensación Térmica")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://regresionguiado-z2lkxwmmtvwtbfncm8urry.streamlit.app"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = ""
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Predictor de calidad del aire CORNARE (MARCO)")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = ""
 st.write(f"Vision: [Enlace]({url})")

