import tkinter as tk
from tkinter import simpledialog, messagebox


class TorresDeHanoi:
    def __init__(self, master, num_discos, torre_objetivo):
        self.master = master
        self.master.title("Torres de Hanoi")
        
        # Configuración inicial
        self.num_discos = num_discos
        self.torre_objetivo = torre_objetivo
        self.movimientos = 0
        self.movimientos_minimos = 2 ** num_discos - 1
        
        self.torres = [list(range(num_discos, 0, -1)), [], []]
        self.torre_origen = None
        
        # Configuración gráfica
        self.setup_gui()
        
    def setup_gui(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        
        # Lienzo para dibujar las torres
        self.canvas = tk.Canvas(self.master, width=600, height=400, bg="lightblue")
        self.canvas.pack(pady=20)
        
        # Botones de control
        self.frame_botones = tk.Frame(self.master)
        self.frame_botones.pack()
        
        self.botones_torres = [
            tk.Button(self.frame_botones, text=f"Torre {i+1}",
                      command=lambda idx=i: self.seleccionar_torre(idx),
                      width=12, bg="brown", fg="white")
            for i in range(3)
        ]
        for boton in self.botones_torres:
            boton.pack(side=tk.LEFT, padx=10)
        
        # Botón para reiniciar el juego
        self.boton_reset = tk.Button(self.master, text="Reiniciar Juego",
                                     command=self.resetear_juego, bg="red", fg="white", width=20)
        self.boton_reset.pack(pady=10)
        
        # Etiqueta de movimientos
        self.label_movimientos = tk.Label(self.master, text=f"Movimientos: 0", font=("Arial", 14))
        self.label_movimientos.pack(pady=10)
        
        # Etiqueta de torre objetivo
        self.label_objetivo = tk.Label(
            self.master,
            text=f"Torre objetivo: {self.torre_objetivo + 1}",
            font=("Arial", 14),
            fg="blue",
        )
        self.label_objetivo.pack(pady=10)
        
        self.dibujar_torres()
        
    def dibujar_torres(self):
        self.canvas.delete("all")
        colores = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'cyan']
        
        for i, torre in enumerate(self.torres):
            x_centro = 200 * (i + 1)
            self.canvas.create_rectangle(x_centro - 100, 350, x_centro + 100, 370, fill="brown")
            self.canvas.create_rectangle(x_centro - 10, 150, x_centro + 10, 350, fill="brown")
            
            for j, disco in enumerate(torre):
                ancho = 20 * disco
                color = colores[disco - 1]
                y = 350 - (j + 1) * 20
                self.canvas.create_rectangle(x_centro - ancho / 2, y, x_centro + ancho / 2, y + 20,
                                             fill=color, outline="black")
        
    def seleccionar_torre(self, idx):
        if self.torre_origen is None:  # Selección de torre de origen
            if not self.torres[idx]:
                messagebox.showwarning("Movimiento inválido", "La torre seleccionada está vacía.")
                return
            self.torre_origen = idx
            self.botones_torres[idx].config(bg="yellow")
        else:  # Selección de torre destino
            if self.torre_origen == idx:
                messagebox.showwarning("Movimiento inválido", "No puedes mover un disco a la misma torre.")
                self.botones_torres[self.torre_origen].config(bg="brown")
                self.torre_origen = None
                return
            
            if self.es_movimiento_valido(self.torre_origen, idx):
                disco = self.torres[self.torre_origen].pop()
                self.torres[idx].append(disco)
                self.movimientos += 1
                self.label_movimientos.config(text=f"Movimientos: {self.movimientos}")
                self.dibujar_torres()
                
                if len(self.torres[self.torre_objetivo]) == self.num_discos:
                    messagebox.showinfo(
                        "¡Victoria!",
                        f"¡Completaste el juego en {self.movimientos} movimientos! " +
                        f"(Mínimos: {self.movimientos_minimos})"
                    )
                    self.resetear_juego()
            else:
                messagebox.showerror("Movimiento inválido",
                                     "No puedes colocar un disco grande sobre uno más pequeño.")
            
            self.botones_torres[self.torre_origen].config(bg="brown")
            self.torre_origen = None
    
    def es_movimiento_valido(self, origen, destino):
        if not self.torres[origen]:
            return False
        if not self.torres[destino] or self.torres[origen][-1] < self.torres[destino][-1]:
            return True
        return False
    
    def resetear_juego(self):
        self.torres = [list(range(self.num_discos, 0, -1)), [], []]
        self.movimientos = 0
        self.label_movimientos.config(text=f"Movimientos: 0")
        self.torre_origen = None
        for boton in self.botones_torres:
            boton.config(bg="brown")
        self.dibujar_torres()


def iniciar_juego():
    root = tk.Tk()
    root.withdraw()
    num_discos = simpledialog.askinteger("Torres de Hanoi", "Número de discos (1-8):", minvalue=1, maxvalue=8)
    if num_discos:
        torre_objetivo = simpledialog.askinteger("Torres de Hanoi", "Selecciona torre objetivo (1-3):", minvalue=1, maxvalue=3) - 1
        root = tk.Tk()
        root.geometry("700x500")
        TorresDeHanoi(root, num_discos, torre_objetivo)
        root.mainloop()


if __name__ == "__main__":
    iniciar_juego()
