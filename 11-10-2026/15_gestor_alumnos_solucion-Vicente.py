import mysql.connector as con
from mysql.connector import Error


# ============================================================
# CONEXIÓN A LA BASE DE DATOS
# ============================================================

def conectar():
    try:
        return con.connect(host="localhost",
            user="root",
            password="root",
            port=3306,
            database="universidad")

    except Error as error:
        print(f"Error de conexión: {error}")
        return None

# ============================================================
# ALTA DE ALUMNO
# ============================================================

def alta_alumno(dni, nombre, email, curso, nota):

    conexion = conectar()

    if conexion is None:
        return False, "No se ha podido conectar con la base de datos."

    cursor = conexion.cursor()

    try:
        # Comprobar primero si existe el DNI

        sql = """
            SELECT dni
            FROM alumnos
            WHERE dni = %s
        """

        cursor.execute(sql, (dni,))

        if cursor.fetchone():

            return False, "Ya existe un alumno con ese DNI."

        # Insertar alumno

        sql = """
            INSERT INTO alumnos
            (dni, nombre, email, curso, nota)
            VALUES (%s, %s, %s, %s, %s)
        """

        datos = (
            dni,
            nombre,
            email,
            curso,
            nota
        )

        cursor.execute(sql, datos)

        conexion.commit()

        return True, "Alumno añadido correctamente."

    except Error as error:

        return False, f"Error: {error}"

    finally:

        cursor.close()
        conexion.close()


# ============================================================
# BUSCAR ALUMNOS POR CURSO
# ============================================================

def buscar_por_curso(curso):

    conexion = conectar()

    if conexion is None:
        return []

    cursor = conexion.cursor(dictionary=True)

    try:

        sql = """
            SELECT dni, nombre, email, curso, nota
            FROM alumnos
            WHERE curso = %s
            ORDER BY nombre
        """

        cursor.execute(sql, (curso,))

        return cursor.fetchall()

    except Error as error:

        print(f"Error: {error}")
        return []

    finally:

        cursor.close()
        conexion.close()


# ============================================================
# BUSCAR ALUMNO POR DNI
# ============================================================

def buscar_por_dni(dni):

    conexion = conectar()

    if conexion is None:
        return None

    cursor = conexion.cursor(dictionary=True)

    try:

        sql = """
            SELECT dni, nombre, email, curso, nota
            FROM alumnos
            WHERE dni = %s
        """

        cursor.execute(sql, (dni,))

        return cursor.fetchone()

    except Error as error:

        print(f"Error: {error}")
        return None

    finally:

        cursor.close()
        conexion.close()


# ============================================================
# BAJA DE ALUMNO
# ============================================================

def baja_alumno(dni):

    conexion = conectar()

    if conexion is None:
        return False

    cursor = conexion.cursor()

    try:

        sql = """
            DELETE FROM alumnos
            WHERE dni = %s
        """

        cursor.execute(sql, (dni,))

        conexion.commit()

        return cursor.rowcount > 0

    except Error as error:

        print(f"Error: {error}")
        return False

    finally:

        cursor.close()
        conexion.close()


# ============================================================
# OBTENER TODOS LOS CURSOS
# ============================================================

def obtener_cursos():

    conexion = conectar()

    if conexion is None:
        return []

    cursor = conexion.cursor()

    try:

        sql = """
            SELECT DISTINCT curso
            FROM alumnos
            ORDER BY curso
        """

        cursor.execute(sql)

        resultados = cursor.fetchall()

        return [fila[0] for fila in resultados]

    except Error as error:

        print(f"Error: {error}")
        return []

    finally:

        cursor.close()

# ============================================================
# ACTUALIZAR ALUMNO
# ============================================================

