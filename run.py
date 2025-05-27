# run.py
from config.config import Config
import uvicorn

if __name__ == "__main__":
    uvicorn.run("app:app", host=Config.HOST, port=Config.PORT, reload=True)
