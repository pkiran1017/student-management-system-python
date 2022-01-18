import sys

from cx_Freeze import *

includefiles = ["profileicon.ico"]
excludes=[]
packages=[]
base = None

if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table = [
    ("DesktopShortcut",
     "DesktopFolder",
     "StudentManagementSystem",
     "TARGETDIR",
     "[TARGETDIR]\StudentManagementSystem.exe",

     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowOnd
     "TARGETDIR", #wdir
     )
]
msi_data = {"Shortcut": shortcut_table}

bdist_msi_options= {'data': msi_data}
setup(
       version="0.1",
       description="Student Management System Developed By Kiran Pandit",
       author="Kiran pandit",
       name="Student Management System",
       options={'build_exe': {'include_files': includefiles}, "bdist_msi": bdist_msi_options, },
       executables=[
          Executable(
              script="StudentManagementSystem.py",
              base=base,
              icon='profileicon.ico',
          )
      ]
)