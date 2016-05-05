"""Run app script."""
from app import create_app
app = create_app(config='settings')
app.run(debug=True)
