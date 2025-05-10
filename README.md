

---

# 💻🔮 Laptop Price Prediction Using Machine Learning 🚀

---

## 🌟 Project Overview

Hello Tech Enthusiasts! 👋
I'm excited to share my new project – **Laptop Price Prediction**! 🖥️📈
This project aims to **predict the price** of a laptop based on its specifications using **Machine Learning**. By leveraging key features like RAM, Processor, GPU, and more, this model helps users estimate the right price range for a laptop! 🚀✨

🔗 **GitHub Repository**: [Laptop Price Prediction Repo 🔥](https://github.com/Anurag-raj03/Laptop-price-prediction)

🔗 **Kaggle Notebook**: [Laptop Price Prediction Notebook 📚](https://www.kaggle.com/code/anuragraj03/laptop-price-prediction)

---

## 🔥 Project Highlights

| 🔹 Features                | 🔹 Details                                                           |
| :------------------------- | :------------------------------------------------------------------- |
| **Framework**              | Python (Jupyter Notebook)                                            |
| **Libraries Used**         | `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `pickle` |
| **Model Used**             | Random Forest Regressor                                              |
| **UI/UX (Web App)**        | Developed using Streamlit                                            |
| **Techniques Implemented** | Feature Engineering, Outlier Removal, Data Preprocessing             |
| **Target Variable**        | Laptop Price (in Indian Rupees ₹)                                    |

---

## 🛠️ Technologies & Libraries Used

| 📚 Technology            | 🚀 Purpose                |
| :----------------------- | :------------------------ |
| **Python**               | Programming Language      |
| **Pandas**               | Data Manipulation         |
| **Numpy**                | Numerical Computation     |
| **Matplotlib & Seaborn** | Data Visualization 📊     |
| **Scikit-Learn**         | Machine Learning Modeling |
| **Pickle**               | Model Serialization       |
| **Streamlit**            | Web App Interface         |

---

## 🏗️ Project Workflow

### 📥 1. Data Collection

* Scraped data from various online laptop-selling websites.
* Dataset includes attributes like **Company**, **TypeName**, **RAM**, **Weight**, **Touchscreen**, **IPS Panel**, **Screen Size**, **Resolution**, **CPU**, **GPU**, **Operating System**, etc.

### 🛠️ 2. Data Preprocessing

* Handled **missing values**.
* Feature extraction from columns like `ScreenResolution`, `CPU`, and `GPU`.
* Created new features like:

  * `PPI (Pixel Per Inch)` from resolution and screen size.
  * `Touchscreen` and `IPS Panel` converted into binary features (0 or 1).

### 📈 3. Exploratory Data Analysis (EDA)

* Analyzed relationships between different features and laptop prices using **heatmaps**, **pairplots**, and **barplots**.
* Identified important factors like **Brand**, **Processor**, **RAM**, and **SSD** that influence laptop prices heavily.

### 🧠 4. Model Building

* Used **Random Forest Regressor** for price prediction.
* **Hyperparameter tuning** using `RandomizedSearchCV` to optimize model performance.
* Achieved **high R² score** showing excellent predictive capability.

### 🧪 5. Model Evaluation

* Evaluated model using metrics like:

  * **R² Score**
  * **Mean Absolute Error (MAE)**
* Model performs with **great accuracy** on unseen data!



## 📋 How to Run Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/Anurag-raj03/Laptop-price-prediction.git
   cd Laptop-price-prediction
   ```

2. **Install required libraries**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App**

   ```bash
   streamlit run app.py
   ```

4. 🎉 **Use the interface to predict laptop prices!**

---



## 📈 Key Visualizations

* 📊 Correlation heatmap to understand feature importance.
* 📈 Scatter plots showing relationships between price and features like RAM, SSD, and Company Brand.

---

## 🚀 Future Improvements

* Integrate **deep learning models** for even better accuracy.
* Expand dataset with more **global laptop brands**.
* Add **image-based feature extraction** (e.g., from laptop photos! 📷).
* Make the web app mobile-friendly 📱.

---

## 🤝 Let's Connect!

Would love to hear your thoughts and suggestions! 🚀✨

* 🔗 [LinkedIn Profile](https://www.linkedin.com/in/anurag-raj-770b6524a/)
* 🐙 [GitHub Profile](https://github.com/Anurag-raj03)
* 📊 [Kaggle Profile](https://www.kaggle.com/anuragraj03)

---

## 📌 Hashtags

\#LaptopPricePrediction #MachineLearning #RandomForest #Streamlit #Python #DataScience #ProjectShowcase #AI #ML #OpenSource #EDA #TechInnovation

---
