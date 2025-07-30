import torch

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
batch_size = 32


def encoder(model, sentences):
    return model.encode(
        sentences,
        batch_size=batch_size,
        show_progress_bar=True,
        normalize_embeddings=True,
        convert_to_tensor=True,
        device=DEVICE,
    )
