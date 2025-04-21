# 🌸 IRIS Detection using K-Nearest Neighbors (K-NN)

This project demonstrates how to implement the **K-Nearest Neighbors (K-NN)** algorithm **from scratch** using the famous **Iris dataset**.  
It is designed for beginners who want to understand the core logic behind one of the simplest machine learning algorithms — without using any ML libraries like scikit-learn.

Full Explication on Medium : 

## 📊 Dataset
- **Name**: Iris Flower Dataset  
- **Source**: [UCI Machine Learning Repository](https://www.kaggle.com/datasets/himanshunakrani/iris-dataset)  
- **Samples**: 150 flowers  
- **Features**: 4 numerical features + 1 target (`Species`)  
  - SepalLengthCm  
  - SepalWidthCm  
  - PetalLengthCm  
  - PetalWidthCm  
- **Classes**:  
  - *Iris-setosa*  
  - *Iris-versicolor*  
  - *Iris-virginica*

## 📁 Files
- `KNN.py` – contains the full implementation
- `Iris.csv` – dataset used for training
- `README.md` – this file

## 🧠 Why from Scratch?

Building machine learning models from scratch helps understand how things work under the hood — including how distances are calculated, how predictions are made, and how each component influences the final result.  
It’s a great way to build strong intuition before using advanced libraries like `scikit-learn`.

---

## ✅ Requirements

- Python 3.x  
- pandas  
- matplotlib (for plotting optional visuals like loss curves or distance graphs)

Install the required libraries with:

```bash
pip install pandas matplotlib
