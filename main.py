{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d20266a2-cd25-48ae-82f6-3f50d64a2177",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Simple Calculator\n",
      "Select operation:\n",
      "1. Add\n",
      "2. Subtract\n",
      "3. Multiply\n",
      "4. Divide\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter choice (1/2/3/4):  1\n",
      "Enter first number:  5\n",
      "Enter second number:  5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5.0 + 5.0 = 10.0\n"
     ]
    }
   ],
   "source": [
    "# Function to add two numbers\n",
    "def add(x, y):\n",
    "    return x + y\n",
    "\n",
    "# Function to subtract two numbers\n",
    "def subtract(x, y):\n",
    "    return x - y\n",
    "\n",
    "# Function to multiply two numbers\n",
    "def multiply(x, y):\n",
    "    return x * y\n",
    "\n",
    "# Function to divide two numbers\n",
    "def divide(x, y):\n",
    "    if y == 0:\n",
    "        return \"Error! Division by zero.\"\n",
    "    return x / y\n",
    "\n",
    "# Main program\n",
    "def calculator():\n",
    "    print(\"Simple Calculator\")\n",
    "    print(\"Select operation:\")\n",
    "    print(\"1. Add\")\n",
    "    print(\"2. Subtract\")\n",
    "    print(\"3. Multiply\")\n",
    "    print(\"4. Divide\")\n",
    "\n",
    "    # Take input from the user\n",
    "    choice = input(\"Enter choice (1/2/3/4): \")\n",
    "\n",
    "    if choice in ['1', '2', '3', '4']:\n",
    "        num1 = float(input(\"Enter first number: \"))\n",
    "        num2 = float(input(\"Enter second number: \"))\n",
    "\n",
    "        if choice == '1':\n",
    "            print(f\"{num1} + {num2} = {add(num1, num2)}\")\n",
    "        elif choice == '2':\n",
    "            print(f\"{num1} - {num2} = {subtract(num1, num2)}\")\n",
    "        elif choice == '3':\n",
    "            print(f\"{num1} * {num2} = {multiply(num1, num2)}\")\n",
    "        elif choice == '4':\n",
    "            print(f\"{num1} / {num2} = {divide(num1, num2)}\")\n",
    "    else:\n",
    "        print(\"Invalid input\")\n",
    "\n",
    "# Run the calculator\n",
    "calculator()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1567b2ac-7df0-485b-9149-293c7924b779",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
