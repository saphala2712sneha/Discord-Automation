# test_send_image.py
from user import User
from time import sleep

with open('account.txt') as f:
    email = f.readline().strip()
    password = f.readline().strip()

user = User(email, password, 'https://discord.com/login')

# Log in and wait for the page to load
user.login()
print("Waiting for the page to load...")
sleep(25)  # Adjust this if needed

# Choose the chat with the specific friend
friend_name = 'Sanki'  # Replace with the actual friend’s name
print(f"Choosing chat with {friend_name}...")
user.choose(friend_name)

# Send an image to the selected friend
file_path = r"C:\Users\SNEHA SAPHALA\Downloads\discord-automation-main\discord-automation-main\Mini.jpg"
user.send_image_js(file_path)
