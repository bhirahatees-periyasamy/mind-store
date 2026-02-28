from app.retrieval.retriever import Retriever
from app.indexing.index_pipeline import IndexPipeline


class VaultService:
    def __init__(self, retriever: Retriever, index_pipeline: IndexPipeline):
        self.retriever = retriever
        self.index_pipeline = index_pipeline
        
    def health(self):
        return True
        
    def search(self, query: str, k: int = 5):
        return self.retriever.retrieve(query, k)
    
    def index(self, path: str):
        return self.index_pipeline.index(path)