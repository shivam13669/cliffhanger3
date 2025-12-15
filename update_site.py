#!/usr/bin/env python3
import os
import glob

# Define replacements
replacements = [
    # Social media links
    ('href="https://www.facebook.com/Manuadventuresindia"', 'href="#"'),
    ('href="https://www.instagram.com/manu_adventures_india/"', 'href="#"'),
    ('href="https://twitter.com/manuadventures"', 'href="#"'),
    ('href="https://www.youtube.com/c/ManuHiyunriManuAdventures/about"', 'href="#"'),
    
    # Addresses
    ('Leta Village, near Bhagsu nag Dharamshala, Himachal Pradesh 176219', '123 Main Street, Sample City 12345'),
    ('Bhagsu Nag, Dharamshala, Himachal Pradesh 176219', '123 Main Street, Sample City 12345'),
    
    # Emails (href)
    ('href="mailto:info@manuadventures.in"', 'href="mailto:you@example.com"'),
    ('href="mailto:manuadventures@gmail.com"', 'href="mailto:you@example.com"'),
    
    # Emails (text)
    ('info@manuadventures.in', 'you@example.com'),
    ('manuadventures@gmail.com', 'you@example.com'),
    
    # Phone
    ('+91-9736871426', '+91-1234567891'),
    
    # Brand names
    ('Manu Adventures India', 'Cliffhanger India'),
    ('MANU ADVENTURES INDIA', 'CLIFFHANGER INDIA'),
    ('Manu Adventures', 'Cliffhanger'),
    ('manuadventures', 'cliffhanger'),
]

def update_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        for old, new in replacements:
            content = content.replace(old, new)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

# Find and update all HTML files
html_files = glob.glob('**/*.html', recursive=True)
updated_count = 0

for filepath in html_files:
    # Skip wp-json and wp-content directories
    if 'wp-json' in filepath or 'wp-content' in filepath:
        continue
    
    if update_file(filepath):
        updated_count += 1
        print(f"Updated: {filepath}")

print(f"\nTotal files updated: {updated_count}")
