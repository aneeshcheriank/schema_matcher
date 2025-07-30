import torch.nn.functional as F

def vector_similarity(x, y):
    x = F.normalize(x, p=2, dim=1)
    y = F.normalize(y, p=2, dim=1)
    similarity = F.cosine_similarity(x, y, dim=1)
    return similarity