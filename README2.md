# 🧠 Python Function Projects: From Easy to Hard

A curated list of 10 Python projects focused on mastering functions — organized by difficulty with clear goals, success criteria, and stretch challenges.

---

## ✅ Easy Projects

### 1. Basic Calculator
- **Goal**: Create functions for basic math operations.
- **Success Criteria**:
  - Takes two numbers and an operator (+, -, *, /).
  - Outputs the correct result.
- **Stretch**:
  - Handle invalid input (e.g., division by zero or wrong operator).

---

### 2. Unit Converter
- **Goal**: Convert between units using functions.
- **Success Criteria**:
  - Correctly converts and displays values.
- **Stretch**:
  - Add support for multiple conversions (e.g., weight, distance).
  - Create a menu to select conversion type.

---

### 3. Grade Average Calculator
- **Goal**: Compute average and assign letter grades.
- **Success Criteria**:
  - Accepts a list of grades.
  - Outputs average and corresponding letter grade.
- **Stretch**:
  - Handle edge cases like empty lists or invalid entries.

---

### 4. Password Strength Checker
- **Goal**: Validate password strength.
- **Success Criteria**:
  - Checks for length, uppercase, lowercase, digit, and symbol.
- **Stretch**:
  - Suggest improvements for weak passwords.

---

### 5. Simple Tip Calculator
- **Goal**: Calculate tip and total bill.
- **Success Criteria**:
  - Takes bill and tip percentage, returns total.
- **Stretch**:
  - Split the bill between multiple people.

---

## 🔁 Medium Projects

### 6. Number Guessing Game
- **Goal**: Build a guess-the-number game.
- **Success Criteria**:
  - Random number generated.
  - User gets hints until they guess correctly.
- **Stretch**:
  - Limit number of guesses.
  - Score system based on attempts.

---

### 7. Mini Contact Book
- **Goal**: Add, search, and delete contacts.
- **Success Criteria**:
  - Use dictionary and functions for operations.
- **Stretch**:
  - Save/load contacts from a file.

---

### 8. Word Counter
- **Goal**: Analyze a paragraph.
- **Success Criteria**:
  - Count words, sentences, and characters.
- **Stretch**:
  - Display most common word and count unique words.

---

## 🚀 Hard Projects

### 9. Bank Account Simulation
- **Goal**: Simulate a bank account using classes and functions.
- **Success Criteria**:
  - Implement deposit, withdraw, and balance checking.
- **Stretch**:
  - Add account types (e.g., savings with limits).

---

### 10. Mini Quiz App
- **Goal**: Build a multiple-choice quiz app.
- **Success Criteria**:
  - Ask questions, collect answers, and show score.
- **Stretch**:
  - Add a timer and randomize question order.

---

## 📌 Tips for Success
- Keep your code clean with proper function names and comments.
- Use `input()` for user interaction and `print()` to display results.
- Try using error handling (`try/except`) in your stretch challenges.

---

✅ Track your progress by checking off each project as you go!

Happy coding! 🚀


# Python Projects: Lists and Tuples

This README includes 10 projects to practice working with **lists** and **tuples** in Python, ranked from easy to hard. Each project includes a **goal**, **success criteria**, and a **stretch challenge** to help improve your Python skills.

---

## 1. Even and Odd Splitter
- **Goal**: Separate even and odd numbers from a list.
- **Success Criteria**:
  - Function takes a list of numbers and returns two new lists: evens and odds.
- **Stretch**:
  - Also return the count of each.

---

## 2. List Sorter
- **Goal**: Sort a list in ascending or descending order.
- **Success Criteria**:
  - Function sorts the list based on user choice.
- **Stretch**:
  - Sort a list of tuples by the second value (e.g., `[(“A”, 2), (“B”, 1)] → [(“B”, 1), (“A”, 2)]`).

---

## 3. Duplicate Finder
- **Goal**: Identify duplicates in a list.
- **Success Criteria**:
  - Function returns a list of duplicate values.
- **Stretch**:
  - Return how many times each duplicate appears.

---

## 4. Tuple Unpacker
- **Goal**: Unpack a list of tuples into two separate lists.
- **Success Criteria**:
  - Input: `[(1, 'a'), (2, 'b')]` → Output: `[1, 2]`, `['a', 'b']`
- **Stretch**:
  - Repack them after processing (e.g., reversing values inside tuples).

---

## 5. Max and Min Tracker
- **Goal**: Find the highest and lowest numbers in a list.
- **Success Criteria**:
  - Function returns min and max values.
- **Stretch**:
  - Return the index positions of min and max too.

---

## 6. List Statistics
- **Goal**: Calculate mean, median, and mode.
- **Success Criteria**:
  - Function takes a list of numbers and returns the three stats.
- **Stretch**:
  - Handle edge cases (e.g., empty list, even number of items for median).

---

## 7. Student Score Manager
- **Goal**: Store names and scores in tuples and return the highest scorer.
- **Success Criteria**:
  - Input: `[("John", 87), ("Jane", 92)]` → Output: `Jane got the highest score.`
