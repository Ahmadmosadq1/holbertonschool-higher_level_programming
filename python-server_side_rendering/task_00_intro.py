# Main file content
import os
import re

def generate_invitations(template_content, attendees):
    
    try:
        if not isinstance(template_content, str):
            print("Error: Template must be a string")
            return
        
        if not isinstance(attendees, list) or not all(isinstance(name, dict) for name in attendees):
            print("Error: Atensees must be a list of dictionaries")
            return
    
        if template_content.strip == "":
            print("Error: content is empty")
            return
        
        if not attendees:
            print("error: no data provided")
            return
        # Read the template from a file
        for index, person in enumerate(attendees, start = 1):
            message = template_content
            for pacholder in ["name", "event_title", "event_date", "event_location"]:
                value = person.get(pacholder) or "N/A"
                message = message.replace(f"{{{pacholder}}}", str(value))
                output_file = f"output_{index}.txt"
            if os.path.exists(output_file):
                print("File already exists")
                continue


            with open(output_file, 'w') as file:
                file.write(message)
    
    except Exception as error:
        print(f"error: {error}")

attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

with open('template.txt', 'r') as file:
    template_content = file.read()
generate_invitations(template_content, attendees)

