# Project: Use a Pre-trained Image Classifier to Identify Dog Breeds

This repository contains the implementation and report for a **Computer Vision Project** focused on identifying dog breeds using pre-trained image classifiers. The project aims to correctly identify whether pet images are of dogs (even if the breed is misclassified) and classify the breed of dog for images that are of dogs. Additionally, it evaluates three CNN architectures (`ResNet`, `AlexNet`, and `VGG`) to determine which one performs best while considering computational efficiency.

---

## 📚 Table of Contents

- [Project: Use a Pre-trained Image Classifier to Identify Dog Breeds](#project-use-a-pre-trained-image-classifier-to-identify-dog-breeds)
  - [📚 Table of Contents](#-table-of-contents)
  - [🌟 Overview](#-overview)
  - [📊 Dataset](#-dataset)
  - [🛠️ Implementation Details](#️-implementation-details)
    - [Key Steps in the Implementation](#key-steps-in-the-implementation)
  - [📁 Files in the Repository](#-files-in-the-repository)
    - [Main Files](#main-files)
    - [Data Files](#data-files)
    - [Helper Scripts](#helper-scripts)
    - [Output Files](#output-files)
  - [🚀 How to Run the Project](#-how-to-run-the-project)
    - [Prerequisites](#prerequisites)
    - [Steps to Run](#steps-to-run)
  - [📊 Results and Visualizations](#-results-and-visualizations)
  - [🤝 Contributions](#-contributions)
  - [📧 Contact](#-contact)
- [Thank you for checking out this project! 🚀](#thank-you-for-checking-out-this-project-)

---

## 🌟 Overview

The objective of this project is to:

1. **Identify Dogs vs. Non-Dogs**:
   - Use pre-trained image classifiers to determine whether pet images are of dogs or not.

2. **Classify Dog Breeds**:
   - For images identified as dogs, classify their breeds using the same classifiers.

3. **Compare CNN Architectures**:
   - Evaluate the performance of three CNN architectures (`ResNet`, `AlexNet`, and `VGG`) in achieving the above objectives.
   - Consider computational efficiency by measuring runtime for each model.

4. **Alternative Solutions**:
   - Assess whether simpler solutions could achieve "good enough" results within reasonable time constraints.

---

## 📊 Dataset

The dataset used in this project consists of:
- **`pet_images` folder**: Contains pet images (both dogs and non-dogs).
- **`dognames.txt`**: A text file listing valid dog breed names.
- **Pre-trained Models**: Utilizes pre-trained models (`ResNet`, `AlexNet`, and `VGG`) for classification.

---

## 🛠️ Implementation Details

The project is implemented using Python with the following libraries:
- **TensorFlow**: For loading and using pre-trained models.
- **NumPy**: For numerical operations.
- **Pandas**: For handling data structures.
- **Matplotlib**: For visualization (optional).

### Key Steps in the Implementation

1. **Time Your Program**:
   - Use the `time` module to measure the runtime of the program.

2. **Get User Inputs**:
   - Accept command-line arguments to specify input parameters.

3. **Create Pet Images Labels**:
   - Parse filenames from the `pet_images` folder to create labels for pet images.

4. **Create Classifier Labels**:
   - Use the `classifier.py` function to classify images and generate classifier labels.

5. **Compare Labels**:
   - Compare classifier labels with pet image labels to evaluate accuracy.

6. **Classify Labels as "Dogs" or "Not Dogs"**:
   - Use the `dognames.txt` file to classify labels as either "Dogs" or "Not Dogs."

7. **Calculate Results**:
   - Compute metrics such as accuracy, precision, recall, and F1-score for each model.

8. **Print Results**:
   - Display the results for each model, including classification accuracy and runtime.

---

## 📁 Files in the Repository

The repository contains the following files:

### Main Files
- **`check_images.py`**: The main Python script implementing the project logic.
- **`classifier.py`**: Functionality for classifying images using pre-trained models.
- **`print_results.py`**: Script for printing final results.

### Data Files
- **`pet_images/`**: Folder containing pet images.
- **`dognames.txt`**: Text file listing valid dog breed names.

### Helper Scripts
- **`calculates_results_stats.py`**: Functions for calculating statistics and metrics.
- **`create_pet_labels.py`**: Script for creating pet image labels.
- **`get_input_args.py`**: Script for parsing command-line arguments.
- **`run_models_batch.bat` / `run_models_batch.sh`**: Batch scripts for running multiple models.

### Output Files
- **Text Files**: Contain classification results for each model (e.g., `alexnet_pet-images.txt`, `resnet_pet-images.txt`, `vgg_pet-images.txt`).

---

## 🚀 How to Run the Project

### Prerequisites
- **Python**: Ensure Python is installed on your machine.
- **Libraries**: Install the required libraries using `pip`:
  ```bash
  pip install tensorflow numpy pandas matplotlib
  ```

### Steps to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/raghad-murad/DogBreedClassifier.git
   ```

2. **Navigate to the Directory**
   ```bash
   cd DogBreedClassifier
   ```

3. **Run the Main Script**
   ```bash
   python check_images.py
   ```

   Alternatively, you can use the batch scripts to run all models:
   ```bash
   # On Windows
   run_models_batch.bat

   # On Linux/Mac
   ./run_models_batch.sh
   ```

4. **View Results**
   - Classification results will be saved in text files (e.g., `alexnet_pet-images.txt`, `resnet_pet-images.txt`, `vgg_pet-images.txt`).
   - Runtime and accuracy metrics will be printed to the console.

---

## 📊 Results and Visualizations

The project generates various outputs, including:
- **Text Files**: Containing classification results for each model.
- **Console Output**: Showing runtime and accuracy metrics for each model.

Example visualizations include:
- Tables comparing accuracy, precision, recall, and F1-score across models.
- Bar charts showing runtime for each model.

---

## 🤝 Contributions

If you'd like to contribute to this repository, feel free to:
1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request with a detailed explanation of your changes.

---

## 📧 Contact

If you have any questions or suggestions, feel free to reach out!

- **Email:** raghadmbuzia@gmail.com
- **LinkedIn:** [in/raghad-murad](http://linkedin.com/in/raghad-murad-02690433a)

---

# Thank you for checking out this project! 🚀