- **Stretch**:
  - Sort the list by score in descending order.

---

## 8. Flatten Nested List
- **Goal**: Turn a list of lists into one flat list.
- **Success Criteria**:
  - Input: `[[1, 2], [3, 4]]` → Output: `[1, 2, 3, 4]`
- **Stretch**:
  - Work for deeper levels of nesting (e.g., `[1, [2, [3]]]`).

---

## 9. List Combinations Generator
- **Goal**: Return all unique pairs from a list.
- **Success Criteria**:
  - Input: `[1, 2, 3]` → Output: `[(1, 2), (1, 3), (2, 3)]`
- **Stretch**:
  - Filter out combinations where the sum is greater than a threshold.

---

## 10. Mini To-Do List App
- **Goal**: Build a to-do list manager with tuples storing (task, status).
- **Success Criteria**:
  - Add, mark complete, delete tasks using a list of tuples.
- **Stretch**:
  - Save to and load from a file to keep tasks between sessions.

---

### How to Use This Repository

1. **Fork** or **Clone** this repository.
2. Start with the first project and move down the list.
3. Track your progress by checking off each project as you complete it.
4. Add your solutions in the form of Python files inside the `projects` folder.

---

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Python Dictionary Projects

This repository contains Python projects focusing on dictionaries. Each project aims to help you understand how to use Python dictionaries for various real-world applications, from simple lookups to more complex data structures.

## Project List

1. [Student Grades Dictionary](#student-grades-dictionary)
2. [Simple Phonebook](#simple-phonebook)
3. [Word Frequency Counter](#word-frequency-counter)
4. [Product Inventory Tracker](#product-inventory-tracker)
5. [Phone Number Validation](#phone-number-validation)
6. [Employee Salary System](#employee-salary-system)
7. [Nested Dictionary for Address Book](#nested-dictionary-for-address-book)
8. [Simple Quiz System](#simple-quiz-system)
9. [Shopping Cart System](#shopping-cart-system)
10. [Contact Grouping by Location](#contact-grouping-by-location)

---

## 1. Student Grades Dictionary

### Goal:
Create a dictionary to store students' names and their grades.

### Success Criteria:
- Function takes a name and grade as input and updates the dictionary.
- Return the grade for a given student.

### Stretch:
- Calculate and return the average grade of all students.

---

## 2. Simple Phonebook

### Goal:
Build a phonebook dictionary where names map to phone numbers.

### Success Criteria:
- Add, search, and delete contacts by name.

### Stretch:
- Allow users to search by phone number and return matching names.

---

## 3. Word Frequency Counter

### Goal:
Count how many times each word appears in a string.

### Success Criteria:
- Function takes a sentence and returns a dictionary of word frequencies.

### Stretch:
- Ignore punctuation and case (treat "Python" and "python" the same).

---

## 4. Product Inventory Tracker

### Goal:
Create an inventory dictionary where keys are product names and values are quantities.

### Success Criteria:
- Function allows you to add, remove, and update quantities.
- Return the quantity of a specific product.

### Stretch:
- Track product prices and compute the total value of inventory.

---

## 5. Phone Number Validation

### Goal:
Use a dictionary to store country codes and validate phone numbers.

### Success Criteria:
- Check if a phone number includes the correct country code.

### Stretch:
- Allow the program to handle different formats for phone numbers.

---

## 6. Employee Salary System

### Goal:
Store employee names and their salaries in a dictionary.

### Success Criteria:
- Add, update, and display salaries.
- Return the name of the highest-paid employee.

### Stretch:
- Calculate the average salary and return employees earning above the average.

---

## 7. Nested Dictionary for Address Book

### Goal:
Create a dictionary of addresses, where each contact has nested information like name, address, phone number.

### Success Criteria:
- Retrieve and update any piece of contact information.

### Stretch:
- Allow search by city or state and return all matching contacts.

---

## 8. Simple Quiz System

### Goal:
Store quiz questions and correct answers in a dictionary.

### Success Criteria:
- Function takes user input for an answer and compares it with the correct answer stored in the dictionary.

### Stretch:
- Allow the system to display a score after answering multiple questions.

---

## 9. Shopping Cart System

### Goal:
Create a shopping cart where each item is a dictionary with price and quantity.

### Success Criteria:
- Add items to the cart and calculate the total price.

### Stretch:
- Allow users to apply discount codes and calculate the new total price.

---

## 10. Contact Grouping by Location

### Goal:
Create a dictionary where each key is a city, and the value is a list of contacts in that city.

### Success Criteria:
- Add contacts to a specific city.
- Retrieve all contacts in a city.

### Stretch:
- Allow sorting contacts by name within each city and return them in order.

---

## How to Run the Projects

Each project is contained in its own Python file. To run any project, follow these steps:

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/python-dictionary-projects.git
    ```
2. Navigate to the project directory:
    ```bash
    cd python-dictionary-projects
    ```
3. Run the project:
    ```bash
    python project_name.py
    ```

---

## Contributing

Feel free to fork this repository, make changes, and create pull requests. Contributions and feedback are always welcome!

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
