import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# GitHub username
username = 'ibrahimtosun18'

# GitHub API URL to get contribution data
api_url = f'https://api.github.com/users/{username}/events/public'

# Get events from the last 60 days
end_date = datetime.now()
start_date = end_date - timedelta(days=60)

# Fetch the data from GitHub API
response = requests.get(api_url)
events = response.json()

# Filter events within the last 60 days
filtered_events = [event for event in events if datetime.strptime(event['created_at'], '%Y-%m-%dT%H:%M:%SZ') >= start_date]

# Count contributions per day
contributions = {}
for event in filtered_events:
    date = event['created_at'][:10]
    if date in contributions:
        contributions[date] += 1
    else:
        contributions[date] = 1

# Prepare data for plotting
dates = [start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)]
counts = [contributions.get(date.strftime('%Y-%m-%d'), 0) for date in dates]

# Plotting the graph
plt.figure(figsize=(10, 5))
plt.plot(dates, counts, marker='o', linestyle='-', color='b')
plt.fill_between(dates, counts, color='skyblue', alpha=0.4)
plt.title(f'GitHub Activity for {username} (Last 60 Days)')
plt.xlabel('Date')
plt.ylabel('Contributions')
plt.xticks(rotation=45)
plt.tight_layout()

# Save the graph
plt.savefig('activity_graph.png')
