# ⌨️ Typing Speed Analyzer

A simple Python-based **Typing Speed Test** that calculates **typing speed (WPM)** and **accuracy**.

The project is divided into two files to keep the logic separate from the program flow.

## 📁 Project Structure

```text
Typing Speed Test/
│
├── Core_Logic.py
└── main.py
```

## 🧠 Core Logic

### `Core_Logic.py`

This file contains the main functionality of the typing test.

#### 1. Random Paragraph

```python
get_random_paragraph()
```

Selects a random paragraph from the predefined paragraph list.

#### 2. Accuracy Calculation

```python
calculate_accuracy(target, typed)
```

Compares the user's typed text with the original paragraph character by character.

**Formula:**

```text
Accuracy = (Correct Characters / Typed Characters) × 100
```

#### 3. WPM Calculation

```python
calculate_wpm(typed, elapsed_time)
```

Calculates **Words Per Minute (WPM)** based on the number of words typed and the time taken.

**Formula:**

```text
WPM = (Words Typed / Time in Seconds) × 60
```

#### 4. Result Calculation

```python
calculate_result(target, typed, elapsed_time)
```

Combines the accuracy and WPM calculations and returns the final result.

---

## ▶️ Program Flow

### `main.py`

The program follows these steps:

```text
Start
  ↓
Select Random Paragraph
  ↓
Display Paragraph
  ↓
Start Timer
  ↓
User Types Paragraph
  ↓
Stop Timer
  ↓
Calculate Accuracy
  ↓
Calculate WPM
  ↓
Display Result
```

## 🛠️ Technologies Used

* Python
* `random`
* `time`

## 🎯 Concepts Practiced

* Functions
* Lists
* Loops
* String manipulation
* `random.choice()`
* Time calculation
* Modular programming
* Importing functions between Python files

## 🚀 Run the Project

```bash
python main.py
```

This project focuses on understanding **Python logic, functions, timing, and modular code organization** without using a GUI.
