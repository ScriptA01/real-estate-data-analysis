# Real Estate Data Analysis

**Python Fundamentals | XML Data Extraction | Data Processing**

## 1. Overview

Real Estate Data Analysis is a Python project focused on extracting, processing, and displaying structured real estate information from XML files.

The project was developed as part of my Data Analysis learning journey, applying fundamental Python concepts studied in the **Python for Data Science** course at Alura.

Its main purpose is to explore real estate data, identify relevant property information, handle missing values, and format monetary data for easier interpretation.

## 2. Project Motivation

This project was inspired by my professional experience as an **Account Manager at a company that provides ERP and CRM solutions for the real estate industry**.

Through my daily interactions with real estate clients, I became familiar with property management processes, real estate listing integrations, and the importance of maintaining structured and consistent property information.

As I began my transition into Data Analysis, I wanted to connect my programming studies with a business environment I already understood.

I chose to work with an XML structure commonly used in real estate listing integrations, transforming my professional experience into an opportunity to practice Python and develop technical skills.

This project represents my first step toward combining **business knowledge, programming, and data analysis**.

## 3. Project Objectives

The main objectives of this project are:

- Read and interpret real estate XML files using Python.
- Identify and count property listings.
- Extract relevant information from each property.
- Identify property transaction types.
- Extract sale and rental prices when available.
- Format monetary values according to Brazilian currency conventions.
- Handle missing price information.
- Display structured property information in the terminal.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| ElementTree | XML parsing and data extraction |
| XML | Structured real estate data source |
| Git | Version control |
| GitHub | Project hosting and portfolio presentation |

## 5. Project Structure

```text
real-estate-data-analysis/
├── data/
│   └── adverts.xml       # Local dataset (not published)
├── src/
│   └── main.py           # Main Python script
├── .gitignore            # Excluded files
└── README.md             # Project documentation
```

The original XML dataset is excluded from version control to protect source data.

## 6. Features

### XML Data Extraction

The application uses Python's built-in `xml.etree.ElementTree` library to read and navigate XML elements.

For each property, the program extracts:

- Property ID
- Property title
- Transaction type
- Sale price, when available
- Rental price, when available
- Number of bedrooms
- Number of bathrooms

### Data Processing

The program applies basic data processing techniques, including:

- Iterating through property records using `for` loops.
- Extracting XML values using `findtext()`.
- Converting numeric strings using `float()`.
- Applying conditional statements to handle missing prices.
- Formatting monetary values in Brazilian real (BRL).

### Missing Data Handling

When a sale or rental price is not provided, the program displays an appropriate message instead of attempting to convert a missing value into a number.

## 7. Example Output

The following example is illustrative and does not represent a real client record.

```text
Total properties: 1

Property ID: 1001
Title: Sample Apartment
Sale price: R$ 450.000,00
Rental price: Rental price not available.
Transaction Type: For Sale
Total bedrooms: 2
Total bathrooms: 1
```

## 8. How to Run

### Requirements

- Python 3 installed.
- A compatible XML file containing real estate listing data.

### Instructions

1. Clone this repository:

```bash
git clone https://github.com/YOUR_USERNAME/real-estate-data-analysis.git
```

2. Navigate to the project directory:

```bash
cd real-estate-data-analysis
```

3. Place an authorized, compatible XML dataset in the `data` directory, using the filename `adverts.xml`.

4. Run the application:

```bash
python3 src/main.py
```

The program will display the total number of properties and their extracted information in the terminal.

**Note:** The application expects an XML structure compatible with the namespace and element paths configured in `main.py`. The original dataset is not included in this repository.

## 9. Learning Outcomes

This project allowed me to practice and reinforce fundamental Python concepts, including:

- Variables and data types
- String and numeric conversions
- `for` loops
- Conditional statements (`if` and `else`)
- String formatting with f-strings
- Working with structured XML data
- Basic missing-value handling
- Organizing a Python project
- Using Git for version control

Beyond programming, this project helped me understand how technical knowledge can be applied to practical business scenarios.

## 10. Future Development

This is the first project in my Data Analysis portfolio.

As I progress through my studies, I plan to develop additional projects involving more advanced Python concepts, data manipulation, SQL, and analytical techniques.

Each project will represent a new stage in my technical development.

## 11. Disclaimer

This is an independent educational project created for learning and portfolio purposes.

It is not an official product or integration of my employer.

The original XML dataset is excluded from the public repository, and no confidential client information is intended to be shared.

## Author

**Alessandro Silva**

Computer Science graduate | Account Manager | Aspiring Data Analyst

Developed as part of my professional transition into Data Analysis.