import torch.nn.functional as F
from .encoder import encoder
from faiss import IndexFlatIP, norlalize_L2


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


def search(encoded1, encoded2, k=5):
    norlalize_L2(encoded1)
    norlalize_L2(encoded2)

    index = IndexFlatIP(encoded1.shape[1])
    index.add(encoded1.cpu().numpy())
    distances, indices = index.search(encoded2.cpu().numpy(), k)
    return distances, indices
