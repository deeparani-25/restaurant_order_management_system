# Restaurant Order Management System

**PS No.: 31**  
**Project Title:** Restaurant Order Management System  
**Language:** Python 3

## 1. Project Description

This project is a console-based Restaurant Order Management System. It simulates the work of a waiter by allowing the user to:

- Select a restaurant table from **1 to 20**.
- View the restaurant menu.
- Add one or more food items to the selected table.
- View the running order.
- Generate the final bill.
- Calculate **10% service charge** and **5% GST**, both on the subtotal.
- Change the selected table during the program.

## 2. Menu

| Item | Price |
|---|---:|
| Burger | Rs. 100 |
| Pizza | Rs. 200 |
| Coffee | Rs. 50 |

## 3. Billing Formula

- **Subtotal** = Sum of `(item price × quantity)`
- **Service Charge** = Subtotal × 10%
- **GST** = Subtotal × 5%
- **Total** = Subtotal + Service Charge + GST

For example, for Coffee × 1:

- Subtotal = Rs. 50.00
- Service charge = Rs. 5.00
- GST = Rs. 2.50
- Total = Rs. 57.50

## 4. Data Structures Used

### Menu dictionary

The menu is stored in a dictionary:

```python
MENU = {
    "Burger": 100.0,
    "Pizza": 200.0,
    "Coffee": 50.0
}
```

This makes it easy to find the price of an ordered item.

### Table orders dictionary

Each table has its own list of orders:

```text
table number -> list of (item, quantity)
```

For example:

```text
3 -> [("Burger", 2), ("Pizza", 1), ("Coffee", 4)]
```

## 5. Main Features

1. **Table validation**  
   Only table numbers from 1 to 20 are accepted.

2. **Item validation**  
   Only Burger, Pizza, and Coffee can be ordered.

3. **Quantity validation**  
   Quantity must be a positive whole number.

4. **Multiple orders**  
   A loop allows the waiter to add multiple items for the same table.

5. **Running order**  
   The current items and subtotal can be viewed at any time.

6. **Final bill**  
   The program calculates subtotal, service charge, GST, and total.

7. **Multiple tables**  
   Orders are stored separately for all 20 tables.

## 6. How to Run

### Requirement

Python 3 must be installed on the computer.

### Command

Open Command Prompt/Terminal in the project folder and run:

```bash
python restaurant_order_management.py
```

If your system uses `python3`, run:

```bash
python3 restaurant_order_management.py
```

## 7. Program Menu

After starting, the program provides:

```text
1. View Menu
2. Add Order
3. View Running Order
4. Generate Final Bill
5. Change Table
6. Exit
```

## 8. Given Test Cases

### Test Case 1: Normal Input

**Input:**
- Table: 5
- Order item: Burger
- Quantity: 2

**Expected result:**

```text
Burger x2 added to Table 5 | Amount: 200
```

### Test Case 2: Boundary / Minimum Input

**Input:**
- Table: 1
- Order item: Coffee
- Quantity: 1
- Generate bill

**Expected result:**

```text
Subtotal:             50.00
Service charge (10%): 5.00
GST (5%):             2.50
Total:                57.50
```

### Test Case 3: Invalid Input

**Invalid item:**
```text
Order item: Pasta
Item not on the menu. Available: Burger, Pizza, Coffee
```

**Invalid quantity:**
```text
Quantity: abc
Invalid quantity. Enter a whole number.
```

**Invalid table:**
```text
Enter table number (1-20): 0
Invalid table number. Enter a number between 1 and 20.
```

### Test Case 4: Different Valid Scenario

**Input:**
- Table: 3
- Burger × 2
- Pizza × 1
- Coffee × 4
- Generate bill

**Expected calculation:**

```text
Burger x2 = 200
Pizza x1 = 200
Coffee x4 = 200
Subtotal = 600.00
Service charge (10%) = 60.00
GST (5%) = 30.00
Total = 690.00
```

## 9. Concepts Used

The project demonstrates the required Python concepts:

- Lists
- Dictionaries
- Tuples
- `for` loops
- `while` loops
- `if-elif-else`
- Functions
- Input/output
- Exception handling using `try-except`
- Validation
- Arithmetic and billing calculations

## 10. Project File

The main program is:

```text
restaurant_order_management.py
```

No external Python libraries are required.
