from sentence_transformers import SentenceTransformer
import pandas as pd
import os

from src.encoder import encoder
from src.matcher import search
import src.config as config

data_path = os.path.join(config.DATA_FOLDER, "train.csv")
model_path = "./models/output/sbert-finetuned-model"

if __name__ == "__main__":

    model = SentenceTransformer(model_path)
    df = pd.read_csv(data_path, engine="python")

    question1 = df["question1"].tolist()
    question2 = df["question2"].tolist()


    question1_embeddings = encoder(model, question1)
    question2_embeddings = encoder(model, question2)

    distances, indices = search(
        question1_embeddings, 
        question2_embeddings, 
        k=5
    )