def actualizar_alumno(dni, nombre, email, curso, nota):
    conexion = None
    try:
        conexion = conectar()  # Reemplaza 'conectar()' por el nombre exacto de tu función de conexión
        cursor = conexion.cursor()
        sql = """
            UPDATE alumnos
            SET nombre = %s, email = %s, curso = %s, nota = %s
            WHERE dni = %s
        """
        cursor.execute(sql, (nombre, email, curso, nota, dni))
        conexion.commit()

        if cursor.rowcount > 0:
            return True, "Alumno actualizado correctamente."
        else:
            return False, "No se realizaron cambios o no existe el alumno."
    except Exception as e:
        return False, f"Error al actualizar: {e}"
    finally:
        if conexion:
            conexion.close()





""" Proyecto gestión de alumnos:

-Alta de alumnos: A través de una ventana, se solicitan los datos de un
nuevo alumno y se guardan en la base de datos. No se admiten dnis duplicados
si se proporciona un dni que ya existe, el alumno no se añade
y se avisa mediante un mensaje al usuario

-Busqueda de alumnos por curso. Se selecciona un curso en un combo
y debajo se muestra una tabla con los datos de todos los alumnos
de ese curso. En cada fila, aparecerá un botón para borrar a ese alumno

-Busqueda de alumno por dni. Se introduce el dni de un alumno
y se muestran todos sus datos, si no existe, mensaje de advertencia.  """

import importlib
import streamlit as st
import operaciones_bd as op2

#st.write("📂 Ruta real del archivo cargado:", op2.__file__)
#st.write("📋 Funciones disponibles:", dir(op2))

