import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

FS_EMAIL = os.environ["FS_EMAIL"]
FS_PASSWORD = os.environ["FS_PASSWORD"]

BASE_URL = "https://www.fourseasons.com"
ITINERARY_URL = f"{BASE_URL}/profile/api/itinerary/"


def login(session: requests.Session) -> None:
    # TODO: reverse-engineer the login endpoint and payload
    raise NotImplementedError


def get_booking_ids(session: requests.Session) -> list[str]:
    # TODO: reverse-engineer the endpoint that lists current bookings
    raise NotImplementedError


def get_itinerary(session: requests.Session, booking_id: str) -> dict:
    resp = session.get(ITINERARY_URL, params={"bookingId": booking_id})
    resp.raise_for_status()
    return resp.json()


def main():
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0"})

    login(session)
    booking_ids = get_booking_ids(session)

    for booking_id in booking_ids:
        itinerary = get_itinerary(session, booking_id)
        print(json.dumps(itinerary, indent=2))
        # TODO: convert itinerary to .ics and commit to repo


if __name__ == "__main__":
    main()
