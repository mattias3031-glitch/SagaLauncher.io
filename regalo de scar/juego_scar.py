import streamlit as st

# Configuración básica de la página (se ve en la pestaña del navegador)
st.set_page_config(page_title="Expedición de Scar", page_icon="🏴‍☠️")

# Inicializar la memoria del juego (en qué paso va)
if "paso" not in st.session_state:
    st.session_state.paso = 0

def avanzar(siguiente_paso):
    st.session_state.paso = siguiente_paso

# --- PANTALLA 0: INICIO ---
if st.session_state.paso == 0:
    st.title("🏴‍☠️ La Gran Expedición Sin Sentido de Scar")
    st.write("Zarparte hacia el Grand Line en busca del verdadero One Piece, pero la lógica ha desaparecido del mundo.")
    
    # Puedes poner un GIF o imagen de internet con su URL, o un archivo local en la misma carpeta
    st.image("https://giphy.com", use_container_width=True)
    
    if st.button("¡Zarpar ahora!", type="primary"):
        avanzar(1)
        st.rerun()

# --- PANTALLA 1: EL ENCUENTRO ABSURDO ---
elif st.session_state.paso == 1:
    st.header("Isla 1: El Mercado del Caos")
    st.write("Desembarcas y te encuentras a Zoro completamente perdido frente a un puesto de frutas. Te señala una pera que tiene un cartel gigante que dice **'PIÑA'** y te pregunta muy serio: *'¿Esto es el One Piece?'*")
    
    # Aquí puedes poner la foto de la pera que dice piña si la guardas como 'pera.jpg' en la misma carpeta
    # st.image("pera.jpg", width=300)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Decirle: 'Sí, cómetela con cáscara'"):
            avanzar(2)
            st.rerun()
    with col2:
        if st.button("Aplicar la de Thorfinn: 'No tengo enemigos, solo frutas confundidas'"):
            avanzar(2)
            st.rerun()

# --- PANTALLA 2: EL DESAFÍO DE LA AMISTAD ---
elif st.session_state.paso == 2:
    st.header("Isla 2: La Tormenta de los 3 Años")
    st.write("De repente, el cielo se oscurece y aparece un pato gigante en un barco de madera exigiendo impuestos por navegar.")
    st.write("Para dejarte pasar, te hace una pregunta mortal: **¿Cuál es el tesoro más grande que has encontrado en estos últimos 3 años?**")
    
    if st.button("Una amistad igual de random que este juego"):
        avanzar(3)
        st.rerun()
    if st.button("El conocimiento de que una pera puede identificarse como piña"):
        avanzar(3)
        st.rerun()

# --- PANTALLA 3: EL TESORO FINAL (CUMPLEAÑOS) ---
elif st.session_state.paso == 3:
    st.balloons() # ¡Lanza globos por toda la pantalla!
    st.title("🎉 ¡FELIZ CUMPLEAÑOS, SCAR! 🎂")
    st.subheader("Has encontrado el verdadero One Piece")
    
    st.write("""
    Ya son **3 años** de amistad, de reírnos de cosas que no tienen ningún sentido 
    y de aguantar nuestras locuras. 
    
    Como diría Thorfinn, en este mundo no tienes enemigos, y como diría Luffy, 
    ¡vamos por muchas más aventuras juntos! Espero que tengas un cumpleaños increíble.
    """)
    
    st.success("🎁 Vale por: Un regalo / salida pendiente cuando nos veamos.")
    
    if st.button("Volver a jugar"):
        avanzar(0)
        st.rerun()