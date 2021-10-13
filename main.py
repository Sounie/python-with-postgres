import psycopg

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def read_from_db():
    conn = psycopg.connect("host=localhost dbname=docker user=docker password=my-local-pass")
    cur = conn.cursor()
    cur.execute("SELECT name FROM users limit 1;")
    result = cur.fetchone()

    cur.close()
    conn.close()
    print(f'Hi, {result[0]}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_from_db()
