# ⌨️ Typing Speed Analyzer

A simple Python-based **Typing Speed Test** that calculates **typing speed (WPM)** and **accuracy**.

The project is divided into two files to keep the **core logic** separate from the **program flow**.

## 📁 Project Structure

```text
Typing Speed Analyzer/
│
├── Core_Logic.py
├── main.py
└── README.md
```

## 🧠 Core Logic

### `Core_Logic.py`

Contains the main functions used by the typing speed analyzer.

#### 1. Random Paragraph

```python
get_random_paragraph()
```

Selects a random paragraph from the predefined list.

#### 2. Accuracy Calculation

```python
calculate_accuracy(target, typed)
```

Compares the target paragraph with the user's typed text character by character.

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

Combines the accuracy and WPM calculations to produce the final result.

---

## ▶️ Program Flow

### `main.py`

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

This project focuses on **Python logic, functions, timing, string processing, and modular code organization** without using a GUI.
