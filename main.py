from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModel
from sentence_transformers import SentenceTransformer, util
import torch


def compute_similarity(sentence1, sentence2):
    # Encode the sentences
    embeddings1 = model.encode(sentence1, convert_to_tensor=True)
    embeddings2 = model.encode(sentence2, convert_to_tensor=True)

    # Compute cosine similarity
    similarity = util.pytorch_cos_sim(embeddings1, embeddings2).item()

    return similarity

if __name__ == '__main__':
    model = SentenceTransformer('sentence-transformers/paraphrase-xlm-r-multilingual-v1')

    s1 = "I like ice-cream"
    s2 = "Tôi thích ăn kem"
    s3 = "Tôi ghét ăn kem"

    print(compute_similarity(s1,s3))