
# 🔐 Password Strength Checker

## 📌 Project Overview

Password Strength Checker is a Python-based cybersecurity mini-project that evaluates the strength of a password based on different security criteria.

It checks password length, uppercase letters, lowercase letters, numbers, special characters, commonly used passwords, and repeated characters.

The application classifies passwords into three categories: WEAK, MEDIUM, and STRONG.

## 🎯 Objectives

- Understand basic password security concepts.
- Identify weak and commonly used passwords.
- Encourage users to create strong passwords.
- Learn Python programming and regular expressions.
- Improve awareness of cybersecurity practices.

## ✨ Features

- Password length validation.
- Uppercase letter detection.
- Lowercase letter detection.
- Number detection.
- Special character detection.
- Common password detection.
- Repeated character detection.
- Password strength scoring system.
- Suggestions to improve password security.

## 🛠️ Technologies Used

- Python 3
- Regular Expressions (re module)
- Conditional Statements
- Functions
- Sets and Strings

## ⚙️ How It Works

The program evaluates the entered password using six criteria:

1. Minimum 8 characters.
2. Recommended length of 12 characters.
3. At least one uppercase letter.
4. At least one lowercase letter.
5. At least one number.
6. At least one special character.

It also checks for common passwords and repeated characters.

## 📊 Password Strength Classification

| Score | Strength |
|-------|----------|
| 0–2   | WEAK     |
| 3–4   | MEDIUM   |
| 5–6   | STRONG   |

Note: Common passwords are automatically classified as WEAK.

## ▶️ How to Run

**Step 1:** Install Python 3.

**Step 2:** Clone the repository.

```bash
git clone https://github.com/your-username/Password-Strength-Checker.git
```

**Step 3:** Open the project folder.

```bash
cd Password-Strength-Checker
```

**Step 4:** Run the Python program.

```bash
python password_strength_checker.py
```

## 💻 Sample Output

```text
==========================================
       PASSWORD STRENGTH CHECKER
==========================================

Enter your password: CyberSecure@2026

------------------------------------------
           PASSWORD REPORT
------------------------------------------
Password          : CyberSecure@2026
Password Length   : 16
Security Score    : 6/6
Password Strength : STRONG

Excellent! Your password has good strength.
------------------------------------------
```

## 📂 Project Structure

```text
Password-Strength-Checker/
│
├── password_strength_checker.py
└── README.md
```

## 🔒 Security Note

This project is developed for educational purposes.

The current demonstration version displays the entered password in the terminal. Do not use real or personal passwords while testing this version.

For better privacy, use Python's getpass module to hide password input and avoid displaying the password in the output.

## 🚀 Future Enhancements

- Add a graphical user interface (GUI).
- Implement password entropy calculation.
- Integrate a larger common-password database.
- Add password visibility controls.
- Improve password security analysis.

## 👨‍💻 Author

**Sundarraj V**

Cyber Security Student

## 📅 Project Details

- **Task:** Week 5
- **Project:** Password Strength Checker
- **Domain:** Cybersecurity
- **Programming Language:** Python

---

⭐ If you find this project useful, consider giving the repository a star!
