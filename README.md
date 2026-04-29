# DrawClassifier

## Real-time Doodle Recognition



A machine learning project inspired by Google's Quick Draw.

Draw on a canvas and get real-time predictions of what you're doing



---



## Features



- Interactive drawing canvas (Streamlit)

- Real-time predictions

- CNN model trained on doodle dataset



---



## How it works



1. User draws on canvas

2. Drawing is preprocessed into 28x28 grayscale image

3. Image is passed through a Convolutional Neural Network

4. Model outputs class probabilities using Softmax



---


## Project structure



```

DrawClassifier/

├── app/ # Streamlit app

├── src/

│ ├── data/ # data loading \& preprocessing

│ ├── model/ # CNN model

│ └── training/ # training pipeline

├── models/ # trained models (.pt)

├── requirements.txt

└── README.md

```



---



## Installation



```bash

git clone https://github.com/your-username/DrawClassifier.git

cd DrawClassifier

pip install -r requirements.txt

```



---



## Dataset



This project uses the Quick Draw dataset, download from:

https://quickdraw.withgoogle.com/data

Place files in:

data/raw/

Example:

data/raw/fully\_simplified\_bird.ndjson



---



## Run the app



```bash

streamlit run app/app.py

```



---



## Model



- Architecture: Convolutional Neural Network

- Input: 28x28 grayscale images

- Output: N classes (softmax probabilities)

- Loss: CrossEntropyLoss

- Optimizer: Adam



---



## Author

Guillermo Orellana Escobar

https://github.com/gOrellana05

