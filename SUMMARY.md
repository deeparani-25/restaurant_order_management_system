# Project Summary

## Restaurant Order Management System

**PS No.: 31**  
**Language:** Python 3

### Objective

The objective of this project is to create a console-based restaurant ordering system in which a waiter can select a table, take orders, view the running order, and generate a final bill.

### Menu

- Burger — Rs. 100
- Pizza — Rs. 200
- Coffee — Rs. 50

### Billing

The program calculates:

- Subtotal
- 10% service charge on the subtotal
- 5% GST on the subtotal
- Final total

Formula:

```text
Service Charge = Subtotal × 10%
GST            = Subtotal × 5%
Total          = Subtotal + Service Charge + GST
```

### Data Structures

The menu is stored in a **dictionary** containing item names and prices.

Orders are stored separately for each table using a **dictionary of lists**. Each order entry contains the item name and quantity.

### Program Flow

```text
Start
  ↓
Select Table (1–20)
  ↓
Display Main Menu
  ↓
Add Order / View Running Order / Generate Bill / Change Table
  ↓
Validate Input
  ↓
Calculate Subtotal
  ↓
Add 10% Service Charge
  ↓
Add 5% GST
  ↓
Display Final Bill
  ↓
Exit
```

### Validation

The program validates:

1. Table number must be between 1 and 20.
2. Item must be Burger, Pizza, or Coffee.
3. Quantity must be a positive whole number.
4. Invalid menu items, quantities, table numbers, and menu choices show appropriate error messages.

### Test Case Results

| Test Case | Scenario | Result |
|---|---|---|
| 1 | Burger × 2 at Table 5 | Amount = Rs. 200 |
| 2 | Coffee × 1 at Table 1 | Total = Rs. 57.50 |
| 3 | Pasta / `abc` quantity / Table 0 | Invalid inputs are rejected |
| 4 | Burger × 2, Pizza × 1, Coffee × 4 | Total = Rs. 690.00 |

### Requirements Satisfied

- Python 3 console application
- Menu stored in a dictionary
- Orders stored in lists for each table
- Loop for multiple items
- Running order display
- Subtotal, service charge, GST and total calculation
- Validation of table number, item name and quantity
- Given test cases supported

### Conclusion

The project successfully implements a simple Restaurant Order Management System using basic Python programming concepts. It provides separate order storage for tables 1–20, validates user input, supports multiple items, and generates the final bill according to the specified 10% service charge and 5% GST rules.
