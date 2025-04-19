# part-unlimited-back

Simple API to expose CRUD operation of Parts Unlimited parts.

**Context**: Parts Unlimited catalogs its seemingly unlimited parts, and we need a service built which will be
used by other teams to manage various aspects of them through the existing endpoint.

## Prerequisites

- Python 3.12
- SQLite

## Set up:

This project has a [Makefile](Makefile) with some useful commands:

- `make help`: Show help
- `make run`: Create a virtual environment, setup dependencies, run migrations and run the FastAPI app with Uvicorn.
- `make clean`: Clean the environment
- `make run_test`: Create a virtual environment, setup dependencies, run unit and integration tests with coverage.


**1. Set environment variables**

```bash
#In .env

DATABASE_URL=sqlite:///./parts_unlimited.db
LOG_LEVEL=DEBUG
```

**2.Run app**

```bash
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
2. Try to get all parts via `GET /api/parts`
3. Try to get part by sku via `GET /api/parts/{sku}`
4. Try to delete part by id via `DELETE /api/parts/{id}`
5. Try to create part via `POST /api/parts`
6. Try to update part by id via `PUT /api/parts/{id}`
7. Try to get top common words in part description via `POST /api/analytics/part/get-top-common-words`


**4.Clean environment**

```bash
make clean
```

## Developer Notes

- To run unit and integration tests with coverage, use `make run_test`.


- **Request and response examples** are available in the [OpenAPI documentation](http://localhost:8000/docs).


- The approach to retrieving the **top common words in part descriptions** relies on a dedicated table that tracks word frequency for each part description. This table is automatically updated when a part is **created, deleted, or modified**, optimizing performance by avoiding real-time word counting for every API request.


- The `get_top_common_words` endpoint supports **filtering out common words** (e.g., *"to", "and", "of"*) and defaults to returning the **top 5 most frequent words**.


- For a **large number of parts**, implementing **pagination** in the `get_parts` endpoint is recommended to enhance performance and usability.

### Assumptions

- Each **SKU is unique** per part.  
- All fields must **not be null**, except for the **description** field.  
- The **Part table** has already been created and populated with data, requiring **migrations to be run** before use.
