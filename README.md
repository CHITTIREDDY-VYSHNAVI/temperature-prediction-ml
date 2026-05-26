# 🌦️ Temperature Prediction using Machine Learning

A Machine Learning-based web application that predicts temperature using environmental parameters such as humidity, wind speed, and atmospheric pressure.

The project uses a **Random Forest Regression** model trained on historical weather data and integrates the **OpenWeatherMap API** for fetching real-time weather information. The application is deployed using **Streamlit** for an interactive user experience.

---

## 🚀 Features

* Real-time temperature prediction
* Uses Machine Learning (Random Forest Regression)
* Fetches live weather data using API
* Interactive Streamlit web interface
* Simple and lightweight implementation
* Actual vs Predicted temperature visualization

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Requests
* OpenWeatherMap API

---

## 📂 Project Structure

```bash
temperature-prediction-ml/
│
├── app.py
├── model.pkl
├── requirements.txt
└── README.md
```

---

## ⚙️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 🌐 Live Demo

Deployment Link:
[https://temperature-prediction-ml-bhjwitwr4qznz2uw86hhj.streamlit.app/](https://temperature-prediction-ml-bhjwitwr4qznz2uw86hhj.streamlit.app/)

---

## 📊 Machine Learning Model

### Model Used:

* Random Forest Regressor

### Input Features:

* Humidity
* Wind Speed
* Pressure
* Month
* Day

### Evaluation Metrics:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)

---

## 🔄 Workflow

1. User enters city name
2. API fetches live weather data
3. Weather features are extracted
4. Data is passed to ML model
5. Temperature prediction is generated
6. Output displayed on Streamlit interface

---

## 📈 Future Improvements

* Add hourly and weekly forecasting
* Integrate advanced ML/DL models
* Add graphical dashboards
* Auto-detect user location
* Support multiple weather APIs

---

## 👨‍💻 Author

**Vyshnavi Reddy Chittireddy**
