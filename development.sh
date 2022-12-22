export FLASK_APP=app
export FLASK_ENV=development
source venv/bin/activate
# python3 init_db.py
#DB Should already be initialized
flask run

deactivate