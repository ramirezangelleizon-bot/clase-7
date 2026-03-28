import tkinter as tk
from tkinter import ttk

class AppWindow(tk.Tk):
    def __init__(self, task_service):
        super().__init__()
        self._task_service = task_service
        self.title("Gestor de Tareas")
        self.geometry("500x600") # Aumenté un poco el alto para que quepa el botón nuevo
        
        self.create_widgets()
        self.update_table()

    def create_widgets(self):
        # Formulario de entrada
        tk.Label(self, text="Título de la Tarea:").pack(pady=5)
        self.entry_title = tk.Entry(self)
        self.entry_title.pack()

        tk.Label(self, text="Descripción:").pack(pady=5)
        self.entry_desc = tk.Entry(self)
        self.entry_desc.pack()

        # Botones de acción
        tk.Button(self, text="Registrar Tarea", command=self.save_task).pack(pady=10)
        
        # NUEVO: Botón para limpiar los campos de texto
        tk.Button(self, text="Limpiar Campos", command=self.clear_inputs).pack(pady=5)

        # Tabla (Treeview)
        self.tree = ttk.Treeview(self, columns=("ID", "Title", "Desc"), show="headings")
        self.tree.heading("ID", text="UUID")
        self.tree.heading("Title", text="Título")
        self.tree.heading("Desc", text="Descripción")
        
        self.tree.column("ID", width=100, anchor="center")
        self.tree.column("Title", width=150)
        self.tree.column("Desc", width=200)
        self.tree.pack(pady=10, fill="x", padx=10)

    def save_task(self):
        title = self.entry_title.get()
        desc = self.entry_desc.get()
        
        if title and desc:
            # Llama al servicio
            self._task_service.create_one_task(title, desc)
            
            # Limpia los campos automáticamente después de guardar
            self.clear_inputs()
            self.update_table()

    # NUEVO: Función para borrar el texto de los inputs
    def clear_inputs(self):
        self.entry_title.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)

    def update_table(self):
        # Limpiar la tabla antes de recargar
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Obtener datos desde el servicio
        tasks = self._task_service.get_all_task()
        for t in tasks:
            # Insertar en la tabla
            self.tree.insert("", "end", values=(str(t.id)[:8], t.title, t.description))
      