# Bank Accounts Management

This project is a command-line based bank account management system using Python and PostgreSQL.

## Features

- Manage bank accounts via a Python command-line interface (CLI).
- Uses SQLAlchemy for object-relational mapping (ORM).
- Includes SQL scripts for complete database and schema setup.

## Requirements

- Python 3.x
- PostgreSQL
- Dependencies listed in `requirements.txt`

## Setup

1.  **Install PostgreSQL** on your system if you haven't already.

2.  **Set up the database** by running the provided SQL scripts. You will need to create the initial database first.
    ```sh
    # Connect to psql and create the database
    psql -U <your_username>
    CREATE DATABASE bank_management;
    \q

    # Run the schema scripts
    psql -U <your_username> -d bank_management -f src/BAMS_Schema.sql
    ```
    *(Replace `<your_username>` with your PostgreSQL username)*

3.  **Install Python dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the main application from your terminal:

```sh
python bank.py
```

Follow the on-screen prompts to interact with the banking system.

## File Structure

-   `bank.py`: The main CLI application entry point.
-   `models.py`: Defines the database tables using SQLAlchemy ORM.
-   `src/BAMS_Schema.sql`: SQL script to create tables and seed data.
-   `requirements.txt`: A list of Python package dependencies.

## Contributors

- Ayushman Daruka
- Mrinal Chaturvedi
- Siddhant Shekhar
