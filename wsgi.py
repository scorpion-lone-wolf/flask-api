# this is the entry point of our application
from app import create_app

app = create_app()

# for dev purpose run with default wsgi server else run with gunicorn
if __name__ == "__main__":
    app.run(debug=True)
