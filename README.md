# REGULAR-EXPRESSION
🧾 User Input Validation Script using Python & Regex
This Python script is a simple console-based tool that validates user input for four fields: Name, Date of Birth, Email ID, and Mobile Number, using Regular Expressions (regex).

📌 Features
✅ Validates Name to accept only alphabetic characters (A-Z, a-z)

📅 Checks Date of Birth in the format DD-MM-YYYY

📧 Accepts only Gmail addresses in lowercase (e.g., username@gmail.com)

📱 Verifies Mobile Number in the format XXX-XXX-XXXX and stores it as a 10-digit number without dashes

💻 Tech Used
Python 3

re module (Regular Expressions)

🚀 How to Run
Make sure you have Python installed.

Clone or download this repository.

Run the script using:

bash
Copy
Edit
python input_validation.py
Follow the prompts and enter values as requested.

🧠 Example
yaml
Copy
Edit
Enter your name: John
Enter date of birth (DD-MM-YYYY): 15-08-1995
Enter email ID: johnsmith@gmail.com
Enter mobile number (XXX-XXX-XXXX): 123-456-7890

Name: John
Date of Birth: 15-08-1995
Email ID: johnsmith@gmail.com
Mobile Number: 1234567890
📂 File Structure
graphql
Copy
Edit
📁 input-validation
│
├── input_validation.py     # Main script
├── README.md               # Project documentation
🛡️ License
This project is licensed under the MIT License.