# ============================================================
# CONFIGURACIÓN STREAMLIT
# ============================================================
st.set_page_config(
    page_title="Gestión de Alumnos",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Gestión de Alumnos")
st.write("Aplicación para gestionar los alumnos de la base de datos Universidad.")
st.divider()

# ============================================================
# MENÚ
# ============================================================
opcion = st.sidebar.radio(
    "Selecciona una opción:",
    ["Alta de alumno", "Buscar por curso", "Buscar por DNI","Actualizar alumno"]
)

# ============================================================
# ALTA DE ALUMNO
# ============================================================
if opcion == "Alta de alumno":
    st.header("➕ Alta de alumno")
    with st.form("formulario_alta"):
        dni = st.text_input("DNI")
        nombre = st.text_input("Nombre")
        email = st.text_input("Email")
        curso = st.text_input("Curso")
        nota = st.number_input("Nota", min_value=0.0, max_value=10.0, step=0.5)
        guardar = st.form_submit_button("Guardar alumno")

    if guardar:
        if not dni or not nombre or not email or not curso:
            st.warning("Debes completar todos los campos de texto.")
        else:
            correcto, mensaje = op2.alta_alumno(
                dni.strip().upper(),
                nombre.strip(),
                email.strip(),
                curso.strip(),
                float(nota)
            )
            if correcto:
                st.success(mensaje)
            else:
                st.error(mensaje)

# ============================================================
# BÚSQUEDA POR CURSO
# ============================================================
elif opcion == "Buscar por curso":
    st.header("📚 Buscar alumnos por curso")
    cursos = op2.obtener_cursos()

    if not cursos:
        st.warning("No existen cursos en la base de datos.")
    else:
        curso = st.selectbox("Selecciona un curso:", cursos)
        alumnos = op2.buscar_por_curso(curso)

        if alumnos:
            st.success(f"Se han encontrado {len(alumnos)} alumnos.")

            # Cabecera con 6 columnas (índices 0 al 5)
            columnas = st.columns([2, 2, 3, 2, 1, 1])
            columnas[0].markdown("**DNI**")
            columnas[1].markdown("**Nombre**")
            columnas[2].markdown("**Email**")
            columnas[3].markdown("**Curso**")
            columnas[4].markdown("**Nota**")
            columnas[5].markdown("**Borrar**")
            st.divider()

            # Filas de alumnos usando solo listas/diccionarios nativos
            for alumno in alumnos:
                columnas = st.columns([2, 2, 3, 2, 1, 1])
                columnas[0].write(alumno["dni"])
                columnas[1].write(alumno["nombre"])
                columnas[2].write(alumno["email"])
                columnas[3].write(alumno["curso"])
                #columnas[4].write(alumno["nota"])
                columnas[4].markdown(
                                    f"<p style='font-size: 28px; font-weight: bold;'>{alumno['nota']}</p>",
                                    unsafe_allow_html=True 
                )  # si quieres ajustar los píxeles exactos o cambiar el color,

                with columnas[5]:
                    eliminar = st.button(
                        "🗑️",
                        key=f"borrar_{alumno['dni']}",
                        help="Eliminar alumno"
                    )
                    if eliminar:
                        borrado = op2.baja_alumno(alumno["dni"])
                        if borrado:
                            st.success("Alumno eliminado.")
                            st.rerun()
                        else:
                            st.error("No se ha podido eliminar.")
        else:
            st.info("No hay alumnos matriculados en este curso.")

# ============================================================
# BÚSQUEDA POR DNI
# ============================================================
elif opcion == "Buscar por DNI":
    st.header("🔎 Buscar alumno por DNI")
    dni_buscar = st.text_input("Introduce el DNI:")
    buscar = st.button("Buscar alumno", type="primary")

    if buscar:
        if not dni_buscar:
            st.warning("Introduce un DNI.")
        else:
            alumno = op2.buscar_por_dni(dni_buscar.strip().upper())
            if alumno:
                st.success("Alumno encontrado.")
                st.subheader(f"{alumno['nombre']}")
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**DNI:** {alumno['dni']}")
                    st.write(f"**Nombre:** {alumno['nombre']}")
                    st.write(f"**Email:** {alumno['email']}")
                with col2:
                    st.write(f"**Curso:** {alumno['curso']}")
                    st.write(f"**Nota:** {alumno['nota']}")
            else:
                st.warning("No existe ningún alumno con ese DNI.")


# ============================================================
# ACTUALIZAR ALUMNO
# ============================================================
elif opcion == "Actualizar alumno":
    st.header("✏️ Actualizar datos de alumno")

    dni_editar = st.text_input("Introduce el DNI del alumno a modificar:")
    if st.button("Cargar datos", type="primary"):
        if not dni_editar:
            st.warning("Introduce un DNI.")
        else:
            alumno_encontrado = op2.buscar_por_dni(dni_editar.strip().upper())
            if alumno_encontrado:
                st.session_state["alumno_editar"] = alumno_encontrado
            else:
                st.session_state.pop("alumno_editar", None)
                st.warning("No existe ningún alumno con ese DNI.")

    # Si hay un alumno cargado en memoria, mostramos el formulario precargado
    if "alumno_editar" in st.session_state:
        alumno = st.session_state["alumno_editar"]
        st.info(f"Editando al alumno con DNI: **{alumno['dni']}**")

        with st.form("formulario_actualizar"):
            nuevo_nombre = st.text_input("Nombre", value=alumno["nombre"])
            nuevo_email = st.text_input("Email", value=alumno["email"])
            nuevo_curso = st.text_input("Curso", value=alumno["curso"])
            nueva_nota = st.number_input(
                "Nota",
                min_value=0.0,
                max_value=10.0,
                step=0.5,
                value=float(alumno["nota"])
            )
            actualizar = st.form_submit_button("Guardar cambios")

        if actualizar:
            if not nuevo_nombre or not nuevo_email or not nuevo_curso:
                st.warning("Debes completar todos los campos de texto.")
            else:
                correcto, mensaje = op2.actualizar_alumno(
                    alumno["dni"],
                    nuevo_nombre.strip(),
                    nuevo_email.strip(),
                    nuevo_curso.strip(),
                    float(nueva_nota)
                )
                if correcto:
                    st.success(mensaje)
                    st.session_state.pop("alumno_editar", None)
                else:
                    st.error(mensaje)