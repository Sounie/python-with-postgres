import psycopg

def read_from_db():
    with psycopg.connect("host=localhost dbname=docker user=docker password=my-local-pass") as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT name FROM users limit 1;")
            result = cur.fetchone()

            print(f'Hi, {result[0]}')

if __name__ == '__main__':
    read_from_db()
