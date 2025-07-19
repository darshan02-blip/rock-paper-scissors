# rock-paper-scissors
Absolutely! A good `README.md` file helps others (and your future self) understand what your project does, how to use it, and how it's structured. Here’s a sample **GitHub README.md** you can use for your **Rock-Paper-Scissors AI Project (RPS Project)** with phases:

---

## 🧠 Rock-Paper-Scissors (RPS) - Hand Gesture Recognition with AI

This project uses **Computer Vision** and **Machine Learning** to recognize **hand gestures** (Rock, Paper, Scissors) and play the classic game in real-time using a webcam and AI.

---

### 📁 Project Structure (Phases)

| Phase       | Description                                                |
| ----------- | ---------------------------------------------------------- |
| **Phase 1** | Hand Gesture Dataset Collection using webcam               |
| **Phase 2** | Training an ML Model (like SVM or KNN) on collected images |
| **Phase 3** | Streamlit App for Gesture Classification                   |
| **Phase 4** | Play RPS Game against AI                                   |
| **Phase 5** | Real-time Prediction & Display using Webcam                |

---

### 🚀 How to Run

#### 1. Clone the Repository

```bash
git clone https://github.com/your-username/rock-paper-scissors-ai.git
cd rock-paper-scissors-ai
```

#### 2. Install Dependencies

Make sure Python is installed. Then install required packages:

```bash
pip install -r requirements.txt
```

If you don't have `streamlit`:

```bash
pip install streamlit
```

#### 3. Run a Phase

For example, to run Phase 4 (Game):

```bash
streamlit run phase4_rps_game.py
```

---

### 🎮 How It Works

* Uses **OpenCV** to capture hand gestures.
* ML model is trained using extracted hand gesture images.
* Streamlit provides a clean UI for interacting with the model.
* AI plays RPS with the user in real-time.

---

### 🛠 Technologies Used

* Python 🐍
* OpenCV 📷
* scikit-learn 🔍
* Streamlit 🌐
* NumPy, Pandas

---

### 📸 Screenshots

*Add images from the UI/game preview here if you want.*

---

### ✅ TODO

* [x] Dataset Collection
* [x] Model Training
* [x] Streamlit Classification App
* [x] RPS Game
* [x] Real-time Prediction
