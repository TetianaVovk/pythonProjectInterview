import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("BASE_URL", "https://the-internet.herokuapp.com")
    headed: bool = os.getenv("HEADED", "0") == "1"
    trace: bool = os.getenv("TRACE", "0") == "1"
    slow_mo: int = int(os.getenv("SLOW_MO", "0"))


settings = Settings()

BASE_API_URL = os.getenv("BASE_API_URL", "https://reqres.in/api")
REQRES_API_KEY = os.getenv("REQRES_API_KEY")
REQRES_API_KEY = "reqres_2a3ce3f712e3411c9636a03deae13821"
