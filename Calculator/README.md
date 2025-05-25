Scientific Calculator – Python Command Line App
This is a simple calculator program you can run from the command line. It’s written in Python and handles both basic math like addition and multiplication, and some more advanced functions like sine, cosine, logarithms, and powers. It uses Python’s built-in math module, so you don’t need to install anything extra.

Files
The main file here is calculator.py. Just run this script, and it will walk you through using the calculator.

Features
Basic operations include adding, subtracting, multiplying, and dividing numbers. The calculator also checks for division by zero and gives you an error if you try that.

For advanced math, you can calculate sine, cosine, and tangent (you give the angle in degrees, and the program does the conversion internally). You can also compute natural logarithms (only for positive numbers), square roots (only for zero or positive numbers), and powers (raising one number to the power of another).

How to Use It
First, make sure you have Python 3 installed on your computer. Download or clone this project, then run the script by typing:

nginx
Copy
Edit
python calculator.py
Follow the on-screen instructions to choose whether you want to do a basic calculation or an advanced one, then enter your numbers and operations.

Example
Here’s how it looks when you use it:

yaml
Copy
Edit
Scientific Calculator

Select mode:
1. Basic Operations
2. Advanced Operations
3. Exit
Enter choice: 2

Advanced operations: sin, cos, tan, sqrt, power
Enter operation: sin
Enter number: 30
Result: 0.5
Important Notes
The program tries to catch common mistakes like dividing by zero or taking the log of a negative number and gives you clear error messages. Also, remember that the trigonometric functions expect the angle in degrees, not radians — the program converts this automatically.

License
This project is open source under the MIT License. Feel free to use or modify it however you want.

Contributing
If you have ideas for improvements or want to add new features, please open an issue or send a pull request. Suggestions for things like factorials, calculation history, or even a graphical interface would be great!
