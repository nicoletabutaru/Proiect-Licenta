from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from core.config_loader import CONFIG

class Retriever:
  
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        
        self.topics = CONFIG["topics"]
        self.topic_embeddings = self.model.encode(self.topics, convert_to_numpy=True)

    def get_topic(self, question):
        q_emb = self.model.encode([question], convert_to_numpy=True)
        sims = cosine_similarity(q_emb, self.topic_embeddings)[0]
        top_idx = np.argmax(sims)
        return self.topics[top_idx]