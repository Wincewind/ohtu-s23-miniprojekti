# ohtu-s23-miniprojekti
![GHA workflow badge](https://github.com/Wincewind/ohtu-s23-miniprojekti/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/Wincewind/ohtu-s23-miniprojekti/graph/badge.svg?token=NT9QQT7HRH)](https://codecov.io/gh/Wincewind/ohtu-s23-miniprojekti)

- [Product Backlog](https://docs.google.com/spreadsheets/d/e/2PACX-1vTFMWHkg-GeTz5WsSQdvTTTKeWg1X4EbmagzSqQpQGtWI-dL88LgfhepvqFQfgGQxLHZ2dLskBmxhSG/pubhtml)

### Definition of Done
- User story acceptance criteria is met.
- Code is complete and refactored (if needed).
- Code is peer reviewed.
- Code is merged and successfully deployed to the development environment.
- Code is tested.

## How to setup and run locally (tested in Uni Linux environment, some steps/commands might be different on Windows or Mac):
1.  Clone the repository or download it as a zip:
```bash
git clone git@github.com:Wincewind/ohtu-s23-miniprojekti.git
```
2. Install current dependencies with command
```bash
poetry install
```
3. Activate poetry venv with command
```bash
poetry shell
```

4.  Start your PostgreSQL database if it's not running yet and create the required tables in psql using the schema.sql in the root folder.

**Note that this will delete any existing tables of the same name!**
```bash
psql < schema.sql
```
5.  Create .env file for the environment variables and assign appropriate values for them

The values in example.env should work if it's just renamed to ".env", but generating your own secure SECRET_KEY is **highly** recommended!

6.  The app should now be ready to run.
```bash
flask --app src/app.py run
```
