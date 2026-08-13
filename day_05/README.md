# Bank Account Program

## Overview

In the meet after learning about clsses and objects and as well as the methods of the class this program was built to demonstrate all that.

The class allows us to:
- Create a bank account
- Store the account owner's name and balance
- Deposit money
- Withdraw money
- Display the current balance
- Handle insufficient balance


## Class Components

### Attributes

- `self.owner` — Stores the account owner's name.
- `self.balance` — Stores the current account balance.

### Methods

- `__init__()` — Initializes the account with an owner and starting balance.
- `deposit()` — Adds the specified amount to the balance.
- `withdraw()` — Withdraws money if sufficient balance is available.
- `show_balance()` — Displays the current balance.


## Execution Flow

### 1. Create the Account

account = BankAccount('Gosling', 5000)

A `BankAccount` object is created.

The constructor receives:
- owner = "Gosling"
- balance = 5000

These values are stored using:

self.owner = owner
self.balance = balance

Initial balance: 5000


### 2. Deposit Money

account.deposit(1500)

The `deposit()` method adds 1500 to the current balance.

5000 + 1500 = 6500

New balance: 6500


### 3. Withdraw Money

account.withdraw(2000)

The method checks whether sufficient balance is available:

if amount <= self.balance:

Since 2000 <= 6500, the withdrawal is allowed.

6500 - 2000 = 4500

New balance: 4500


### 4. Display Balance

account.show_balance()

The current balance is displayed.


## Output

Balance: 4500


## Summary

The program combines an object's data and the operations performed on that data within a single class. This demonstrates the basic structure and usage of Object-Oriented Programming in Python.