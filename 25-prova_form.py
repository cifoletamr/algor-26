import streamlit as st

st.title("Formulari amb neteja automatitzada només en cas d'èxit")

# 1. Inicialitzem un comptador al session_state per a la clau (key) del formulari
if "form_id" not in st.session_state:
    st.session_state.form_id = 0

# 2. Creem el formulari utilitzant el comptador a la key.
# Si el comptador canvia, Streamlit crearà un formulari totalment buit (reiniciat).
form_key = f"meu_formulari_{st.session_state.form_id}"

with st.form(key=form_key):
    nombre = st.text_input("Introdueix el teu nom:")
    apellidos = st.text_input("cognoms:")
    telefon = st.text_input("telefon:")
    edad = st.slider("Selecciona la teva edat:", 0, 100, 25)
    
    submitted = st.form_submit_button("Enviar")

# 3. Validació lògica despres de prémer el botó
if submitted:
    if not nombre.strip():
        # Hi ha un error: es mostra el missatge i el formulari MANTÉ les dades
        st.error("Si us plau, introdueix un nom vàlid.")
    elif edad < 18:
        # Hi ha un error: es mostra el missatge i el formulari MANTÉ les dades
        st.error("Has de ser major d'edat per enviar aquest formulari.")
    else:
        # L'ENVIAMENT ÉS CORRECTE: 
        # Mostrem el missatge d'èxit
        st.success(f"Dades enviades correctament! Gràcies, {nombre}.")
        
        # Incrementem el comptador per "destruir" el formulari actual i crear-ne un de buit
        st.session_state.form_id += 1
        st.rerun()
