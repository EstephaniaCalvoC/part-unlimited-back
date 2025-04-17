# part-unlimited-back

Simple API to expose CRUD operation of Parts Unlimited parts.

**Context**: Parts Unlimited catalogs its seemingly unlimited parts, and we need a service built which will be
used by other teams to manage various aspects of them through the existing endpoint.

## Prerequisites

- Python 3.12
- SQLite


## Set up:

**1. Set environment variables**
```bash
#In .env

DATABASE_URL=sqlite:///./parts_unlimited.db
LOG_LEVEL=DEBUG
```

**2.Run app**
```bash
# This will init db and run the FastAPI app with Uvicorn.
# Maybe you'll need to run sudo apt-get install sqlite3 first.
make run
```

The database will be created in the root directory of the project with three parts.

| id | name | sku | description | weight_ounces | is_active |
|----|----|----|----|----|----|
| 1 | Heavy coil | SDJDDH8223DHJ | Tightly wound nickel-gravy alloy spring | 22 | True |
| 2 | Reverse lever | DCMM39823DSJD | Attached to provide inverse leverage | 9 | False |
| 3 | Macrochip | OWDD823011DJSD | Used for heavy-load computing | 2 | True |


**3. Try API**

1. Open http://localhost:8000/docs
2. Try get all parts GET /api/parts
3. Try get part by sku GET /api/parts/{sku}
4. Try delete part by id DELETE /api/parts/{id}
5. Try create part POST /api/parts


**4.Clean environment**
```bash
make clean
```
