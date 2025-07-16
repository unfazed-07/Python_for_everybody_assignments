# 🎵 Music Track Data Organizer with SQLite

This project demonstrates how to extract music metadata from a CSV file and store it in a structured SQLite database using Python. It was built as part of my learning journey through the **Python for Everybody Specialization** by the **University of Michigan on Coursera**.

## 📦 Project Files

| File              | Description                                                 |
|------------------|-------------------------------------------------------------|
| `tracksss.py`     | Python script that reads from `tracks.csv` and inserts data into SQLite |
| `tracks.csv`      | Source file containing music metadata (artist, title, rating, length, etc.) |
| `tracknow.sqlite` | SQLite database containing organized tables extracted from the CSV |

## 🛠️ Technologies Used

- **Python 3**: Script automation and file handling
- **sqlite3**: Creation and manipulation of SQL tables
- **os**: Handling file paths and directories

## 📚 How It Works

1. Run `tracksss.py` to process the contents of `tracks.csv`.
2. The script creates and populates an SQLite database named `tracknow.sqlite`.
3. To view the extracted data:
   - Open **DB Browser for SQLite**
   - Select the `tracknow.sqlite` file
   - Navigate to the **Browse Data** tab to view the well-organized tables

This setup ensures all tracks and related metadata are sorted and easily accessible in relational format.


---

