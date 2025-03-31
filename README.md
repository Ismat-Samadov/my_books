# My Reading List Tracker 📚

A simple GitHub repository to track books I've read, am currently reading, or plan to read. This system provides a straightforward way to maintain a personal reading list using CSV format.

## Repository Structure

```
.
├── LICENSE
├── README.md
├── favicon.ico
├── index.html
└── reading-list.csv
```

## CSV Structure

The `reading-list.csv` file contains the following columns:

| Column | Description |
|--------|-------------|
| `book_name` | Title of the book |
| `author` | Author(s) of the book |
| `language` | Language the book is written in |
| `physically_exists` | Boolean indicating if you own a physical copy (true/false) |
| `status` | Reading status (to_read, in_progress, completed, abandoned) |
| `notes` | Your thoughts, quotes, or anything noteworthy about the book |

## Sample Data

```
book_name,author,language,physically_exists,status,notes
"Stratejik Pazarlama","Harvard Business Review Press",Turkish,true,completed,"interesting book for sales"
"HBR's 10 Must Reads on Managing People","Harvard Business Review Press",English,true,completed,"bullshit"
"HBR On Leadership","Harvard Business Review Press",English,true,completed,"bullshit"
"HBR's 10 Must Reads on Making Smart Decisions","Harvard Business Review Press",English,true,completed,"bullshit"
"HBR's 10 Must Reads on Teams","Harvard Business Review Press",English,true,completed,"bullshit"
```

## How to Use

### Adding a New Book

1. Visit the [Book Entry Form](https://yourusername.github.io/my_books/) (GitHub Pages)
2. Fill out the book details 
3. Click "Generate CSV Line"
4. Click "Copy to Clipboard"
5. Open `reading-list.csv` in your repository
6. Paste the line at the end of the file

### Manual Entry

You can also directly edit the `reading-list.csv` file by:

1. Opening or cloning the repository
2. Adding a new line to the CSV file with all required fields
3. Committing the changes

Example CSV entry:
```
"The Pragmatic Programmer","Andrew Hunt, David Thomas",English,true,completed,"Great book on software craftsmanship"
```

## Format Guidelines

- Wrap text fields that might contain commas in double quotes
- Escape double quotes within fields by doubling them
- Use lowercase for status values: to_read, in_progress, completed, abandoned

## Status Meanings

- `to_read`: Books you plan to read
- `in_progress`: Books you're currently reading
- `completed`: Books you've finished reading
- `abandoned`: Books you started but decided not to finish

## Book Entry Form

I've created a simple HTML form to help generate properly formatted CSV lines. The form is included directly in the repository as `index.html` and can be accessed via GitHub Pages at:

https://yourusername.github.io/my_books/

The form includes:
- Required fields validation
- Auto-generation of properly escaped CSV
- Language selection (English, Turkish, Azerbaijani, Russian)
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