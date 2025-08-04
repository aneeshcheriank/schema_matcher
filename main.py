from sentence_transformers import SentenceTransformer
import pandas as pd
import json

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
    
    similar_question_dict = dict()
    for q in question1:
        for dis, idx in zip(distances[i], indices[i]):
            sim_questions = []
            if dis > 0.75:
                sim_questions.append(
                    (question2[idx], {'similarity': dis}))
            else:
                break 
        similar_question_dict[q] = sim_questions

    with open("./output/similar_questions.json", "w") as f:
        json.dump(similar_question_dict, f, indent=4)

