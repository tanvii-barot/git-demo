import os
from dotenv import load_dotenv
from routes import app

load_dotenv()

def main():
    port = int(os.getenv("PORT", 4999))
    return app.run(debug=True, port=port)

if __name__ == '__main__':
    main()
