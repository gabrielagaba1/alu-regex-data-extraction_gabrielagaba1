# Norrsken Kigali Membership Invoice - Regex Data Extraction

## About The Project
This project is part of my Software Engineering coursework at ALU. The goal is to take unstructured text from a real-world document—in this case, a monthly coworking membership invoice from Norrsken House Kigali (`input/raw-text.txt`)—and extract meaningful information using Python and regular expressions (`re`).

The script parses through the invoice, extracts details like emails, contact numbers, prices, and links, and saves everything neatly formatted into a JSON file (`output/sample-output.json`).

---

## What the Script Extracts

- **Emails**: Finds all email addresses in the invoice and groups them into general emails, ALU staff emails, alumni emails, and student intern emails.
- **Credit Card Numbers**: Locates 16-digit card numbers and masks the middle digits (for example: `4120-****-****-3344`) so sensitive payment info is protected.
- **Phone Numbers**: Captures local Rwandan numbers, including both `+250` landlines and standard `07...` mobile numbers.
- **Web Links**: Pulls all URLs such as room reservation links and portals.
- **Prices and Times**: Extracts monetary amounts in Rwandan Francs (`Rwf`) and meeting time slots (`AM/PM`).
- **Security Check**: Scans the document for basic security threats like injected scripts (`<script>`) or SQL commands (`DROP TABLE`).

---

## Project Structure

```text
alu-regex-data-extraction_gabrielagaba1/
│
├── README.md                  # Project documentation
├── input/
│   └── raw-text.txt           # The raw invoice text
├── output/
│   └── sample-output.json     # The extracted JSON data
└── src/
    └── main.py                # Python script with extraction functions