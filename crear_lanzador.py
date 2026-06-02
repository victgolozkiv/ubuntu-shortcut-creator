import os
import sys
import stat
import shutil

def create_launcher(name, exec_path, icon_path=None, work_dir=None):
    desktop_dir = os.path.expanduser("~/Escritorio")
    if not os.path.exists(desktop_dir):
        desktop_dir = os.path.expanduser("~/Desktop")
    
    # Use the name provided by the user for the filename, but safe for Linux
    safe_name = name.replace(" ", "_")
    file_name = f"{safe_name}.desktop"
    file_path = os.path.join(desktop_dir, file_name)
    
    # FIX: If it's a python script, we MUST prepend 'python3 '
    final_exec = exec_path
    if exec_path.endswith(".py"):
        # Ensure we have the absolute path for the script
        abs_script = os.path.abspath(os.path.expanduser(exec_path))
        final_exec = f"python3 {abs_script}"
    
    content = [
        "[Desktop Entry]",
        "Version=1.0",
        "Type=Application",
        f"Name={name}",
        f"Exec={final_exec}",
        "Terminal=false",
        "Categories=Development;"
    ]
    
    if icon_path and icon_path.strip():
        content.append(f"Icon={os.path.abspath(os.path.expanduser(icon_path))}")
    
    if work_dir and work_dir.strip():
        content.append(f"Path={os.path.abspath(os.path.expanduser(work_dir))}")
    
    try:
        # 1. Write file
        with open(file_path, "w") as f:
            f.write("\n".join(content))
        
        # 2. Permissions
        st = os.stat(file_path)
        os.chmod(file_path, st.st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)
        
        # 3. Trust via GIO (The magic command for Ubuntu)
        os.system(f'gio set -t string "{file_path}" metadata::trusted true')
        
        # 4. Copy to local apps so the system "registers" it
        apps_dir = os.path.expanduser("~/.local/share/applications")
        if os.path.exists(apps_dir):
            shutil.copy(file_path, os.path.join(apps_dir, file_name))
        
        print(f"Acceso directo creado correctamente: {file_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python3 crear_lanzador.py 'Nombre' 'Comando' ['Icono'] ['Directorio']")
    else:
        create_launcher(sys.argv[1], sys.argv[2], 
                        sys.argv[3] if len(sys.argv) > 3 else None,
                        sys.argv[4] if len(sys.argv) > 4 else None)
