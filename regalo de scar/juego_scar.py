import streamlit as st  # type: ignore[import-not-found]
import streamlit.components.v1 as components  # type: ignore[import-not-found]
import base64
import os
import time
import json

st.set_page_config(page_title="Misión Cumpleaños de Scar", page_icon="🎂")

# --- MOTOR DE AUDIO AUTOMATICO POR CARPETAS ---
directorio_app = os.path.dirname(os.path.abspath(__file__))
CARPETA_AMBIENTE = "ambiente"
CARPETA_BRAINROT = "sonidos brainrot"


def obtener_carpeta(nombre_carpeta):
    candidatos = (
        os.path.join(directorio_app, nombre_carpeta),
        os.path.join(directorio_app, "regalo de scar", nombre_carpeta),
        os.path.join(os.path.dirname(directorio_app), "regalo de scar", nombre_carpeta),
    )
    for candidato in candidatos:
        if os.path.isdir(candidato):
            return candidato
    return os.path.join(directorio_app, nombre_carpeta)


def cargar_audios_carpeta(carpeta):
    audios = []
    tipos = {
        ".mp3": "audio/mpeg",
        ".wav": "audio/wav",
        ".ogg": "audio/ogg",
    }
    if os.path.isdir(carpeta):
        for archivo in sorted(os.listdir(carpeta)):
            extension = os.path.splitext(archivo)[1].lower()
            if extension in tipos:
                ruta_completa = os.path.join(carpeta, archivo)
                with open(ruta_completa, "rb") as f:
                    contenido = base64.b64encode(f.read()).decode()
                    audios.append({"data": contenido, "mime": tipos[extension]})
    return audios


lista_ambiente = cargar_audios_carpeta(obtener_carpeta(CARPETA_AMBIENTE))
lista_brainrot = cargar_audios_carpeta(obtener_carpeta(CARPETA_BRAINROT))
ambiente = lista_ambiente[0] if lista_ambiente else None

if ambiente or lista_brainrot:
    ambiente_js = json.dumps(ambiente)
    js_array_brainrot = json.dumps(lista_brainrot)
    html_audio = f"""
    <script>
        if (!window.parent.audioIniciado) {{
            window.parent.audioIniciado = true;

            const ambiente = {ambiente_js};
            let bgMusic = null;
            if (ambiente) {{
                bgMusic = new Audio("data:" + ambiente.mime + ";base64," + ambiente.data);
                bgMusic.loop = true;
                bgMusic.volume = 0.35;
            }}

            const memes = {js_array_brainrot};

            function lanzarBrainrot() {{
                if (memes.length > 0) {{
                    const sonido = memes[Math.floor(Math.random() * memes.length)];
                    const sfx = new Audio("data:" + sonido.mime + ";base64," + sonido.data);
                    sfx.volume = 1.0;
                    sfx.play().catch(e => console.log("Esperando clic..."));
                }}
                const siguienteTiempo = Math.floor(Math.random() * (30000 - 15000 + 1)) + 15000;
                setTimeout(lanzarBrainrot, siguienteTiempo);
            }}

            window.parent.document.addEventListener("click", function iniciarTodo() {{
                if (bgMusic) {{
                    bgMusic.play();
                }}
                setTimeout(lanzarBrainrot, 6700);
                window.parent.document.removeEventListener("click", iniciarTodo);
            }});
        }}
    </script>
    """
    components.html(html_audio, height=0, width=0)

# Inicializar memoria de la escena
if "escena" not in st.session_state:
    st.session_state.escena = "inicio"

def ir_a(nueva_escena):
    st.session_state.escena = nueva_escena

# ==========================================
# ESCENA 0: INICIO
# ==========================================
if st.session_state.escena == "inicio":
    st.title("🏴‍☠️ OPERACIÓN: CUMPLEAÑOS DE SCAR 🎂")
    st.write("Es 26 de noviembre. El Gobierno Mundial (y la lógica) han intentado esconder tu regalo de cumpleaños en algún lugar del multiverso.")
    st.info("💡 **Tip:** Cada decisión te lleva a una realidad distinta. ¡Juega varias veces para desbloquear los 6 finales absurdos!")
    
    st.write("### Elige tu transporte para zarpar:")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⛵ Un barco pirata hecho de cartón mojado", use_container_width=True):
            st.toast("¡Logro: Capitana sin presupuesto!")
            ir_a("isla_zoro")
            st.rerun()
        if st.button("🚀 La nave Bebop sin gasolina y sin comida", use_container_width=True):
            st.toast("¡Logro: Cazarrecompensas en quiebra!")
            ir_a("ruta_bebop")
            st.rerun()
    with col2:
        if st.button("🛶 Una balsa vikinga remada por Thorfinn", use_container_width=True):
            st.toast("¡Logro: Modo pacifista activado!")
            ir_a("isla_vinland")
            st.rerun()
        if st.button("🔭 Un astrolabio prohibido del siglo XV", use_container_width=True):
            st.toast("¡Logro: Hereje de la astronomía!")
            ir_a("ruta_tierra")
            st.rerun()

