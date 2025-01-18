# Penguin Species Classification - Algorithm Comparison

## Overview

The **Penguin Species Classification** project explores the effectiveness of different Machine Learning algorithms (KNN, Decision Tree, Random Forest) in classifying penguin species based on their physical attributes. The project emphasizes model comparison to identify the most accurate and efficient approach.

## Features

- **Dataset**: Utilizes the Palmer Penguins dataset for classification tasks.
  
- **Algorithms Compared**:
  - K-Nearest Neighbors (KNN)
  - Decision Tree (DT)
  - Random Forest Classifier (RFC)
    
- **Evaluation Metrics**: Assesses algorithm performance using accuracy, precision, recall, and F1 score.
  
- **Visualization**: Graphical representation of results for better insight.

## Technologies Used

- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Scikit-learn, Matplotlib

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/ankita34359/Machine-Learning-Penguin-Model-Comparing-Algorithms-KNN-DT-RFC.git
   cd Machine-Learning-Penguin-Model-Comparing-Algorithms-KNN-DT-RFC
   ```

2. **Set Up Virtual Environment** (optional)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Project**
   Execute the Python script to train and evaluate models:
   ```bash
   python penguin_model_comparison.py
   ```

## Dataset

The project uses the **Palmer Penguins** dataset, which includes the following features:

- Culmen Length (mm)
- Culmen Depth (mm)
- Flipper Length (mm)
- Body Mass (g)
- Species (Adelie, Chinstrap, Gentoo)

The dataset can be obtained from [Kaggle](https://www.kaggle.com/datasets).

## How It Works

1. Preprocesses the dataset to handle missing values and encode categorical data.
2. Splits the data into training and testing sets.
3. Trains three different algorithms (KNN, Decision Tree, Random Forest) on the data.
4. Evaluates models using metrics and compares their performance.
5. Visualizes the results for better understanding.

## Results

- Detailed evaluation of each algorithm's performance.
- Insights into which model performs best for the given dataset.

## Contributing

Contributions are welcome! Fork the repository, create a new branch, and submit a pull request to suggest improvements or add features.

## License

This project is licensed under the [MIT License](LICENSE).

---

Exploring Machine Learning algorithms for effective classification! 🚀
