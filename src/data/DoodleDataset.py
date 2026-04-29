from torch.utils.data import Dataset
from src.data.preprocess import drawing_to_image
import torchvision.transforms as T
from src.data.labels import LABEL_MAP


class DoodleDataset(Dataset):

    def __init__(self, data):
        self.data = data
        self.label_map = LABEL_MAP

        self.transform = T.Compose([
            T.ToTensor()
        ])

    def __len__(self):
        return len(self.data)

    def __getitem__(self,idx):
        item = self.data[idx]
        img = drawing_to_image(item["drawing"])
        img = self.transform(img)
        label = LABEL_MAP[item["word"]]
        return img, label