# ==========================================
# RUTA A: ISLA DE ZORO Y LA FRUTA CONFUNDIDA
# ==========================================
elif st.session_state.escena == "isla_zoro":
    st.header("🏝️ Isla 1A: El Mercado de la Lógica Rota")
    st.write("Tu barco de cartón sobrevive de milagro. Al bajar, te encuentras a Zoro mirando fijamente una **pera que tiene un cartel gigante que dice 'PIÑA'**.")
    st.write("*'Oye Scar, me dijeron que esta fruta te da poderes de cumpleañera... pero sabe raro.'*")
    
    if st.button("🍎 Decirle: 'Zoro, eso es claramente un pato'"):
        ir_a("isla_pato")
        st.rerun()
    if st.button("🗡️ Quitarle la pera y darle una espada de plástico"):
        ir_a("isla_jefe_absurdo")
        st.rerun()

# ==========================================
# RUTA B: ISLA DE VINLAND (EL CAMINO DE LA PAZ)
# ==========================================
elif st.session_state.escena == "isla_vinland":
    st.snow()
    st.header("❄️ Isla 1B: Las Tierras Heladas del Norte")
    st.write("Thorfinn deja de remar, te mira muy serio en medio de la tormenta de nieve y te dice:")
    st.warning("No tienes enemigos, Scar. Nadie tiene enemigos... excepto los que no te felicitan hoy.")
    
    if st.button("🤝 Responder: 'Tienes razón, vamos por pastel'"):
        ir_a("final_vikingo")
        st.rerun()
    if st.button("🔥 Gritar: '¡YO QUIERO CAOS, DAME UN GEAR 5!'"):
        ir_a("isla_jefe_absurdo")
        st.rerun()

# ==========================================
# RUTA C: COWBOY BEBOP (CAZARRECOMPENSAS DEL PASTEL)
# ==========================================
elif st.session_state.escena == "ruta_bebop":
    st.header("🎷 Órbita 1C: Jazz Espacial y Refrigerador Vacío")
    st.write("Spike Spiegel está fumando un cigarro doblado mientras Jet grita porque Ed hackeó el microondas para minar criptomonedas.")
    st.write("*'Escucha Scar... tenemos una recompensa de 50 millones de Woolongs por capturar un Pastel de Tres Leches prófugo en Ganímedes. Pero no tenemos dinero ni para el peaje.'*")
    
    if st.button("🥩 Comer pimientos con carne (sin carne) y despegar igual"):
        ir_a("final_bebop")
        st.rerun()
    if st.button("🐕 Dejar que Ein el corgi conduzca la nave"):
        st.toast("¡Ein tiene más IQ que toda la tripulación!")
        ir_a("ruta_jojo")
        st.rerun()

# ==========================================
# RUTA D: ORB / THE MOVEMENTS OF THE EARTH
# ==========================================
elif st.session_state.escena == "ruta_tierra":
    st.header("🌌 Observatorio 1D: El Movimiento de la Tierra")
    st.write("Estás escondida en un bosque polaco mirando las estrellas junto a Rafal y Oczy. De repente aparece un inquisidor con cara de pocos amigos.")
    st.write("*'¡ALTO AHÍ! Según las leyes oficiales, la Tierra es el centro del universo y hoy NO es un día especial.'*")
    
    if st.button("📜 Gritar: '¡Y sin embargo, la Tierra gira y hoy es mi cumpleaños!'"):
        ir_a("final_tierra")
        st.rerun()
    if st.button("💪 Hacer una pose dramática tan exagerada que te dislocas la espalda"):
        ir_a("ruta_jojo")
        st.rerun()

# ==========================================
# RUTA E: JOJO'S BIZARRE ADVENTURE (DESVÍO EXTRAÑO)
# ==========================================
elif st.session_state.escena == "ruta_jojo":
    st.header("ゴゴゴ Zona Bizarra: El Usuario de Stand Enemigo ゴゴゴ")
    st.write("El ambiente se vuelve morado con verde neón. Un tipo extremadamente musculoso vestido con ropa llena de agujeros te señala con el dedo:")
    st.error("「¡Hoho! ¿Te acercas a mí en lugar de huir? ¡Incluso sabiendo que mi Stand 『BIRTHDAY PARADOX』 te hará cumplir años en cámara lenta!」")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("👊 'No puedo recibir mis regalos sin acercarme más'"):
            ir_a("final_jojo")
            st.rerun()
    with col2:
        if st.button("🏃‍♂️ Usar la técnica secreta de los Joestar: ¡NIGERUNDAYO!"):
            st.toast("¡Escapaste directo al jefe final!")
            ir_a("isla_jefe_absurdo")
            st.rerun()

