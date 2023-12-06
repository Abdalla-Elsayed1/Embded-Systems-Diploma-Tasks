import requests

def suggest_activity():
    activity = requests.get('https://www.boredapi.com/api/activity').json()
    for i, j in activity.items():
        print(f"The {i} is {j} ")

if __name__ == "__main__":
    while True:
        suggest_activity()
        user_input = input("Do you want another suggestion? (yes/no): ").lower()
        if user_input != 'yes':
            break

    