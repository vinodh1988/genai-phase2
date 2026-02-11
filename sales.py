import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker('en_IN')
np.random.seed(42)
random.seed(42)

# Indian product categories and realistic products
categories = {
    'Electronics': ['Smartphone', 'Laptop', 'Headphones', 'Charger', 'Power Bank', 'Tablet', 'Smart Watch', 'USB Cable'],
    'Clothing': ['T-Shirt', 'Jeans', 'Saree', 'Kurta', 'Shirt', 'Trousers', 'Dress', 'Jacket'],
    'Home & Kitchen': ['Mixer Grinder', 'Pressure Cooker', 'Microwave', 'Utensils Set', 'Bedsheet', 'Pillow', 'Towel'],
    'Books': ['Novel', 'Self-Help', 'Technical Book', 'Comic', 'Magazine', 'Reference Book'],
    'Beauty': ['Face Cream', 'Shampoo', 'Soap', 'Deodorant', 'Lipstick', 'Face Wash'],
    'Sports': ['Cricket Bat', 'Yoga Mat', 'Dumbbells', 'Shoes', 'T-Shirt', 'Water Bottle']
}

# Generate Products (1000s)
print("Generating Products...")
products = []
product_id = 1
for category, items in categories.items():
    for item in items:
        for i in range(120):  # ~1000 products across categories
            products.append({
                'product_id': product_id,
                'product_name': f"{item} {fake.word()}",
                'category': category,
                'price': round(np.random.lognormal(mean=np.log(500), sigma=1.5), 2),
                'stock_quantity': random.randint(10, 1000)
            })
            product_id += 1

df_products = pd.DataFrame(products)
df_products.to_csv('products.csv', index=False)
print(f"Products: {len(df_products)} records created")

# Generate Customers (1000s)
print("Generating Customers...")
customers = []
for i in range(5000):
    customers.append({
        'customer_id': i + 1,
        'customer_name': fake.name(),
        'email': fake.email(), 
        'phone': fake.phone_number(),
        'city': random.choice(['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai', 'Kolkata', 'Pune', 'Ahmedabad']),
        'state': random.choice(['Maharashtra', 'Delhi', 'Karnataka', 'Telangana', 'Tamil Nadu', 'West Bengal', 'Gujarat']),
        'registration_date': fake.date_between(start_date='-2y')
    })

df_customers = pd.DataFrame(customers)
df_customers.to_csv('customers.csv', index=False)
print(f"Customers: {len(df_customers)} records created")

# Generate Orders (10000s)
print("Generating Orders...")
orders = []
base_date = datetime.now() - timedelta(days=730)
for i in range(15000):
    order_date = base_date + timedelta(days=random.randint(0, 730))
    orders.append({
        'order_id': i + 1,
        'customer_id': random.randint(1, 5000),
        'order_date': order_date.date(),
        'order_status': random.choice(['Pending', 'Confirmed', 'Shipped', 'Delivered', 'Cancelled']),
        'total_amount': round(random.uniform(500, 50000), 2)
    })

df_orders = pd.DataFrame(orders)
df_orders.to_csv('orders.csv', index=False)
print(f"Orders: {len(df_orders)} records created")

# Generate Order Items (Lakhs - 100s of 1000s)
print("Generating Order Items...")
order_items = []
item_id = 1
for order_id in df_orders['order_id']:
    num_items = random.randint(1, 5)
    for _ in range(num_items):
        product_id = random.randint(1, len(df_products))
        quantity = random.randint(1, 10)
        price = df_products[df_products['product_id'] == product_id]['price'].values[0]
        
        order_items.append({
            'order_item_id': item_id,
            'order_id': order_id,
            'product_id': product_id,
            'quantity': quantity,
            'unit_price': price,
            'total_price': round(quantity * price, 2)
        })
        item_id += 1

df_order_items = pd.DataFrame(order_items)
df_order_items.to_csv('order_items.csv', index=False)
print(f"Order Items: {len(df_order_items)} records created")

print("\n✓ All 4 CSV files created successfully!")
print(f"  - products.csv: {len(df_products)} products")
print(f"  - customers.csv: {len(df_customers)} customers")
print(f"  - orders.csv: {len(df_orders)} orders")
print(f"  - order_items.csv: {len(df_order_items)} order items")