# ==========================================
# SUB-ISLA A1: EL TRIBUNAL DE LOS PATOS
# ==========================================
elif st.session_state.escena == "isla_pato":
    st.header("🦆 Isla 2: El Tribunal Supremo de los Patos")
    st.write("Por haber insultado a la pera-piña, un ejército de patos con corbata te rodea.")
    st.write("El Juez Pato golpea su martillo y exige saber: **¿Qué se celebra hoy en todo el océano?**")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎉 ¡Que Scar cumple un año más de vida!"):
            ir_a("final_pirata")
            st.rerun()
    with col2:
        if st.button("🤡 El día internacional de la pera-piña"):
            st.error("¡Respuesta incorrecta! El Juez Pato te lanza un pastelazo en la cara.")
            time.sleep(1.5)
            ir_a("final_meme")
            st.rerun()

# ==========================================
# SUB-ISLA COMÚN: EL JEFE FINAL ABSURDO
# ==========================================
elif st.session_state.escena == "isla_jefe_absurdo":
    st.header("🌋 Isla Final: La Cueva del Sin Sentido")
    with st.spinner("Calculando nivel de absurdez..."):
        time.sleep(1)
    st.write("Aparece un enemigo final: Un caracol transpondedor (Den Den Mushi) gigante con gafas de sol que bloquea el cofre de tu cumpleaños.")
    st.write("'Puru puru puru... Para abrir este cofre debes aceptar que hoy eres la protagonista del mundo.'")
    if st.button("👑 Aceptar mi destino de cumpleañera suprema"):
        ir_a("final_pirata")
        st.rerun()

# ==========================================
# FINALES DIFERENTES (TODOS CELEBRAN SU CUMPLE)
# ==========================================
elif st.session_state.escena == "final_pirata":
    st.balloons()
    st.title("🏴‍☠️ FINAL 1: LA REINA DE LOS PIRATAS CUMPLEAÑEROS 🎂")
    st.success("¡FELIZ CUMPLEAÑOS, SCAR!")
    st.write("""
Has cruzado el Grand Line, sobreviviste a la falta de neuronas de este juego y encontraste el verdadero tesoro: ¡Un año más de vida!
Espero que hoy te la pases increíble, que te rías de las cosas más absurdas posibles y que todos tus deseos se cumplan. ¡Disfruta muchísimo tu día! 🎉
""")
elif st.session_state.escena == "final_vikingo":
    st.snow()
    st.title("⚔️ FINAL 2: LA VERDADERA GUERRERA DE VINLAND 🎂")
    st.success("¡FELIZ CUMPLEAÑOS, SCAR!")
    st.write("""
Encontraste la tierra prometida donde no hay enemigos, no hay estrés y sobra el pastel de cumpleaños.
Que este nuevo año de vida venga cargado de paz, aventuras épicas y muchísimas risas sin sentido. ¡Pásala genial hoy! 🥳
""")
elif st.session_state.escena == "final_jojo":
    st.balloons()
    st.title("ゴゴゴ FINAL 3: JOJO'S BIZARRE BIRTHDAY ADVENTURE 🎂")
    st.success("¡YARE YARE DAZE... FELIZ CUMPLEAÑOS, SCAR!")
    st.write("""
Despertaste tu propio Stand: 『CAKE EXPERIENCE REQUIEM』. Su habilidad absoluta es anular cualquier mal día y convertir cada segundo de hoy en pura diversión bizarra.
To Be Continued... ➡️ (Hasta el próximo cumpleaños) 🎉
""")
elif st.session_state.escena == "final_bebop":
    st.balloons()
    st.title("🎷 FINAL 4: SEE YOU SPACE BIRTHDAY GIRL... 🎂")
    st.success("¡FELIZ CUMPLEAÑOS, SCAR!")
    st.write("""
Al final el pastel escapó por una escotilla y seguimos sin un centavo en la cuenta, pero el solo de saxofón de fondo estuvo espectacular.
Que este nuevo viaje alrededor del sol esté lleno de buenas historias, música increíble y cero problemas. Bang. 👉✨
""")
elif st.session_state.escena == "final_tierra":
    st.snow()
    st.title("🔭 FINAL 5: LA VERDAD QUE MUEVE EL UNIVERSO 🎂")
    st.success("¡FELIZ CUMPLEAÑOS, SCAR!")
    st.write("""
La Inquisición no pudo detener el conocimiento: está científicamente comprobado que la Tierra da una vuelta completa al Sol solo para celebrar que hoy naciste tú.
Gracias por iluminar el universo con tu humor y tu forma de ser. ¡Que tengas un año astronómicamente épico! 🌍✨
""")
elif st.session_state.escena == "final_meme":
    st.balloons()
    st.title("🍐 FINAL SECRETO: DIOSA DE LA PERA-PIÑA 🍍")
    st.warning("¡Desbloqueaste el final oculto por responder pura tontería!")
    st.write("""
Los patos se rinden ante tu nivel de humor absurdo y te coronan como la cumpleañera más random de los siete mares.
¡FELIZ CUMPLEAÑOS, SCAR! Nunca cambies ese sentido del humor que hace que todo sea mil veces más divertido. 🎂🎉
""")

# Botón permanente abajo para volver a empezar y explorar otras rutas

if st.session_state.escena != "inicio":
    st.divider()
    if st.button("🔄 Volver al inicio para probar otra ruta"):
        ir_a("inicio")
        st.rerun()
