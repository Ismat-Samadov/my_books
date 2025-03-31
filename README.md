# My Reading List Tracker 📚

A simple GitHub repository to track books I've read, am currently reading, or plan to read. This system provides a straightforward way to maintain a personal reading list using CSV format.

## Repository Structure

```
.
├── LICENSE
├── README.md
└── reading-list.csv
└── docs/
    └── index.html
```

## CSV Structure

The `reading-list.csv` file contains the following columns:

| Column | Description |
|--------|-------------|
| `book_id` | Unique identifier for each book |
| `start_date` | Date when you started reading (YYYY-MM-DD) |
| `finish_date` | Date when you finished reading (YYYY-MM-DD) |
| `book_name` | Title of the book |
| `author` | Author(s) of the book |
| `language` | Language the book is written in |
| `pdf_link` | Link to PDF version if available |
| `physically_exists` | Boolean indicating if you own a physical copy (true/false) |
| `status` | Reading status (to_read, in_progress, completed, abandoned) |
| `notes` | Your thoughts, quotes, or anything noteworthy about the book |

## How to Use

### Adding a New Book

1. Visit the [Book Entry Form](https://yourusername.github.io/my_books/) (GitHub Pages)
2. Fill out the book details 
3. Click "Generate CSV Line"
4. Click "Copy to Clipboard"
5. Open `reading-list.csv` in your repository
6. Paste the line at the end of the file and add the next book_id at the beginning

### Manual Entry

You can also directly edit the `reading-list.csv` file by:

1. Opening or cloning the repository
2. Adding a new line to the CSV file with all required fields
3. Committing the changes

Example CSV entry:
```
1,2023-10-15,2023-11-20,"The Pragmatic Programmer","Andrew Hunt, David Thomas",English,https://example.com/pragmatic.pdf,true,completed,"Great book on software craftsmanship"
```

## Format Guidelines

- Use YYYY-MM-DD format for dates
- Wrap text fields that might contain commas in double quotes
- Escape double quotes within fields by doubling them
- Use lowercase for status values: to_read, in_progress, completed, abandoned

## Status Meanings

- `to_read`: Books you plan to read
- `in_progress`: Books you're currently reading
- `completed`: Books you've finished reading
- `abandoned`: Books you started but decided not to finish

## Book Entry Form

I've created a simple HTML form to help generate properly formatted CSV lines. You can access it at:

https://yourusername.github.io/my_books/

The form includes:
- Required fields validation
- Auto-generation of properly escaped CSV
- Date helpers with "Today" buttons
- Status auto-suggestions based on dates
- Copy to clipboard functionality
- Dark mode interface

## Future Improvements

Potential improvements to consider:
- Automated statistics about reading habits
- Data visualization of reading progress
- Integration with external book APIs
- Reading goal tracking

## License

This repository is licensed under the [LICENSE included in the repository](LICENSE).

---

Happy reading! 📚