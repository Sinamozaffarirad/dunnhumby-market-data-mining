from django.db import connection
import traceback

try:
    with connection.cursor() as cursor:
        cursor.execute("SELECT @@VERSION")
        result = cursor.fetchone()
        print("✅ Database Connection Successful!")
        print(f"SQL Server Version: {result[0][:50]}...")
except Exception as e:
    print("❌ Database Connection Failed!")
    print(f"Error: {e}")
    traceback.print_exc()