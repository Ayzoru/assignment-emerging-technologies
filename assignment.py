import requests

# Webex API link
webex_api_url = 'https://webexapis.com/v1'

def main():
    # Welcome message and prompt for Webex token
    print("\n-------------------------------------------")
    print("Welcome to My Webex Navigator Application!")
    print("-------------------------------------------")
    token = input("Enter your Webex token: ")
    
    # Main menu loop, 6 options for user to interact with
    while True:
        print("\nOption 0: Test connection")
        print("Option 1: Display user information")
        print("Option 2: Display rooms")
        print("Option 3: Create a room")
        print("Option 4: Send message to a room")
        print("Option 5: Exit")
        option = input("Choose an option: ")
        
        # If, else if based on user input 
        if option == "0":
            test_connection(token)
        elif option == "1":
            display_user_info(token)
        elif option == "2":
            display_rooms(token)
        elif option == "3":
            create_room(token)
        elif option == "4":
            send_message(token)
        elif option == "5":
            break  # Exit the loop and end the program
        else:
            print("Invalid option. Please try again.")

def test_connection(token):
    try:
        # Test connection with Webex server
        url = webex_api_url + '/people/me'
        headers = {'Authorization': 'Bearer ' + token}
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for any errors in the response
        print("Webex Successfully Connected!")
    except requests.exceptions.RequestException as e:
        # Handle connection errors
        print(f"Failed to connect to the server. Please try again. {e}")

def display_user_info(token):
    # Display user information
    try:
        url = webex_api_url + '/people/me'
        headers = {'Authorization' : 'Bearer ' + token}
        response = requests.get(url, headers=headers)
        response.raise_for_status ()  # Check for any errors in the response

        displayinfo = response.json()
        print("\n-------------------------------------")
        print("Obtained User Information Successfully")
        print("-------------------------------------")
        print("Displayed Name: " + displayinfo["displayName"])
        print("Nickname: " + displayinfo["nickName"])
        print("Email: " + displayinfo["emails"][0])
    except requests.exceptions.RequestException as e:
        # Handle connection errors
        print(f"Failed to connect to the server. Please try again. {e}")


def display_rooms(token):
    # Display room information
    try:
        url = webex_api_url + '/rooms'
        headers = {'Authorization' : 'Bearer ' + token}
        response = requests.get(url, headers=headers)
        response.raise_for_status ()  # Check for any errors in the response

        displayrooms = response.json()['items'][:6]  # Limit to first 6 rooms
        for room in displayrooms:
            print("\n--------------------")
            print("Room Information")
            print("--------------------")
            print("Room ID: " + room["id"])
            print("Room Title: " + room["title"])
            print("Date Created: " + room["created"])
            print("Last Activity: " + room["lastActivity"])
    except requests.exceptions.RequestException as e:
             # Handle connection errors
             print(f"Failed to connect to the server. Please try again. {e}")

        

def create_room(token):
    # Create a new room
    try:
        url = webex_api_url + '/rooms'
        headers = {'Authorization' : 'Bearer ' + token, 'Content-Type': 'application/json'}
        room_title = input("Please enter new room title: ")
        title_data = {'title': room_title}
        response = requests.post(url, headers=headers, json=title_data)
        response.raise_for_status()  # Check for any errors in the response
        print("\n--------------------------")
        print(" Room Successfully Created ")
        print("--------------------------")
    except requests.exceptions.RequestsException as e:
        # Handle connection errors
        print(f"Failed to connect to the server. Please try again. {e}")

def send_message(token):
    # Send a message to a room
    try:
        url = webex_api_url + '/rooms'
        headers = {'Authorization' : 'Bearer ' + token}
        response = requests.get(url, headers=headers)
        response.raise_for_status ()  # Check for any errors in the response

        displayrooms = response.json()['items']
        for i, room in enumerate(displayrooms, start=1):
            print(f"{i}. {room['title']}")
        
        room_number = int(input("Enter room number: "))
        message = input("Type the message you want to send: ")

        selected_room_id = displayrooms[room_number - 1]['id']
        url = webex_api_url + '/messages'
        headers = {'Authorization' : 'Bearer ' + token, 'Content-Type': 'application/json'}
        message_data = {'roomId': selected_room_id, 'text': message}
        response = requests.post(url, headers=headers, json=message_data)
        response.raise_for_status ()  # Check for any errors in the response
        print("\n-----------------------------------")
        print("Message has been sent successfully!")
        print("-----------------------------------")
    except requests.exceptions.RequestsException as e:
            # Handle connection errors
            print(f"Failed to connect to the server. Please try again. {e}")

if __name__ == "__main__":
    main()

