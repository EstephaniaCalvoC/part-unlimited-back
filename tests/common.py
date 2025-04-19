DATABASE_FILE = "parts_unlimited.db"
DATABASE_URL = f"sqlite:///{DATABASE_FILE}"


PART_1 = {
    "id": 1,
    "name": "Heavy coil",
    "sku": "SDJDDH8223DHJ",
    "description": "Tightly wound nickel-gravy alloy spring",
    "weight_ounces": 22,
    "is_active": True,
}

PART_2 = {
    "id": 2,
    "name": "Reverse lever",
    "sku": "DCMM39823DSJD",
    "description": "Attached to provide inverse leverage",
    "weight_ounces": 9,
    "is_active": False,
}

PARTS_WORDS = [
    {"id": "tightly", "count": 1},
    {"id": "wound", "count": 1},
    {"id": "nickel", "count": 1},
    {"id": "gravy", "count": 1},
    {"id": "alloy", "count": 1},
    {"id": "spring", "count": 1},
    {"id": "attached", "count": 1},
    {"id": "to", "count": 1},
    {"id": "provide", "count": 1},
    {"id": "inverse", "count": 1},
    {"id": "leverage", "count": 1},
]

NEW_PART = {
    "name": "Macrochip",
    "sku": "OWDD823011DJSD",
    "description": "Used for heavy-load computing",
    "weight_ounces": 2,
    "is_active": True,
}
