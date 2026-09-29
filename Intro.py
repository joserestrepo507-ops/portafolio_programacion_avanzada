import base64
import html
import io
from pathlib import Path

import streamlit as st
from PIL import Image

# ──────────────────────────────────────────────────────────────
# Datos editables
# ──────────────────────────────────────────────────────────────
NOMBRE = "José Daniel Restrepo Ramírez"
PERFIL = "Estudiante de ingeniería de software en la Institución Universitaria Pascual Bravo, Medellín"
SITIO_EJERCICIOS = "https://sites.google.com/view/aplicacionesdeia/inicio"

# Deja vacío lo que no quieras mostrar en el pie de página.
CONTACTO = {
    "GitHub": "joserestrepo507-ops",
    "LinkedIn": "",
    "Correo": "jose.restrepo507@pascualbravo.edu.co", 
}

SOBRE_EL_CURSO = (
    "El principal interés del módulo implementar estrategias enfocadas a la cuarta revolución industrial, "
    "específicamente al auge de la análitica de datos y la inteligencia artificial, permitiéndole al futuro ingeniero de software direccionar actividades que permitan "
    "tomar decisiones en cadenas productivas basadas en el procesamiento de datos con la finalidad de optimizar procesos y disminuir costos."
)

CATEGORIAS = ["Todos", "Fundamentos", "Regresión", "Clasificación", "Series de tiempo", "Audio y texto"]

PROYECTOS = [
    {
        "titulo": "¿Qué fruta es más parecida?",
        "categoria": "Clasificación",
        "descripcion": "Compara una fruta con las más parecidas según sus características, usando un modelo entrenado.",
        "imagen": "Pera.png",
        "url": "https://classfruta-btgmcsws8r7zumh7qhwtuc.streamlit.app",
    },
    {
        "titulo": "Descenso de gradiente interactivo",
        "categoria": "Fundamentos",
        "descripcion": "Sigue paso a paso cómo el descenso de gradiente busca el mínimo de una función.",
        "imagen": "txt_to_audio.png",
        "url": "https://compuavanzadagradiente-gxnut9hj5byu8wdjrwcgds.streamlit.app",
    },
    {
        "titulo": "Detector de anomalías",
        "categoria": "Fundamentos",
        "descripcion": "Detecta valores atípicos en un conjunto de datos y compara la complejidad de los algoritmos usados (lógica, Big-O y NumPy).",
        "imagen": "OIG5.jpg",
        "url": "https://detectoranomalias-nqhdajsavrdjkkymnjblsj.streamlit.app",
    },
    {
        "titulo": "Datos: preparación y estructura",
        "categoria": "Fundamentos",
        "descripcion": "Explora cómo limpiar, estructurar y preparar datos antes de construir un modelo.",
        "imagen": "OIG8.jpg",
        "url": "https://appdedatos-zjqbt9mw7kcjyyzvebipmu.streamlit.app",
    },
    {
        "titulo": "Nivel de cauce en Guarne",
        "categoria": "Series de tiempo",
        "descripcion": "Monitorea el nivel del cauce en la quebrada La Mosca, estación 23, cerca del aeropuerto José María Córdova.",
        "imagen": "data_analisis.png",
        "url": "https://nivelcornare-2u26pudtubo8mouvxd5qmb.streamlit.app",
    },
    {
        "titulo": "Transcriptor de audio y video",
        "categoria": "Audio y texto",
        "descripcion": "Transcribe archivos de audio y video a texto.",
        "imagen": "OIG3.jpg",
        "url": "https://transcript-whisper.streamlit.app/",
    },
    {
        "titulo": "Regresión: conceptos clave",
        "categoria": "Regresión",
        "descripcion": "Repasa de forma interactiva los conceptos clave de un modelo de regresión.",
        "imagen": "Chat_pdf.png",
        "url": "https://regresionconceptos-rheeg8nqvdq95r4ufs7n85.streamlit.app",
    },
    {
        "titulo": "Serie de tiempo de un sensor IoT",
        "categoria": "Series de tiempo",
        "descripcion": "Analiza los datos de un sensor IoT como una serie de tiempo.",
        "imagen": "OIG4.jpg",
        "url": "https://seriestiempo-jg7zlzjahxwmmcpnvvruoi.streamlit.app",
    },
    {
        "titulo": "Calidad del aire CORNARE (MARCO)",
        "categoria": "Series de tiempo",
        "descripcion": "Pronostica los niveles de PM10 y PM2.5 con modelos SARIMA, Holt-Winters y ventana deslizante.",
        "imagen": "OIG6.jpg",
        "url": "https://pronosticocornare-geewhjfvz77suqqbdhtvuh.streamlit.app",
    },
    {
        "titulo": "Predictor de sensación térmica",
        "categoria": "Regresión",
        "descripcion": "Estima la sensación térmica a partir de variables climáticas con un modelo de regresión.",
        "imagen": "Chat_pdf.png",
        "url": "https://regresionguiado-z2lkxwmmtvwtbfncm8urry.streamlit.app",
    },
    {
        "titulo": "¿Lloverá mañana?",
        "categoria": "Clasificación",
        "descripcion": "Predice la probabilidad de lluvia para mañana con un modelo de regresión logística.",
        "imagen": "OIG4.jpg",
        "url": "https://regresionlogistica-k7raw4gtuuhn7ecddww5hj.streamlit.app",
    },
    {
        "titulo": "KNN con datos de suelos de AGROSAVIA",
        "categoria": "Clasificación",
        "descripcion": "Clasifica la fertilidad del suelo (baja, media o alta) con el algoritmo KNN y datos de AGROSAVIA.",
        "imagen": "OIG6.jpg",
        "url": "https://knnsuelos-eeiet48jys5ybjnbdxucz4.streamlit.app",
    },
]

