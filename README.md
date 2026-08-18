# Python Projects – FC2

A collection of six Python projects built as part of my Python programming and data analytics training. The projects cover game logic, algorithms, automation, data handling with Pandas, and web scraping.

## 📌 Projects

### 1. Rock-Paper-Scissors Game
`1_rock_paper_scissors.py`

A simple interactive game where the user plays Rock-Paper-Scissors against the computer.

**Key concepts:** Python, `random` module, user input, conditional statements, game logic

**Features:**
- Accepts Rock, Paper, or Scissors as input
- Generates a random choice for the computer
- Determines the winner
- Handles invalid choices

---

### 2. Binary Search Algorithm
`2_binary_search.py`

A Python implementation of the Binary Search algorithm for efficiently finding a target value in a sorted list.

**Key concepts:** Functions, lists, loops, conditional statements, searching algorithms

**Features:**
- Searches a sorted list
- Uses the Binary Search technique
- Returns the index of the target value
- Displays a message if the value is not found

---

### 3. Send Emails Using Python
`3_send_emails.py`

A Python program that sends emails to one or multiple recipients using Gmail's SMTP server.

**Key concepts:** `smtplib`, email automation, SMTP, `MIMEText`, `MIMEMultipart`

**Features:**
- Connects to Gmail SMTP
- Sends emails to multiple recipients
- Supports custom email subjects and messages
- Automatically closes the SMTP connection

> **Security note:** the sender password is read from an environment variable (`EMAIL_PASSWORD`), not hardcoded. Never commit real credentials to a public repository — use an environment variable or an app-specific password.

---

### 4. Zodiac Sign Finder Using Pandas
`4_zodiac_sign_finder.py`

A Python program that takes a person's name and date of birth and determines their Zodiac sign, then stores the result in a CSV file using Pandas.

**Key concepts:** Python functions, user input, conditional statements, Pandas, DataFrames, CSV files

**Features:**
- Accepts name and birth date
- Determines the corresponding Zodiac sign
- Creates a Pandas DataFrame
- Exports the data to `zodiac_sign.csv`

---

### 5. Bulk File Renaming
`5_bulk_file_renaming.py`

A Python program that renames a batch of files in a directory to follow a consistent naming pattern.

**Key concepts:** `os` module, file system operations, string pattern matching, automation

**Features:**
- Takes a directory path and search pattern as input
- Finds all files matching the pattern
- Renames matches to a new, consistent pattern
- Preserves each file's original extension

---

### 6. Web Scraping Using Beautiful Soup
`6_web_scraping_beautifulsoup.py`

A web scraper that extracts the table of the largest companies in the US by revenue from Wikipedia, using Beautiful Soup and Pandas.

**Key concepts:** `requests`, `BeautifulSoup`, HTML parsing, Pandas

**Features:**
- Fetches a live Wikipedia page
- Parses the relevant HTML table
- Extracts rank, company name, industry, revenue, revenue growth, and headquarters
- Loads the results into a Pandas DataFrame

---

## 🛠️ Requirements

```
pandas
requests
beautifulsoup4
```

Install with:

```
pip install pandas requests beautifulsoup4
```

## ▶️ Running a project

Each project is a standalone script. Run any file directly, for example:

```
python 6_web_scraping_beautifulsoup.py
```
