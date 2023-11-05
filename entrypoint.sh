#!/bin/bash

# Prompt the user to enter a number (1 or 2)
read -p "Enter 1 to run producer.py, or 2 to run consumer.py: " choice

# Check the user's input and execute the respective Python file
if [ "$choice" = "1" ]; then
    python producer.py
elif [ "$choice" = "2" ]; then
    python consumer.py
else
    echo "Invalid choice. Please enter 1 or 2."
fi