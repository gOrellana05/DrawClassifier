import torch
import torch.nn as nn
import torch.optim as optim

from src.models.cnn import DoodleCNN
from src.data.load_data import load_ndjson
from src.data.create_dataloader import create_dataloader
from src.data.labels import ID_TO_LABEL

def train():
    data = []

    files = ["full_simplified_bird.ndjson", "full_simplified_banana.ndjson", "full_simplified_cow.ndjson", "full_simplified_donut.ndjson","full_simplified_cactus.ndjson"]

    for f in files:
        data += load_ndjson(f)
        loader = create_dataloader(data, batch_size=32)
        
    model = DoodleCNN()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    for images, labels in loader:
        print(labels.unique())
        break
    epochs = 5
    for epoch in range(epochs):
        total_loss = 0
        for images, labels in loader:
            outputs = model(images)

            loss = criterion(outputs, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()

        print(f"Epcoh {epoch+1}, Loss: {total_loss:.4f}")
    from pathlib import Path

    MODEL_PATH = Path(__file__).resolve().parents[2] / "models" / "doodle_cnn.pt"

    torch.save(model.state_dict(), MODEL_PATH)

    print("Modelo guardado")

if __name__ == "__main__":
    train()
