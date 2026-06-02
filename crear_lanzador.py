import os
import sys
import stat
import shutil

def create_launcher(name, exec_path, icon_path=None, work_dir=None):
    desktop_dir = os.path.expanduser("~/Escritorio")
    if not os.path.exists(desktop_dir):
        desktop_dir = os.path.expanduser("~/Desktop")
    
    file_name = f"{name.replace(' ', '_')}.desktop"
    file_path = os.path.join(desktop_dir, file_name)
    
    # Simple content generation to avoid path errors
    content = [
        "[Desktop Entry]",
        "Version=1.0",
        "Type=Application",
        f"Name={name}",
        f"Exec={exec_path}",
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
        
        # 3. Trust via GIO
        os.system(f'gio set -t string "{file_path}" metadata::trusted true')
        
        # 4. Copy to local apps
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
