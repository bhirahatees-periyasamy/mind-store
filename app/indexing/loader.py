class Loader:
    def __init__(self):
        pass
    
    def load(self, path: str):
        print(f"Loading documents from: {path}")
        return [path]