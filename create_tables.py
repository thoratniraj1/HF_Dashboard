from db_connection import engine, Base

# Import ALL models before create_all
from models import User

# Create tables only if they don't exist
Base.metadata.create_all(bind=engine)

print("Table creation completed")