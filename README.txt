# Simple Bubble Sort App

A Python app to visualize the Bubble Sort algorithm using Gradio.

## How to Run
1. Install: `pip install -r requirements.txt`
2. Run: `python app.py`

## Computational Thinking Plan

### 1. Decomposition
I split the project into three parts:
* **Input:** Getting numbers from a text box.
* **Logic:** The double loop to compare and swap numbers.
* **Output:** Showing the sorted list and the history of swaps.

### 2. Pattern Recognition
The main pattern is **comparing neighbors**: `if nums[j] > nums[j+1]`, we swap them. This repeats until the list is sorted.

### 3. Abstraction
I hide the complex code (loops and indices) and only show the user the **list changes**

### 4. Algorithm Design
Flow: `User Input` -> `Check Errors` -> `Loop & Swap` -> `Update UI`.

![Flowchart](flowchart.png)

## Testing
* **Test:** `5, 1, 3` -> Result: `1, 3, 5` (Working)
* **Test:** `a, b, c` -> Result: `Error message` (Handled)

## Links
* **GitHub:** [Your GitHub Link]
* **Hugging Face:** [Your Hugging Face Link]