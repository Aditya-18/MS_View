from cx_Freeze import setup, Executable

base = None

executables = [Executable("ms_begin.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "MS_View",
    options = options,
    version = "1.0.0",
    description = 'A voice controlled assistant that can control your device according to your commands.',
    executables = executables
)