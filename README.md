# Django Data Dump and Load Utility

This project provides instructions and tools to:
1. Dump data from a Django database into a JSON file.
2. Convert the encoding of the dumped data to UTF-8 (or another encoding of your choice).
3. Load the data back into a Django database.

---

## Prerequisites

- Python installed on your machine.
- Django installed in your project environment.
- An existing Django project with a configured database.

---

### Dump Data from the Database

Use the following Django management command to dump the database contents into a JSON file:

```bash
python manage.py dumpdata --indent 2 > data.json
```

If any 'charmap' error comes, use bash and run this:

```bash
PYTHONIOENCODING=utf-8 python manage.py dumpdata --indent 2 > db_dump.json
```

and if you have to change the encoding you can use the main.py
