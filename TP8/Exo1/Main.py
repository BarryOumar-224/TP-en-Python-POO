from pathlib import Path
from contextlib import contextmanager, ExitStack
import os

class TempFileWriter:
    def __enter__(self):
        self.filepath = Path("temp_class.txt")
        self.f = self.filepath.open("w")
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
        if self.filepath.exists():
            self.filepath.unlink()

@contextmanager
def temp_file():
    path = Path("temp_gen.txt")
    f = path.open("w")
    try:
        yield f
    finally:
        f.close()
        if path.exists():
            path.unlink()

if __name__ == "__main__":
    print("Debut Partie 1")
    with TempFileWriter() as f:
        f.write("Contenu temporaire\n")
    print("Fin Partie 1")

    print("Debut Partie 2")
    with temp_file() as f:
        f.write("Autre test\n")
    print("Fin Partie 2")

    print("Debut Partie 3")
    paths = ["a.txt", "b.txt", "c.txt"]
    with ExitStack() as stack:
        files = [stack.enter_context(open(p, "w")) for p in paths]
        for f in files:
            f.write("test\n")
    print("Fin Partie 3")

    for p in paths:
        if os.path.exists(p):
            os.remove(p)
    print("Nettoyage termine")