BASE = Path(__file__).parent
NUMEROS = {3: "Tres", 4: "Cuatro", 5: "Cinco", 6: "Seis", 7: "Siete", 8: "Ocho", 9: "Nueve", 10: "Diez", 11: "Once", 12: "Doce"}

st.set_page_config(page_title=f"Portafolio de IA, {NOMBRE}", page_icon="🤖", layout="wide")


# ──────────────────────────────────────────────────────────────
# Utilidades
# ──────────────────────────────────────────────────────────────
def limpiar(bloque: str) -> str:
    """Une el HTML en una sola línea para que Markdown no lo interprete como código."""
    return "".join(linea.strip() for linea in bloque.splitlines())


@st.cache_data(show_spinner=False)
def imagen_base64(nombre: str, ancho: int = 720) -> str:
    img = Image.open(BASE / nombre).convert("RGB")
    img.thumbnail((ancho, ancho))
    buffer = io.BytesIO()
    img.save(buffer, format="JPEG", quality=82, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buffer.getvalue()).decode()


def e(texto: str) -> str:
    return html.escape(texto, quote=True)


ICONO_EXTERNO = (
    '<svg width="15" height="15" viewBox="0 0 16 16" fill="none" aria-hidden="true">'
    '<path d="M6 3H3.5A1.5 1.5 0 0 0 2 4.5v8A1.5 1.5 0 0 0 3.5 14h8a1.5 1.5 0 0 0 1.5-1.5V10'
    'M9 2h5v5M14 2 7.5 8.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" '
    'stroke-linejoin="round"/></svg>'
)

