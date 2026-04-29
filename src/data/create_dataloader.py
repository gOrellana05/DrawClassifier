from torch.utils.data import DataLoader
from src.data.DoodleDataset import DoodleDataset

def create_dataloader(data, batch_size=32, shuffle=True):
    dataset = DoodleDataset(data)

    loader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle
    )

    return loader