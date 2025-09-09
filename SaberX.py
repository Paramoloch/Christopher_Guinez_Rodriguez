import tkinter as tk
from tkinter import messagebox

def registrar_libro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    genero = genero_var.get()
    anio= entry_anio.get()
    categorias = [cat for cat, var in categorias_vars.items() if var.get()]
    disponibilidad = disponibilidad_var.get()
    copias = entry_copias.get()
    resumen = text_resumen.get("1.0", tk.END).strip()
    idioma = idioma_var.get()
    print(f"Libro registrado: ")
    print(f"Título: {titulo}")
    print(f"Autor: {autor}")
    print(f"Género: {genero}")
    print(f"Año: {anio}")
    print(f"Categorías: {categorias}")
    print(f"Dispoinibilidad: {disponibilidad}")
    print(f"Copias: {copias}")
    print(f"Resumen: {resumen}")
    print(f"Idioma: {idioma}")
    print("-"* 40)

def limpiar_formulario():
    entry_titulo.delete(0, tk.END)
    entry_autor.delete(0, tk.END)
    entry_anio.delete(0, tk.END)
    genero_var.set(None)
    for var in categorias_vars.values():
        var.set(False)
    disponibilidad_var.set(None)
    entry_copias.delete(0, tk.END)
    text_resumen.delete("1.0", tk.END)
    idioma_var.set("Español")

root = tk.Tk()
root.title("Registro de Libros de la Biblioteca SaberX")
root.geometry("600x700")

frame_detalles = tk.LabelFrame(root, text="Detalles del Libro", padx=10, pady=10)
frame_detalles.pack(padx=10, pady=5, fill="x")
tk.Label(frame_detalles, text="Título:").grid(row=0, column=0, sticky="w")
entry_titulo = tk.Entry(frame_detalles, width=50)
entry_titulo.grid(row=0, column=1)
tk.Label(frame_detalles, text="Autor:").grid(row=1, column=0, sticky="w")
entry_autor = tk.Entry(frame_detalles, width=50)
entry_autor.grid(row=1, column=1)
tk.Label(frame_detalles, text="Año de Publicación:").grid(row=2, column=0, sticky="w")
entry_anio = tk.Entry(frame_detalles, width=20)
entry_anio.grid(row=2, column=1, sticky="w")

frame_genero_categoria = tk.LabelFrame(root, text="Género y Categorías", padx=10, pady=10)
frame_genero_categoria.pack(padx=10, pady=5, fill="x")
genero_var = tk.StringVar()
tk.Label(frame_genero_categoria, text="Género:").grid(row=0, column=0, sticky="w")
tk.Radiobutton(frame_genero_categoria, text="Ficción", variable=genero_var, value="Ficción").grid(row=0, column=1, sticky="w")
tk.Radiobutton(frame_genero_categoria, text="No Ficción", variable=genero_var, value="No Ficción").grid(row=0, column=2, sticky="w")
tk.Label(frame_genero_categoria, text="Categorías:").grid(row=1, column=0, sticky="w")
categorias=["Fantasía", "Ciencia Ficción", "Romance", "Misterio", "Historia", "Otras"]
categorias_vars = {}
for idx, cat in enumerate(categorias):
    var= tk.BooleanVar()
    chk = tk.Checkbutton(frame_genero_categoria, text=cat, variable=var)
    chk.grid(row=1+idx//3, column=1 + idx%3, sticky="w")
    categorias_vars[cat] = var

frame_disponibilidad = tk.LabelFrame (root, text="Disponibilidad", padx=10, pady=10)
frame_disponibilidad.pack(padx=10, pady=5, fill="x")
disponibilidad_var = tk.StringVar()
tk.Radiobutton(frame_disponibilidad, text="Disponible", variable=disponibilidad_var, value="Disponible").pack(anchor="w")
tk.Radiobutton(frame_disponibilidad, text="En prestamo", variable=disponibilidad_var, value="En Prestamo").pack(anchor="w")

frame_copias = tk.LabelFrame(root, text="Copias", padx=10, pady=10)
frame_copias.pack(padx=10, pady=5, fill="x")
tk.Label(frame_copias, text="Numero de Copias:").pack(anchor="w")
entry_copias = tk.Entry(frame_copias, width=10)
entry_copias.pack(anchor="w")

frame_resumen = tk.LabelFrame(root, text="Resumen del Libro", padx=10, pady=10)
frame_resumen.pack(padx=10, pady=5, fill="x")
text_resumen = tk.Text(frame_resumen, height=5, width=50)
text_resumen.pack(fill="x")

frame_idioma = tk.LabelFrame(root, text="Idioma", padx=10, pady=10)
frame_idioma.pack(padx=10, pady=5, fill="x")
idioma_var = tk.StringVar(value="Español")
tk.OptionMenu(frame_idioma, idioma_var, "Español", "Inglés", "Francés", "Alemán").pack(anchor="w")

frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

btn_registrar = tk.Button(frame_botones, text="Registrar Libro", command=registrar_libro, bg="green", fg="white", width=20 )
btn_registrar.pack(side="left", padx=5)
btn_limpiar = tk.Button(frame_botones, text="Limpiar Formulario", command=limpiar_formulario, bg="orange", fg="white", width=20)
btn_limpiar.pack(side="right", padx=5)

root.mainloop()




