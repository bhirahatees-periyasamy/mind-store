class Retriever:
    
    def __init__(self, embedder, vector_store):
        self.embedder = embedder
        self.vector_store = vector_store
        
    def retrieve(self, query: str, k: int = 5):
        print(f"Retrieving for query: {query}")
        print(f"K: {k}")
        return [
            {
                "content": "dummy snippet",
                "path": "src/auth.rs",
                "score": 0.91
            }
        ]