# ──────────────────────────────────────────────────────────────
# Estilos
# ──────────────────────────────────────────────────────────────
ESTILOS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Figtree:wght@400;500;600&display=swap');
:root{--bg:#F4F5F7;--surface:#FFFFFF;--ink:#1B2130;--muted:#586174;--line:#DDE1E8;--accent:#2540F5;--accent-soft:#E6EAFE;--radius:14px;--display:'Bricolage Grotesque','Segoe UI',system-ui,sans-serif;--text:'Figtree','Segoe UI',system-ui,sans-serif;}
.stApp,[data-testid="stAppViewContainer"]{background:var(--bg);font-family:var(--text);}
[data-testid="stHeader"],[data-testid="stToolbar"],[data-testid="stDecoration"],#MainMenu,footer{display:none !important;}
[data-testid="stMainBlockContainer"],.block-container{max-width:1180px;padding:1.5rem 1.5rem 3rem !important;}
.pf{font-family:var(--text);color:var(--ink);}
.pf *{box-sizing:border-box;}
.pf a:focus-visible{outline:3px solid var(--accent);outline-offset:3px;border-radius:6px;}
.pf-nav{display:flex;justify-content:space-between;align-items:center;padding:.4rem 0 1.1rem;border-bottom:1px solid var(--line);}
.pf .pf-brand{white-space:nowrap;font-family:var(--display);font-weight:700;font-size:1.1rem;color:var(--ink);text-decoration:none;}
.pf-links{display:flex;gap:1.6rem;}
.pf .pf-links a{white-space:nowrap;color:var(--muted);text-decoration:none;font-weight:500;font-size:.98rem;}
.pf .pf-links a:hover{color:var(--accent);}
.pf-hero{display:grid;grid-template-columns:1.1fr .9fr;gap:3.5rem;align-items:center;padding:3.5rem 0 3rem;}
.pf h1.pf-title{font-family:var(--display);font-weight:700;font-size:clamp(2.1rem,4.4vw,3.6rem);line-height:1.02;letter-spacing:-.028em;margin:0 0 1.25rem;padding:0;color:var(--ink);}
.pf p.pf-lead{font-size:1.15rem;line-height:1.55;color:var(--muted);max-width:33rem;margin:0 0 .9rem;}
.pf p.pf-who{font-size:.98rem;color:var(--ink);font-weight:500;margin:0 0 1.9rem;}
.pf-cta{display:flex;flex-wrap:wrap;gap:.75rem;}
.pf a.pf-btn{display:inline-flex;align-items:center;gap:.5rem;padding:.75rem 1.2rem;border-radius:10px;font-weight:600;font-size:1rem;text-decoration:none;border:1px solid transparent;}
.pf a.pf-btn-primary{background:var(--accent);color:#fff;}
.pf a.pf-btn-primary:hover{background:#1B33D6;}
.pf a.pf-btn-ghost{background:var(--surface);color:var(--ink);border-color:var(--line);}
.pf a.pf-btn-ghost:hover{border-color:var(--accent);color:var(--accent);}
.pf-collage{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:10px;aspect-ratio:1/1.05;}
.pf-collage img{width:100%;height:100%;object-fit:cover;border-radius:var(--radius);display:block;}
.pf-collage img:first-child{grid-row:span 2;}
.pf-sechead{display:flex;justify-content:space-between;align-items:baseline;gap:1rem;margin:2.25rem 0 .9rem;scroll-margin-top:1rem;}
.pf h2.pf-h2{font-family:var(--display);font-weight:700;font-size:1.9rem;letter-spacing:-.02em;margin:0;padding:0;color:var(--ink);}
.pf .pf-count{color:var(--muted);font-size:.98rem;}
.pf-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1.5rem;margin:.5rem 0 0;}
.pf-card{background:var(--surface);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;display:flex;flex-direction:column;}
.pf-card img{width:100%;aspect-ratio:4/3;object-fit:cover;display:block;}
.pf-body{padding:1.1rem 1.25rem 1.3rem;display:flex;flex-direction:column;gap:.5rem;flex:1;}
.pf .pf-tag{align-self:flex-start;font-size:.82rem;font-weight:600;color:var(--accent);background:var(--accent-soft);padding:.2rem .65rem;border-radius:999px;}
.pf h3.pf-h3{font-family:var(--display);font-weight:700;font-size:1.3rem;letter-spacing:-.012em;line-height:1.2;margin:.2rem 0 0;padding:0;color:var(--ink);}
.pf .pf-body p{color:var(--muted);line-height:1.5;margin:0;font-size:.97rem;flex:1;}
.pf a.pf-open{margin-top:.7rem;align-self:flex-start;display:inline-flex;align-items:center;gap:.45rem;font-weight:600;color:var(--ink);text-decoration:none;border-bottom:2px solid var(--accent);padding-bottom:1px;}
.pf a.pf-open:hover{color:var(--accent);}
.pf-about{display:grid;grid-template-columns:1fr 1fr;gap:3.5rem;padding:3rem 0;margin-top:3rem;border-top:1px solid var(--line);}
.pf-about p{font-size:1.08rem;line-height:1.65;color:var(--muted);margin:0 0 1.25rem;max-width:34rem;}
.pf-foot{display:flex;justify-content:space-between;flex-wrap:wrap;gap:1rem;padding:1.4rem 0 0;border-top:1px solid var(--line);color:var(--muted);font-size:.92rem;}
.pf-foot nav{display:flex;gap:1.25rem;}
.pf .pf-foot a{color:var(--ink);font-weight:500;text-decoration:none;}
.pf .pf-foot a:hover{color:var(--accent);}
[data-testid="stPills"]{margin-top:.25rem;}
@media (max-width:860px){
.pf-hero{grid-template-columns:1fr;gap:2rem;padding:2.25rem 0 1.5rem;}
.pf-about{grid-template-columns:1fr;gap:1.25rem;}
.pf-collage{aspect-ratio:16/10;grid-template-rows:1fr 1fr;}
.pf-links{gap:1.1rem;}
}
@media (max-width:520px){
.pf-links a:nth-child(2){display:none;}
.pf-hero{padding-top:1.75rem;}
}
</style>
"""
st.markdown(limpiar(ESTILOS), unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────
# Navegación y portada
# ──────────────────────────────────────────────────────────────
total = len(PROYECTOS)
collage = "".join(
    f'<img src="{imagen_base64(n, 640)}" alt="" loading="lazy">'
    for n in ("OIG6.jpg", "OIG4.jpg", "data_analisis.png")
)

st.markdown(
    limpiar(
        f"""
<div class="pf">
<nav class="pf-nav" aria-label="Principal">
<a class="pf-brand" href="#inicio">{e(NOMBRE)}</a>
<div class="pf-links"><a href="#proyectos">Proyectos</a><a href="#sobre-el-curso">Sobre el curso</a><a href="#contacto">Contacto</a></div>
</nav>
<header class="pf-hero" id="inicio">
<div>
<h1 class="pf-title">{NUMEROS.get(total, total)} aplicaciones realizadas en clase.</h1>
<p class="pf-lead">Portafolio Programación Avanzada. Cada proyecto está publicado en línea y funciona desde el navegador.</p>
<p class="pf-who">{e(NOMBRE)}, {e(PERFIL[0].lower() + PERFIL[1:])}</p>
<div class="pf-cta">
<a class="pf-btn pf-btn-primary" href="#proyectos">Ver proyectos</a>
<a class="pf-btn pf-btn-ghost" href="{e(SITIO_EJERCICIOS)}" target="_blank" rel="noopener">Ejercicios del curso {ICONO_EXTERNO}</a>
</div>
</div>
<div class="pf-collage">{collage}</div>
</header>
</div>
"""
    ),
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────────────────────
# Proyectos
# ──────────────────────────────────────────────────────────────
st.markdown(
    limpiar(
        f"""
<div class="pf"><div class="pf-sechead" id="proyectos">
<h2 class="pf-h2">Proyectos</h2><span class="pf-count">{total} aplicaciones</span>
</div></div>
"""
    ),
    unsafe_allow_html=True,
)

seleccion = st.pills(
    "Filtrar por categoría",
    CATEGORIAS,
    selection_mode="single",
    default="Todos",
    label_visibility="collapsed",
)
seleccion = seleccion or "Todos"
visibles = [p for p in PROYECTOS if seleccion == "Todos" or p["categoria"] == seleccion]

tarjetas = "".join(
    f"""
<article class="pf-card">
<img src="{imagen_base64(p['imagen'])}" alt="Ilustración del proyecto {e(p['titulo'])}" loading="lazy">
<div class="pf-body">
<span class="pf-tag">{e(p['categoria'])}</span>
<h3 class="pf-h3">{e(p['titulo'])}</h3>
<p>{e(p['descripcion'])}</p>
<a class="pf-open" href="{e(p['url'])}" target="_blank" rel="noopener" aria-label="Abrir {e(p['titulo'])} en una pestaña nueva">Abrir aplicación {ICONO_EXTERNO}</a>
</div>
</article>
"""
    for p in visibles
)
st.markdown(limpiar(f'<div class="pf"><div class="pf-grid">{tarjetas}</div></div>'), unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────
# Sobre el curso y pie de página
# ──────────────────────────────────────────────────────────────
enlaces = "".join(
    f'<a href="{e(("mailto:" + url) if nombre == "Correo" else url)}" target="_blank" rel="noopener">{e(nombre)}</a>'
    for nombre, url in CONTACTO.items()
    if url
)
bloque_contacto = f"<nav aria-label='Contacto'>{enlaces}</nav>" if enlaces else ""

st.markdown(
    limpiar(
        f"""
<div class="pf">
<section class="pf-about" id="sobre-el-curso">
<h2 class="pf-h2">Sobre el curso</h2>
<div>
<p>{e(SOBRE_EL_CURSO)}</p>
<a class="pf-btn pf-btn-ghost" href="{e(SITIO_EJERCICIOS)}" target="_blank" rel="noopener">Páginas y ejercicios prácticos {ICONO_EXTERNO}</a>
</div>
</section>
<div class="pf-foot" id="contacto" role="contentinfo">
<span>{e(NOMBRE)}</span>
{bloque_contacto}
</div>
</div>
"""
    ),
    unsafe_allow_html=True,
)

