import sqlite3

database=sqlite3.connect("R:/Study/(1)_Python course/simple_database.sqlite")
cursor=database.cursor()
create_table='''CREATE TABLE IF NOT EXISTS products
                        (product_id INT,
                         name TEXT,
                         amount INT,
                         PRIMARY KEY(product_id));'''
cursor.execute(create_table)
add_soda='''INSERT OR REPLACE INTO products
                    (product_id, name, amount) VALUES (1, 'Soda', 10);'''
cursor.execute(add_soda)
database.commit()
add_product='''INSERT OR REPLACE INTO products
                        (product_id, name, amount) VALUES (?, ?, ?);'''
cursor.execute(add_product, (2, "Waffel", 15))
cursor.execute(add_product, (3, "Cookie", 20))
cursor.execute(add_product, (4, "Chips", 3))
cursor.execute(add_product, (5, "Water", 130))
cursor.execute(add_product, (6, "Snack", 20))
cursor.execute(add_product, (7, "Cola", 80))
database.commit()
select_soda='''SELECT product_id, amount
                        FROM products
                        WHERE name="Soda";'''
# cursor.execute(select_soda)
# print(cursor.fetchone())
select_product='''SELECT *
                            FROM products
                            WHERE amount=?;'''
cursor.execute(select_product, (20, ))
# print(cursor.fetchone())
# print(cursor.fetchmany(2))
select_everything='''SELECT *
                                FROM products;'''
# cursor.execute(select_everything)
# results1=cursor.fetchall()
# print(results1)
update_amount_by_product_id="""UPDATE products
                                                        SET amount=?
                                                        WHERE product_id=?;"""
update_amount2='''UPDATE products
                              SET amount=?
                              WHERE amount=?;'''
cursor.execute(update_amount_by_product_id, (32, 3))
database.commit()
delete_product="""DELETE
                              FROM products
                              WHERE name=?;"""
cursor.execute(delete_product, ("Snack",))
database.commit()
select_between="""SELECT *
                                FROM products
                                WHERE product_id BETWEEN ? AND ?;"""
def print_results(query=None, params=None):
    if params is None:
        cursor.execute(query)
    else:
        cursor.execute(query, params)
    print("Amount of  activated is:", cursor.rowcount)
    results2=cursor.fetchall()
    for res in results2:
        print(res, end=" ")
    print()
# print_results(add_soda)
# print_results(select_everything)
# print_results(select_product, (20, ))
cursor.execute(add_product, (6, "Candy", 80))
# print_results(update_amount2, (95, 80))
database.commit()
# print_results(select_between, (3, 7))
order_table="""SELECT *
                         FROM products
                         ORDER BY product_id DESC;"""
print_results(order_table)
database.commit()
# delete_table="DROP TABLE IF EXISTS products;"
# cursor.execute(delete_table)
# cursor.close()
# database.close()
