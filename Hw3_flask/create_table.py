def create_table() -> None:
    import sqlite3
    con = sqlite3.connect('phones.db')
    cur = con.cursor()

    sql = """
        CREATE TABLE IF NOT EXISTS phones (
        PhoneID INTEGER PRIMARY KEY,
        ContactName varchar(255),
        PhoneValue varchar(255)
        );
        """
    cur.execute(sql)
    con.commit()
    con.close()
