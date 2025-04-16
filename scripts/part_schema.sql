-- part_schema.sql
CREATE TABLE part (
    id INTEGER PRIMARY KEY,
    name VARCHAR(150),
    sku VARCHAR(30),
    description VARCHAR(1024),
    weight_ounces INTEGER,
    is_active TINYINT(1)
);

INSERT INTO part (name, sku, description, weight_ounces, is_active)
VALUES
    ('Heavy coil', 'SDJDDH8223DHJ', 'Tightly wound nickel-gravy alloy spring', 22, 1),
    ('Reverse lever', 'DCMM39823DSJD', 'Attached to provide inverse leverage', 9, 0),
    ('Macrochip', 'OWDD823011DJSD', 'Used for heavy-load computing', 2, 1);
