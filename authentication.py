
from google_auth import get_calendar_service

print("Starting Google Calendar authentication...")

service = get_calendar_service()

# Test access by retrieving calendar events
events_result = service.events().list(
    calendarId="primary",
    maxResults=5,
    singleEvents=True
).execute()

print("\nGoogle Calendar authentication successful!")
print("Calendar API connection is working!")

events = events_result.get("items", [])

print(f"Retrieved {len(events)} events.")
