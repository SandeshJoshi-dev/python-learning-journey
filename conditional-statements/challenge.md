
# Python Challenge #36 — Hotel Booking & Discount System 🏨

**Topic:** Nested Conditional Statements (`if`, `elif`, `else`)

**Difficulty:** Intermediate Beginner (6/10)

## Problem Statement

You are a junior Python developer working for a hotel in Pokhara, Nepal.

The hotel wants a Python program that checks room availability, validates the booking duration, and calculates the final bill after applying discounts based on membership status and the number of nights booked.

## Given Information

```python
room_available = True
nights = 3
price_per_night = 2500
is_member = True
```

## Discount Policy

| Condition | Discount |
|---|---|
| Member staying 3 or more nights | 15% |
| Non-member staying 3 or more nights | 10% |
| Any guest staying fewer than 3 nights | 0% |

Discounts apply only to valid bookings.

## Programming Requirements

**Task 1 — Validate the Booking**

- Check whether a room is available.
- Check whether the number of nights is greater than zero.
- If either condition fails, display `"Booking Unavailable or Invalid Nights"`.

**Task 2 — Calculate the Original Price**

- Multiply the number of nights by the price per night.
- Store the result in `total_price`.

**Task 3 — Apply the Discount**

- Use nested `if`, `elif`, and `else` statements.
- Determine the discount according to the hotel's policy.
- Store the selected percentage in `discount_rate`.

**Task 4 — Calculate the Final Bill**

- Calculate the discount amount.
- Subtract the discount amount from the original price.
- Display the original price, discount rate, discount amount, and final bill.
- Do not calculate a bill if the booking is invalid.

## Expected Output

For a member staying 3 nights at Rs. 2,500 per night:

```text
Rooms Available
Original Price: 7500
Discount Rate: 15%
Discount Amount: 1125.0
Final Bill: 6375.0
```

## Test Cases

| Scenario | Expected Result |
|---|---|
| Member, 3 nights | 15% discount |
| Non-member, 3 nights | 10% discount |
| Member, 2 nights | No discount |
| Room unavailable | Booking rejected |
| Zero or negative nights | Invalid booking |

## Learning Objectives

- Practice nested conditional statements.
- Use logical operators such as `and` and `not`.
- Apply percentage calculations.
- Understand input validation and boundary conditions.
- Solve a real-world business problem using Python.
