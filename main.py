# main.py - Poorly documented but functional
import requests
import sqlite3
import json
from datetime import datetime
import smtplib
from email.mime.text import MIMEText

class PriceTracker:
    def __init__(self, db_path="prices.db"):
        self.db_path = db_path
        self._setup_db()
    
    def _setup_db(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute('''CREATE TABLE IF NOT EXISTS products 
                       (id INTEGER PRIMARY KEY, url TEXT, name TEXT, 
                        target_price REAL, current_price REAL, 
                        last_checked TIMESTAMP)''')
        conn.close()
    
    def add_product(self, url, name, target_price):
        # No docstring, unclear what this does
        conn = sqlite3.connect(self.db_path)
        conn.execute("INSERT INTO products (url, name, target_price) VALUES (?, ?, ?)",
                    (url, name, target_price))
        conn.commit()
        conn.close()
    
    def check_prices(self):
        # Complex function with no documentation
        conn = sqlite3.connect(self.db_path)
        products = conn.execute("SELECT * FROM products").fetchall()
        
        for product in products:
            try:
                response = requests.get(product[1], headers={'User-Agent': 'Mozilla/5.0'})
                # Pretend we're scraping price - simplified for demo
                current_price = self._extract_price(response.text)
                
                if current_price and current_price <= product[3]:
                    self._send_alert(product[2], current_price, product[3])
                
                conn.execute("UPDATE products SET current_price=?, last_checked=? WHERE id=?",
                           (current_price, datetime.now(), product[0]))
            except Exception as e:
                print(f"Error checking {product[2]}: {e}")
        
        conn.commit()
        conn.close()
    
    def _extract_price(self, html):
        # Mysterious price extraction logic
        import re
        patterns = [
            r'\$(\d+\.?\d*)',
            r'price["\s]*:\s*["\s]*(\d+\.?\d*)',
            r'amount["\s]*:\s*["\s]*(\d+\.?\d*)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, html, re.IGNORECASE)
            if match:
                return float(match.group(1))
        return None
    
    def _send_alert(self, product_name, current_price, target_price):
        # Email sending with no error handling explanation
        msg = MIMEText(f"Price drop alert! {product_name} is now ${current_price} (target: ${target_price})")
        msg['Subject'] = f'Price Alert: {product_name}'
        msg['From'] = 'alerts@pricetracker.com'
        msg['To'] = 'user@example.com'
        
        server = smtplib.SMTP('localhost')
        server.send_message(msg)
        server.quit()

# utils.py - Helper functions with minimal docs
def format_currency(amount):
    return f"${amount:.2f}"

def calculate_savings(original, current):
    # What does this return? Percentage? Absolute amount?
    return ((original - current) / original) * 100

class NotificationSettings:
    def __init__(self):
        self.email_enabled = True
        self.sms_enabled = False
        self.threshold_percentage = 10