import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import stat

def create_launcher(name, exec_path, icon_path=None, work_dir=None):
    desktop_dir = os.path.expanduser("~/Escritorio")
    if not os.path.exists(desktop_dir):
        desktop_dir = os.path.expanduser("~/Desktop")
    
    file_path = os.path.join(desktop_dir, f"{name.replace(' ', '_')}.desktop")
    
    content = [
        "[Desktop Entry]",
        "Version=1.0",
        f"Name={name}",
        f"Exec={exec_path}",
        "Terminal=false",
        "Type=Application",
        "Categories=Development;"
    ]
    
    if icon_path and icon_path.strip():
        content.append(f"Icon={os.path.abspath(icon_path)}")
    
    if work_dir and work_dir.strip():
        content.append(f"Path={os.path.abspath(work_dir)}")
    
    try:
        with open(file_path, "w") as f:
            f.write("\n".join(content))

        st = os.stat(file_path)
        os.chmod(file_path, st.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)

        # Mark as trusted (Allow Launching) automatically
        os.system(f'gio set -t string "{file_path}" metadata::trusted true')

        return True, file_path
    except Exception as e:
        return False, str(e)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Creador de Accesos Directos")
        self.root.geometry("500x450")
        self.root.configure(bg="#2d2d2d")
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TLabel", foreground="white", background="#2d2d2d", font=("Segoe UI", 10))
        style.configure("TButton", font=("Segoe UI", 10))
        
        container = tk.Frame(root, bg="#2d2d2d", padx=20, pady=20)
        container.pack(fill="both", expand=True)
        
        # Name
        ttk.Label(container, text="Nombre del Acceso Directo:").pack(anchor="w", pady=(0, 5))
        self.name_ent = ttk.Entry(container, width=50)
        self.name_ent.pack(fill="x", pady=(0, 15))
        
        # Command
        ttk.Label(container, text="Comando o Ruta del Ejecutable:").pack(anchor="w", pady=(0, 5))
        cmd_frame = tk.Frame(container, bg="#2d2d2d")
        cmd_frame.pack(fill="x", pady=(0, 15))
        self.cmd_ent = ttk.Entry(cmd_frame)
        self.cmd_ent.pack(side="left", fill="x", expand=True)
        ttk.Button(cmd_frame, text="...", width=3, command=self.browse_cmd).pack(side="right", padx=(5, 0))
        
        # Icon
        ttk.Label(container, text="Ruta del Icono (Opcional):").pack(anchor="w", pady=(0, 5))
        icon_frame = tk.Frame(container, bg="#2d2d2d")
        icon_frame.pack(fill="x", pady=(0, 15))
        self.icon_ent = ttk.Entry(icon_frame)
        self.icon_ent.pack(side="left", fill="x", expand=True)
        ttk.Button(icon_frame, text="...", width=3, command=self.browse_icon).pack(side="right", padx=(5, 0))
        
        # Work Dir
        ttk.Label(container, text="Directorio de Trabajo (Opcional):").pack(anchor="w", pady=(0, 5))
        dir_frame = tk.Frame(container, bg="#2d2d2d")
        dir_frame.pack(fill="x", pady=(0, 20))
        self.dir_ent = ttk.Entry(dir_frame)
        self.dir_ent.pack(side="left", fill="x", expand=True)
        ttk.Button(dir_frame, text="...", width=3, command=self.browse_dir).pack(side="right", padx=(5, 0))
        
        # Create Button
        self.create_btn = tk.Button(container, text="CREAR ACCESO DIRECTO", 
                                   bg="#0078d4", fg="white", font=("Segoe UI", 11, "bold"),
                                   relief="flat", pady=10, command=self.on_create)
        self.create_btn.pack(fill="x")

    def browse_cmd(self):
        path = filedialog.askopenfilename()
        if path: self.cmd_ent.delete(0, tk.END); self.cmd_ent.insert(0, path)
        
    def browse_icon(self):
        path = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png *.ico *.svg *.jpg")])
        if path: self.icon_ent.delete(0, tk.END); self.icon_ent.insert(0, path)
        
    def browse_dir(self):
        path = filedialog.askdirectory()
        if path: self.dir_ent.delete(0, tk.END); self.dir_ent.insert(0, path)

    def on_create(self):
        name = self.name_ent.get()
        cmd = self.cmd_ent.get()
        icon = self.icon_ent.get()
        wdir = self.dir_ent.get()
        
        if not name or not cmd:
            messagebox.showerror("Error", "Nombre y Comando son obligatorios.")
            return
            
        success, res = create_launcher(name, cmd, icon, wdir)
        if success:
            messagebox.showinfo("Éxito", f"Acceso directo creado en el Escritorio:\n{res}\n\nNo olvides darle a 'Permitir lanzar' al abrirlo por primera vez.")
        else:
            messagebox.showerror("Error", f"No se pudo crear: {res}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
