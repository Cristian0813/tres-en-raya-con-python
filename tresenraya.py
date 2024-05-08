# Este código implementa el juego "Tres en Raya"
# Utilizando la biblioteca Tkinter de Python para crear la interfaz de usuario

# Aquí hay una explicación paso a paso del código:

# 1. Función crear_tablero(): Esta función crea y devuelve una lista 2D (una lista de listas) que representa el tablero
#    del juego. Cada elemento de la lista principal representa una fila del tablero, y cada elemento de las listas
#    internas representa una celda del tablero. Inicialmente, todas las celdas están vacías y se representan con espacios
#    en blanco.
#
# 2. Función mostrar_tablero(tablero): Esta función toma el tablero actual como entrada y actualiza la apariencia visual
#    de los botones del tablero para reflejar el estado actual del juego. Los botones se configuran con el texto
#    correspondiente a la ficha del jugador en esa celda. Si la celda está vacía, el botón se activa para que el jugador
#    pueda hacer clic en él y colocar su ficha.
#
# 3. Función verificar_ganador(tablero, jugador): Esta función comprueba si un jugador ha ganado el juego. Recibe como
#    entrada el tablero actual y el jugador cuya ficha se está comprobando. Comprueba todas las filas, columnas y
#    diagonales para ver si el jugador tiene tres fichas en línea en alguna dirección.
#
# 4. Función tablero_lleno(tablero): Esta función verifica si el tablero está lleno, es decir, si no hay espacios vacíos 
#    en el tablero. Si el tablero está lleno y no hay un ganador, el juego termina en empate.
#
# 5. Función cambiar_jugador(jugador): Esta función cambia el jugador actual. Si el jugador actual es 'X', lo cambia a 'O', y viceversa.
#
# 6. Función manejar_click(i, j): Esta función se llama cuando un jugador hace clic en un botón del tablero. Toma la fila i 
#    y la columna j del botón que se ha presionado. Si la celda correspondiente está vacía, coloca la ficha del jugador 
#    actual en esa celda, actualiza el tablero visualmente y verifica si hay un ganador o un empate.
#
# 7. Función reiniciar_juego(): Esta función reinicia el juego. Limpia el tablero, establece al jugador actual como 'X' 
#    y restablece el texto de las etiquetas de resultado. Se llama cuando se presiona el botón "Reiniciar".

import tkinter as tk

# 1. Función para crear el tablero vacío
def crear_tablero():
    return [[' ' for _ in range(3)] for _ in range(3)]

# 2. Función para actualizar la apariencia del tablero
def mostrar_tablero(tablero):
    for i, fila in enumerate(tablero):
        for j, celda in enumerate(fila):
            boton = botones[i][j]
            # Configurar el texto del botón según el contenido de la celda
            boton.config(text=celda, state='disabled' if celda != ' ' else 'normal')

# 3. Función para verificar si hay un ganador
def verificar_ganador(tablero, jugador):
    for fila in tablero:
        if all([celda == jugador for celda in fila]):
            return True
    
    for col in range(3):
        if all([tablero[fila][col] == jugador for fila in range(3)]):
            return True
        
    if all([tablero[i][i] == jugador for i in range(3)]) or all([tablero[i][2 - i] == jugador for i in range(3)]):
        return True
    
    return False

# 4. Función para verificar si el tablero está lleno
def tablero_lleno(tablero):
    return all(all(celda != ' ' for celda in fila) for fila in tablero)

# 5. Función para cambiar el jugador
def cambiar_jugador(jugador):
    return 'X' if jugador == 'O' else 'O'

# 6. Función para manejar el click en un botón del tablero
def manejar_click(i, j):
    global jugador_actual, x_ganadas, o_ganadas

    # Verificara si la celda está vacía
    if tablero[i][j] == ' ':
        # Colocar la ficha del jugador actual en la celda
        tablero[i][j] = jugador_actual
        # Actualizar la apariencia visual del tablero
        mostrar_tablero(tablero)
        # Verificar si se hay ganador
        if verificar_ganador(tablero, jugador_actual):
            # Actualizar el texto del resultado y contador de victorias
            if jugador_actual == 'X':
                x_ganadas += 1
                resultado_texto_gana.set(f"¡Jugador X gana!")
                resultado_texto_contador.set(f"X: {x_ganadas} || O: {o_ganadas}")
            else:
                o_ganadas += 1
                resultado_texto_gana.set(f"¡Jugador O gana!")
                resultado_texto_contador.set(f"X: {x_ganadas} || O: {o_ganadas}")
        # Si no hay un ganador y el tablero está lleno, es un empate
        elif tablero_lleno(tablero):
            resultado_texto_gana.set("¡Es un empate!")
            resultado_texto_contador.set(f"X: {x_ganadas} || O: {o_ganadas}")
        # Cambiar al siguiente jugador
        else:
            jugador_actual = cambiar_jugador(jugador_actual)

# 7. Función para reiniciar el juego
def reiniciar_juego():
    global tablero, jugador_actual
    
    # Crea un tablero vacío y establecer el primer jugador como 'X'
    tablero = crear_tablero()
    jugador_actual = 'X'

    # Reiniciar el texto del resultado
    resultado_texto_gana.set(" ")

    # Restablece la apariencia visual de los botones del tablero
    for i in range(3):
        for j in range(3):
            boton = botones[i][j]
            boton.config(text=' ', state='normal')

# Crea la ventana principal
raiz = tk.Tk()
raiz.title("Tres en Raya")

# Marco principal para organizar los elemento de la interfaz
marco_principal = tk.Frame(raiz)
marco_principal.pack(padx=10, pady=10)

# Etiqueta del título del juego
titulo_etiqueta = tk.Label(marco_principal, text="Tres en Raya", font=('Helvetica', 28))
titulo_etiqueta.grid(row=0, column=0, columnspan=3, pady=10)

# Variable para mostrar el resultado del juego
resultado_texto_gana = tk.StringVar()
resultado_texto_gana.set(" ")
resultado_etiqueta_gana = tk.Label(marco_principal, textvariable = resultado_texto_gana, font=('Helvetica', 12))
resultado_etiqueta_gana.grid(row=1, column=0, columnspan=3)

# Variable para mostrar el contador de victorias
resultado_texto_contador = tk.StringVar()
resultado_etiqueta_contador = tk.Label(marco_principal, textvariable=resultado_texto_contador, font=('Helvetica', 12))
resultado_etiqueta_contador.grid(row=2, column=0, columnspan=3)

# Crear el tablero y establecer el jugador inicial como 'X'
tablero = crear_tablero()
jugador_actual = 'X'
x_ganadas = 0
o_ganadas = 0

# Crea los Botones para el Tablero
botones = []
for i in range(3):
    fila = []
    for j in range(3):
        # Crea un botón para cada celda del tablero
        boton = tk.Button(marco_principal, text=' ', font=('Helvetica', 24), width=5, height=2, command=lambda i=i, j=j: manejar_click(i, j))
        boton.grid(row=i+3, column=j, padx=5, pady=5)
        fila.append(boton)
    botones.append(fila)

# Botón para reiniciar el juego
reiniciar_boton = tk.Button(marco_principal, text="Reiniciar", font=('Helvetica', 18), command=reiniciar_juego)
reiniciar_boton.grid(row=6, column=0, columnspan=3, pady=10)

# Iniciar el bucle principal de la aplicación
raiz.mainloop()