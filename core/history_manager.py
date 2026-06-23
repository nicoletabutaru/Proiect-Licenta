import sqlite3
import os
from datetime import datetime


DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'chat_history.db')

def init_db():
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
  
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            question TEXT,
            detected_topic TEXT,
            response TEXT
        )
    ''')
    
    conn.commit()
    conn.close()
    print(" History Database initialized successfully.")

def save_interaction(question, topic, response):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute('''
        INSERT INTO history (timestamp, question, detected_topic, response)
        VALUES (?, ?, ?, ?)
    ''', (timestamp, question, topic, response))
    
    conn.commit()
    conn.close()

def get_history():
  
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('SELECT timestamp, question, detected_topic, response FROM history ORDER BY id DESC')
    rows = cursor.fetchall()
    
    conn.close()
    return rows