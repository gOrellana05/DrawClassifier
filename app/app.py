import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
import streamlit as st
import torch
import numpy as np
from PIL import Image

from streamlit_drawable_canvas import st_canvas
from src.models.cnn import DoodleCNN
from src.data.labels import ID_TO_LABEL

import torch.nn.functional as F


model = DoodleCNN(num_classes=len(ID_TO_LABEL))
model.load_state_dict(torch.load("models/doodle_cnn.pt"))

model.eval()
st.title("Draw Classifier")

canvas_result = st_canvas(
    fill_color="black",
    stroke_width=10,
    stroke_color="white",
    background_color="black",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas",
)

if canvas_result.image_data is not None:
    img = canvas_result.image_data

    img = Image.fromarray((img[:, :, 0]).astype(np.uint8))
    img = img.resize((28, 28))
    img = np.array(img) / 255.0
    img = torch.tensor(img).float().unsqueeze(0).unsqueeze(0)

    with torch.no_grad():
        outputs = model(img)
        probs = F.softmax(outputs, dim=1)

    top_probs, top_idxs = probs.topk(5)

    st.subheader("Predicciones:")

    for idx, prob in zip(top_idxs[0], top_probs[0]):
        label = ID_TO_LABEL[idx.item()]
        st.write(f"{label}: {prob.item() * 100:.2f}%")

