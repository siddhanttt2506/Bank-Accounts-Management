# Bank Accounts Management

This project is a backend-only bank account management system using Python and PostgreSQL.  
**No frontend or web deployment is included.** All interactions are via the command line and SQL scripts.

## Features

- Manage bank accounts using a Python CLI (`bank.py`)
- PostgreSQL database schema and sample data provided
- SQL scripts for database setup and operations

## Setup

### 1. Database

1. Install PostgreSQL on your machine.
2. Create the database and tables:
   ```sh
   psql -U <your_username> -f bank_accounts_management_DB.sql
   psql -U <your_username> -f src/BAMS_Schema.sql
   ```
   *(Replace `<your_username>` with your PostgreSQL username)*

3. (Optional) Run additional SQL scripts in `src/` for more features or sample data.

### 2. Python CLI

1. Make sure you have Python 3 installed.
2. Run the CLI:
   ```sh
   python bank.py
   ```
   Follow the prompts to manage accounts.

## File Structure

- `bank.py` — Python CLI for bank operations
- `models.py` — ORM models (optional, for advanced usage)
- `bank_accounts_management_DB.sql` — Main database creation script
- `src/` — Additional SQL scripts (schema, sample data, user registration, etc.)

## Usage

- **All operations are performed via the terminal.**
- **No web interface or frontend is included.**
- Use the CLI for account management.
- Use SQL scripts for database setup and direct SQL queries.

## Requirements

- Python 3.x
- PostgreSQL

