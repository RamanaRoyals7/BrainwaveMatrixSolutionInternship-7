# ATM Interface Application

This repository contains a simple ATM interface simulation built using Python. The program mimics basic ATM functionalities such as checking balance, depositing money, withdrawing money, and generating receipts.

---

## Features

1. **Card Insertion Simulation**  
   Simulates the insertion of a card to initiate the ATM interface.

2. **Language Selection**  
   Supports multiple languages:
   - English
   - Hindi
   - Kannada
   - Telugu  
   Defaults to English if an invalid selection is made.

3. **PIN Verification**  
   Allows the user to enter a 4-digit PIN.
   - Validates PIN length and ensures it is numeric.
   - Limits attempts to 3 before blocking the card.

4. **Transaction Options**  
   - **Check Balance**: Displays the current account balance.
   - **Deposit Money**: Allows the user to deposit an amount and updates the balance.
   - **Withdraw Money**: Enables the user to withdraw an amount, provided it is within the balance.
   - **Exit**: Ends the session.

5. **Receipt Generation**  
   Provides a detailed receipt for deposit and withdrawal transactions, showing:
   - Transaction type
   - Amount
   - Remaining balance

---

## Prerequisites

- Python 3.x

---

## How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/atm-interface.git
cd atm-interface
