def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and attendee list.
    
    Args:
        template (str): The template string with placeholders
        attendees (list): List of dictionaries containing attendee information
    """
    if not isinstance(template, str):
        print(f"Error: Template must be a string, got {type(template).__name__} instead.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print(f"Error: Attendees must be a list of dictionaries, got {type(attendees).__name__} instead.")
        return
    
    if not template:
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    for idx, attendee in enumerate(attendees, start=1):
        processed_template = template
        
        placeholders = ['name', 'event_title', 'event_date', 'event_location']
        for placeholder in placeholders:
            placeholder_pattern = '{' + placeholder + '}'
            placeholder_value = attendee.get(placeholder, "N/A")
            processed_template = processed_template.replace(placeholder_pattern, str(placeholder_value))
        
        output_filename = f"output_{idx}.txt"
        with open(output_filename, 'w') as output_file:
            output_file.write(processed_template)
