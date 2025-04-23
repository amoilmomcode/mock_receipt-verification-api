import sqlite3
from flask import g

DATABASE = 'data.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def select(query, param):
    db = get_db()
    cur = db.cursor()
    cur.execute(query, param)
    result = cur.fetchall()
    cur.close()

    return result

def logReceipt(receipt):
    existCount = selectReceipt(receipt.receipt_id)

    if existCount <= 0:
        db = get_db()
        db.execute('INSERT OR IGNORE INTO receipts (user_id, receipt_id, platform, status) VALUES (?,?,?,?)', (receipt.user_id, receipt.receipt_id, receipt.platform, receipt.status))
        db.commit()


def selectReceipt(receipt_id):
    return select('SELECT COUNT(*) FROM receipts WHERE receipt_id = ?', (receipt_id,))[0][0]

