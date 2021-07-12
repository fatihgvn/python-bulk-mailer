import sqlite3

def initTables(db):
    c = db.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS `smtp`(
        `sendername` varchar(255),
        `mail` varchar(255),
        `passwd` varchar(255),
        `server` varchar(255),
        `port` int
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS `mailaddress`(
        `name` varchar(255),
        `mail` varchar(255),
        `counter` int
    )
    """)

    db.commit()
