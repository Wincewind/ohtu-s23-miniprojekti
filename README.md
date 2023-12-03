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

### Acceptance criteria

As a User, I want to be able to list my references in human-readable form

- The user can see all the added references in the UI.
- The frontend fetches the references from backend.
- Backend gets the data from the database.
- Newly added references can be seen without the need to update the page.

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

4.  Start your PostgreSQL database if it's not running yet. Init database and build everything with the following command

**Note: this will reset the database!**

```bash
invoke build-full-init-db
```

5.  Create .env file for the environment variables and assign appropriate values for them

The values in example.env should work if it's just renamed to ".env", but generating your own secure SECRET_KEY is **highly** recommended!

6.  The app should now be ready to run.

```bash
invoke start
```

### Scripts

**Note: Run these scripts inside the Poetry shell. Enter `poetry shell` to activate the shell.**

Install frontend dependencies and build:

```bash
invoke build-frontend
```

Install backend dependencies:

```bash
invoke build-backend
```

Run Flask app:

```bash
invoke start
```

Initialize database:

```bash
invoke init-db
```

Run `build-frontend` & `build-backend`:

```bash
invoke build-full
```

Run `build-frontend`, `build-backend` & `init-db`:

```bash
invoke build-full-init-db
```
