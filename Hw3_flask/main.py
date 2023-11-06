from flask import Flask, request
from utils import commit_sql
from create_table import create_table

app = Flask(__name__)


@app.route('/phones/create')
def phones_create():
    contact_name = request.args['contact_name']
    phone_value = request.args['phone_value']

    sql = f"""
    INSERT INTO phones (ContactName, PhoneValue)
    VALUES ('{contact_name}','{phone_value}'); 
    """
    commit_sql(sql)

    return 'phones_create'


@app.route('/phones/read')
def phones_read():
    import sqlite3
    con = sqlite3.connect('phones.db')
    cur = con.cursor()

    sql = """
    SELECT * FROM Phones;
    """
    cur.execute(sql)

    result = cur.fetchall()
    con.close()

    return result


@app.route('/phones/update')
def phones_update():
    phone_id = request.args['phone_id']
    contact_name = request.args['contact_name']
    phone_value = request.args['phone_value']

    sql = f"""
    UPDATE Phones
    SET ContactName = '{contact_name}',
        PhoneValue = '{phone_value}'
    WHERE PhoneID = {phone_id};
    """
    commit_sql(sql)

    return 'phones_update'


@app.route('/phones/delete')
def phones_delete():
    phone_id = request.args['phone_id']

    sql = f"""
    DELETE FROM Phones
    WHERE PhoneID = {phone_id};
    """
    commit_sql(sql)

    return 'phones_delete'


if __name__ == '__main__':
    create_table()
    app.run(host='0.0.0.0', port=5001)

