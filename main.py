from torch.utils.data import DataLoader
from src.data.DoodleDataset import DoodleDataset
from src.data.load_data import load_ndjson
from src.data.create_dataloader import create_dataloader

def main():


    data = load_ndjson("full_simplified_bird.ndjson")
    loader = create_dataloader(data)

    for images, labels in loader:
        print(images.shape)
        print(labels.shape)
        break



if __name__ == "__main__":
    main()