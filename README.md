# Edunet_Internship_capstone_project

# Eco-Scan AI – Smart Waste Detection and Recycling Assistant

## Project Overview

Eco-Scan AI is an AI-powered waste detection and recycling assistant developed as part of the **Edunet Foundation – GTU Internship Program** under the **Green Skills and Sustainability** domain.

The application allows users to upload an image of a waste item. Using **Artificial Intelligence (AI)** and **Computer Vision**, the system identifies the waste type, classifies it into the correct category, and provides recycling guidance and disposal recommendations to promote sustainable waste management.

---

## Project Objectives

- Detect waste items from uploaded images.
- Classify waste into different categories.
- Suggest the correct disposal or recycling bin.
- Provide recycling tips and environmental awareness.
- Encourage responsible waste disposal using AI.

---

## Waste Categories

The model can identify the following waste classes:

-  Battery
-  Biological (Organic)
-  Cardboard
-  Clothes
-  Green Glass
-  White Glass
-  Brown Glass
-  Paper
-  Plastic
-  Shoes
-  Metal
-  Trash

---

## Technologies Used

- Python
- TensorFlow / Keras
- Streamlit

---

## Project Structure

```text
Eco-Scan-AI/
│
├── app.py                 # Streamlit application
├── train_model.py         # Model training script
├── utils.py               # Recycling information
├── requirements.txt       # Required Python libraries
├── README.md
```

---

## Working Process

1. Upload an image of a waste item.
2. The image is preprocessed and resized.
3. The CNN model predicts the waste type.
4. The application displays:
   - Waste Type
   - Waste Category
   - Recommended Disposal Bin
   - Recycling Tip
   - Prediction Confidence

---

## Sustainability Impact

Eco-Scan AI contributes to environmental sustainability by:

- Promoting proper waste segregation
- Encouraging recycling
- Reducing landfill waste
- Increasing public awareness of responsible waste disposal
- Supporting Green Skills initiatives

---

## Model Information

- Model Type: Convolutional Neural Network (CNN)
- Image Size: 128 × 128
- Optimizer: Adam
- Loss Function: Categorical Crossentropy
- Framework: TensorFlow / Keras

---

## Features

- Upload waste images
- Recycling bin recommendation
- Recycling tips
- Confidence score display
- Simple and user-friendly Streamlit interface

## Team Members

- Pandya Rishi Kanaiyalal
- Parmar Kuldeepkumaar Pravinbhai
- 
---

## Internship Details

**Internship Program:** Edunet Foundation – GTU Internship Program

**Project Domain:** Artificial Intelligence | Computer Vision | Green Skills | Sustainability

---

## License

This project is developed for educational and academic purposes under the Edunet Foundation Internship Program.

---

We sincerely thank **Edunet Foundation**, **GTU (Gujarat Technological University)**, and our mentors for providing the opportunity and guidance to develop this project on Green Skills and Sustainability.
