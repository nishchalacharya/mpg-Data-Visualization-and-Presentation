# mpg-Data-Visualization-and-Presentation
Exploratory Data Analysis (EDA) and visualization of the MPG  dataset using Matplotlib, Seaborn, and Plotly.


# 🚗 MPG Data Visualization and Analysis Dashboard

This project focuses on **exploratory data analysis (EDA)** and **interactive visualizations** of the classic **MPG (Miles Per Gallon)** dataset. The goal is to uncover meaningful patterns and relationships between various features of automobiles such as horsepower, weight, origin, cylinders, and fuel efficiency (mpg).

---

## 📊 Features

- 📌 **Univariate Analysis**: 
  - Histograms with KDE plots
  - Boxplots to detect outliers and distribution
  - Countplots for categorical columns like `cylinders`, `origin`, and `model_year`

- 🔁 **Bivariate & Multivariate Analysis**:  
  - Scatter plots between `horsepower`, `displacement`, `weight` vs `mpg`
  - Correlation heatmaps
  - Crosstabs (e.g., Cylinders vs Origin)
  - Pairplots to examine relationships among all numerical variables

- 💡 **Insights**:  
  - How fuel efficiency relates to engine characteristics and car weight  
  - Effect of `model_year` on MPG (temporal trends)
  - Multivariate visuals combining size and color for better interpretation

- 🌐 **Interactive Dashboard (Plotly)**:  
  - Recreated all key visualizations using **Plotly** for interactivity
  - Better exploration of high-dimensional relationships

---

## 📁 Files

| File | Description |
|------|-------------|
| `mpg.csv` | The dataset used (contains car attributes from 1970s-80s) |
| `datavisualisation.ipynb` | Jupyter notebook with all visualizations |
| `README.md` | This documentation |
| `main.py` | this contains code for plotly in Dash |


---

## 📌 Dataset Overview

The dataset contains the following features:

- `mpg` — miles per gallon (fuel efficiency)
- `cylinders` — number of engine cylinders
- `displacement`, `horsepower`, `weight`, `acceleration` — car specs
- `model_year` — year of manufacture
- `origin` — region (USA, Europe, Japan)

---

## 📉 Key Insights

- Cars with **lower weight and horsepower** tend to have **higher mpg**.
- **MPG increases** over the years, indicating improvements in fuel efficiency.
- Vehicles with **4 cylinders** dominate the dataset and show higher fuel efficiency.
- **Displacement, weight, and horsepower** are strongly positively correlated.
- Using multivariate visuals reveals that **lighter cars with fewer cylinders consistently offer better mileage**.

---

## 🛠️ Tech Stack

- **Python**
- **Seaborn & Matplotlib** – static data visualization
- **Plotly Express** – interactive dashboards
- **Pandas, NumPy** – data manipulation

---

## 🚀 How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/nishchalacharya/mpg-Data-Visualization-and-Presentation.git
   cd mpg-Data-Visualization-and-Presentation
