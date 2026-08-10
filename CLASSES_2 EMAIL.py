# Import Python's built-in datetime library to handle dates and times
import datetime

# Define the Email class to represent a single email message
class Email:
    # The setup method that runs whenever a new email is created
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender          # Stores who sent the email (a User object)
        self.receiver = receiver      # Stores who gets the email (a User object)
        self.subject = subject        # Stores the email's subject line text
        self.body = body              # Stores the main message text of the email
        self.timestamp = datetime.datetime.now()  # Saves the exact date and time it was made
        self.read = False             # New emails start as unread (False)

    # A simple method to change the email status to read
    def mark_as_read(self):
        self.read = True              # Changes unread (False) to read (True)

    # Method to print out everything inside the email nicely
    def display_full_email(self):
        self.mark_as_read()           # Automatically mark it read when viewed
        print('\n--- Email ---')      # Prints a top visual divider line
        print(f'From: {self.sender.name}')      # Prints the sender's name
        print(f'To: {self.receiver.name}')      # Prints the receiver's name
        print(f'Subject: {self.subject}')       # Prints the subject line
        # Prints the time formatted as Year-Month-Day Hour:Minute
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')             # Prints the actual message text
        print('------------\n')     # Prints a bottom visual divider line

    # Controls how the email looks when printed as a quick one-line summary
    def __str__(self):
        # Pick the word 'Read' or 'Unread' based on the self.read true/false status
        status = 'Read' if self.read else 'Unread'
        # Return a neatly formatted text string showing status, sender, subject, and time
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

# Define the User class to represent a person using the email system
class User:
    # The setup method that runs whenever a new user is created
    def __init__(self, name):
        self.name = name              # Stores the person's name
        self.inbox = Inbox()          # Gives this person their own brand new Inbox object

    # Method for this user to send an email to someone else
    def send_email(self, receiver, subject, body):
        # Create a new Email object, setting 'self' (this user) as the sender
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        # Put that new email directly into the receiver's inbox list
        receiver.inbox.receive_email(email)
        # Print a quick text message confirming the email was sent
        print(f'Email sent from {self.name} to {receiver.name}!\n')

    # Method for the user to check their own inbox list
    def check_inbox(self):
        print(f"\n{self.name}'s Inbox:") # Prints a header like "Ramy's Inbox:"
        self.inbox.list_emails()      # Calls the inbox's method to print the email list

    # Method for the user to read a specific email using its list number
    def read_email(self, index):
        self.inbox.read_email(index)  # Passes the list number down to the inbox object

    # Method for the user to delete a specific email using its list number
    def delete_email(self, index):
        self.inbox.delete_email(index) # Passes the list number down to the inbox object

# Define the Inbox class to hold and manage a collection of emails
class Inbox:
    # The setup method that runs whenever a new inbox is created
    def __init__(self):
        self.emails = []              # Starts with an empty Python list to store emails

    # Adds an incoming email object into the inbox list
    def receive_email(self, email):
        self.emails.append(email)     # Appends the email to the end of the list

    # Prints a numbered list of all emails currently in the inbox
    def list_emails(self):
        # If the emails list has nothing in it
        if not self.emails:
            print('Your inbox is empty.\n') # Tell the user it's empty
            return                    # Stop right here and exit the method
        print('\nYour Emails:')       # Print a list header
        # Loop through the list, giving us a counting number (i) starting at 1
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')    # Prints something like: 1. [Unread] From: Tory...

    # Method to process reading an email from the inbox list
    def read_email(self, index):
        # Check if there are no emails to read
        if not self.emails:
            print('Inbox is empty.\n') # Show empty warning message
            return                    # Stop and exit
        actual_index = index - 1      # Change user's 1-based number to Python's 0-based position
        # Check if the calculated position number is out of bounds (invalid)
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n') # Show error message
            return                    # Stop and exit
        # If valid, find that email in the list and run its display method
        self.emails[actual_index].display_full_email()

    # Method to process deleting an email from the inbox list
    def delete_email(self, index):
        # Check if there are no emails to delete
        if not self.emails:
            print('Inbox is empty.\n') # Show empty warning message
            return                    # Stop and exit
        actual_index = index - 1      # Change user's 1-based number to Python's 0-based position
        # Check if the calculated position number is out of bounds (invalid)
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n') # Show error message
            return                    # Stop and exit
        del self.emails[actual_index] # Use 'del' keyword to remove that item from the list
        print('Email deleted.\n')     # Print a success confirmation message

# The main function where we run our simulation steps
def main():
    tory = User('Tory')               # Create a User object named Tory
    ramy = User('Ramy')               # Create a User object named Ramy        
    
    # Tory sends a message to Ramy
    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
    # Ramy sends a reply back to Tory
    ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')
    
    ramy.check_inbox()                # Ramy looks at his list of incoming messages
    ramy.read_email(1)                # Ramy opens up and reads email number 1
    ramy.delete_email(1)              # Ramy deletes email number 1 from his inbox
    ramy.check_inbox()                # Ramy checks his inbox list again to verify it's gone

# Check if this specific script file is the one being directly clicked/run
if __name__ == '__main__':
    main()                            # Start the simulation by running the main function
