import requests

def fetch_events_on_date(year, month, day):
    url = f"https://history.muffinlabs.com/date/{month}/{day}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        events = data["data"]["Events"]
        events_in_year = [event for event in events if event["year"] == year]
        return events_in_year
    else:
        return None

# ANSI header
print("\033[1;34;40mTimeInfo\033[0m")

search_count = 0
while search_count < 5:
    print("\nWhich date and year would you like to search?")
    year = input("Enter the year: ")
    month = input("Enter the month (1-12): ")
    day = input("Enter the day (1-31): ")

    events = fetch_events_on_date(year, month, day)

    if events:
        print(f"\nHistorical events on {month}-{day}-{year}:")
        for event in events:
            print(f"{event['year']}: {event['text']}")
    else:
        print("No events found for the given date and year.")

    search_again = input("\nWould you like to search again? (y/n): ")
    if search_again.lower() != 'y':
        break
    search_count += 1
