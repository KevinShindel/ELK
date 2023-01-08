from mysql.connector import connect


def main():
    conn = connect(host="localhost",
                   user="root",
                   password="password")
    cur = conn.cursor()
    cur.execute(""" CREATE DATABASE IF NOT EXISTS test_db""")
    cur.execute(""" USE test_db """)
    cur.execute(""" CREATE TABLE IF NOT EXISTS users (id INT NOT NULL AUTO_INCREMENT,
                                        username VARCHAR(128) NOT NULL,
                                        created DATETIME DEFAULT NOW(), PRIMARY KEY (id)) """)
    for _ in range(1000):
        cur.execute(""" INSERT INTO test_db.users (username) VALUES ('Kevin Shindel'), ('Tymur Hilfatullin')""")
        conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    main()
