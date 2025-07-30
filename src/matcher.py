import torch.nn.functional as F
from .encoder import encoder


def vector_similarity(x, y):
    x = F.normalize(x, p=2, dim=1)
    y = F.normalize(y, p=2, dim=1)
    similarity = F.cosine_similarity(x, y, dim=1)
    return similarity


def calculate_similarity(model, sentence_1, sentence_2):
    encoded_1 = encoder(model, sentence_1)
    encoded_2 = encoder(model, sentence_2)
    similarity_scores = vector_similarity(encoded_1, encoded_2)
    return similarity_scores.tolist()
