#!/usr/bin/env python3
import csv
import os
from datetime import datetime

def get_next_id():
    """Get the next book ID by checking the existing CSV."""
    try:
        with open('reading-list.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            return max(int(row[0]) for row in reader if row and row[0].isdigit()) + 1
    except (FileNotFoundError, ValueError, StopIteration):
        return 1

def add_book():
    """Add a new book entry to the CSV file."""
    # Check if file exists, if not create with headers
    file_exists = os.path.isfile('reading-list.csv')
    
    # Get book details from user
    book_name = input("Book name: ")
    author = input("Author: ")
    language = input("Language [English]: ") or "English"
    
    start_date = input("Start date (YYYY-MM-DD) [leave empty if not started]: ")
    if start_date == "today":
        start_date = datetime.now().strftime("%Y-%m-%d")
    
    finish_date = input("Finish date (YYYY-MM-DD) [leave empty if not finished]: ")
    if finish_date == "today":
        finish_date = datetime.now().strftime("%Y-%m-%d")
    
    pdf_link = input("PDF link [optional]: ")
    
    physically_exists = input("Do you have a physical copy? (y/n) [n]: ").lower()
    physically_exists = "true" if physically_exists == "y" else "false"
    
    status_options = ["to_read", "in_progress", "completed", "abandoned"]
    print("Status options:")
    for i, option in enumerate(status_options):
        print(f"{i+1}. {option}")
    
    status_choice = input(f"Choose status [1-{len(status_options)}]: ")
    try:
        status = status_options[int(status_choice) - 1]
    except (ValueError, IndexError):
        status = "to_read"  # Default
    
    notes = input("Notes [optional]: ")
    
    # Get next book ID
    book_id = get_next_id()
    
    # Create book entry
    book_entry = [
        str(book_id),
        start_date,
        finish_date,
        book_name,
        author,
        language,
        pdf_link,
        physically_exists,
        status,
        notes
    ]
    
    # Write to CSV
    with open('reading-list.csv', 'a', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        
        # Write header if file doesn't exist
        if not file_exists:
            writer.writerow([
                'book_id', 'start_date', 'finish_date', 'book_name', 'author',
                'language', 'pdf_link', 'physically_exists', 'status', 'notes'
            ])
        
        writer.writerow(book_entry)
    
    print(f"\nBook '{book_name}' added successfully with ID {book_id}!")

if __name__ == "__main__":
    print("=== Add Book to Reading List ===")
    add_book()
    
    while input("\nAdd another book? (y/n): ").lower() == 'y':
        add_book()