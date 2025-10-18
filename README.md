Artificial Pancreas System — Unit Testing with Pytest  

----

This project models a simplified **Artificial Pancreas System**  developed using Object oriented Programming (OOP) concept and demonstrates **unit testing** using **pytest**.
  
It focuses on verifying glucose regulation, insulin delivery, and system stability under various physiological events.

---

## Project Overview

The Artificial Pancreas simulation tracks glucose levels and insulin delivery in response to activities such as meals and exercise.  
The goal is to ensure the system reacts correctly to varying glucose levels through automated tests that cover all realistic scenarios.

---
## Key terminology
1. Unit test involves testing individual units or components of a software to ensure they work as expected.
2. Pytest is a popular testing framework for Python that makes it easy to write simple and scalable test cases. It supports fixtures, parameterized testing, and a rich plugin architecture.
3. OOP is a fundamental concept that allows creating classes and objects to model real-world entities and their interactions. 

---
## Core Functionalities

| Functionality  | Description |
|----------------|-------------|
| **Meal Event** | Increases glucose level after carbohydrate intake. |
| **Exercise Event** | Decreases glucose level based on exercise intensity or duration. |
| **Insulin Delivery** | Automatically delivers insulin when glucose exceeds the target range. |
| **Safety Mechanisms** | Prevents glucose from dropping below a defined minimum threshold. |
| **Cumulative Tracking** | Tracks the total amount of insulin delivered over time. |

---

## Testing Strategy

This project uses **pytest** to verify system behavior across multiple physiological and edge-case scenarios.

---

### Test Cases Summary

| Test | Description |
|------|--------------|
**Glucose increases after a meal**  Feed the system a meal and verify if the glucose_level rises. 
 **Glucose decreases after exercise**  Simulate exercise and ensure glucose_level drops. |
| **Correct action is returned** | 
- High glucose → "deliver_insulin"
- Low glucose → "warn_low_glucose"
- Normal range → "maintain"  


**Glucose never drops below minimum** After long exercise, ensure glucose_level is not below 50 mg/dL 


**Total insulin tracking** Verify total_insulin_delivered increments when insulin is delivered. 

**Multiple sequential events** Simulate sequence: `meal → exercise → insulin → maintain` to confirm correct state transitions. 

**Invalid input handling** Ensure ValueError is raised for invalid inputs (e.g., negative carbs or negative exercise duration). 

---

##  Example Pytest Patterns

### Using Fixtures
Fixtures set up reusable test environments:
```python

import pytest

import main.artificial_pancreas as art_pan_syst

@pytest.fixture
def art_pan_sys():
   
   return [art_pan_syst.ArtificialPancreasSystem(glucose_level, 1.0, 100, 10) for glucose_level in [100, 80, 130, 95, 50]]
```

### Using Parameterization
Test multiple glucose states efficiently:
```python
@pytest.mark.parametrize("art_sys_index,  expected_action", [
  (2, "deliver_insulin"), 
  (1, "warn_low_glucose"),
  (3, "maintain")
])
def test_correct_action(art_pan_sys, art_sys_index, expected_action):
  art_pan_syst_obj = art_pan_sys[art_sys_index]
  assert art_pan_syst_obj.predict_action()[0] == expected_action , f'Should be {expected_action}'
```

### Testing Exceptions
Validate error handling for invalid inputs:
```python
def test_invalid_input_meal(art_pan_sys):
  with pytest.raises(TypeError):
    art_pan_sys[0].meal('hello')
```

---

## Key Concepts Demonstrated

- **Fixtures** – reusable objects for setting up system state  
- **Parameterization** – running multiple test inputs efficiently  
- **Exception Testing** – ensuring the system safely handles invalid input  
- **Sequential Testing** – simulating time-ordered physiological events  
- **Assertions** – verifying expected outcomes for every action  

---

## Requirement.txt

- **Python 3.10+**
- **pytest 8.4.2**  
- **pluggy 1.6.0**  

Install dependencies:
```bash
pip install pytest  
```

Run tests:
```bash
python -m pytest -v
```

