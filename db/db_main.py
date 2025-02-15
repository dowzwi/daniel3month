import sqlite3
from db import queries

db = sqlite3.connect('store.sqlite3')
cursor = db.cursor()


async def sql_create():
    if db:
        print('База данных подключена!')

    cursor.execute(queries.CREATE_TABLE_PRODUCTS)
    cursor.execute(queries.CREATE_TABLE_PRODUCTS_DETAILS)
    cursor.execute(queries.CREATE_TABLE_COLLECTION_PRODUCTS)
    db.commit()


async def sql_insert_products(name_product, size, price, product_id, photo):
    with sqlite3.connect('store.sqlite3') as db_with:
        cursor_with = db_with.cursor()
        cursor_with.execute(queries.INSERT_PRODUCTS_QUERY, (
            name_product,
            size,
            price,
            product_id,
            photo
        ))
        db_with.commit()


async def sql_insert_products_details(product_id, category, info_product):
    with sqlite3.connect('store.sqlite3') as db_with:
        cursor_with = db_with.cursor()
        cursor_with.execute(queries.INSERT_PRODUCTS_QUERY_DETAILS, (
            product_id, category, info_product
        ))
        db_with.commit()

async def sql_insert_collection_products(collection_products, product_id):
    with sqlite3.connect('store.sqlite3') as db_with:
        cursor_with = db_with.cursor()
        cursor_with.execute(queries.INSERT_PRODUCTS_QUERY_COLLECTION, (
            collection_products,
            product_id

        ))
        db_with.commit()

