#!/usr/bin/env python3
import os
import glob
import re

# Define replacement patterns
replacements = [
    # Social media links - disable them
    ('href="https://www.facebook.com/Manuadventuresindia"', 'href="#"'),
    ('href="https://www.instagram.com/manu_adventures_india/"', 'href="#"'),
    ('href="https://twitter.com/manuadventures"', 'href="#"'),
    ('href="https://www.youtube.com/c/ManuHiyunriManuAdventures/about"', 'href="#"'),
    
    # Addresses - replace both variants
    ('Leta Village, near Bhagsu nag Dharamshala, Himachal Pradesh 176219', '123 Main Street, Sample City 12345'),
    ('Bhagsu Nag, Dharamshala, Himachal Pradesh 176219', '123 Main Street, Sample City 12345'),
    
    # Email addresses in href
    ('href="mailto:info@manuadventures.in"', 'href="mailto:you@example.com"'),
    ('href="mailto:manuadventures@gmail.com"', 'href="mailto:you@example.com"'),
    
    # Email addresses as plain text
    ('info@manuadventures.in', 'you@example.com'),
    ('manuadventures@gmail.com', 'you@example.com'),
    
    # Phone numbers
    ('+91-9736871426', '+91-1234567891'),
    
    # Company names
    ('Manu Adventures India', 'Cliffhanger India'),
    ('MANU ADVENTURES INDIA', 'CLIFFHANGER INDIA'),
]

# Find all HTML files
html_files = glob.glob('**/*.html', recursive=True)

# Exclude wp-json and wp-content directories
html_files = [f for f in html_files if 'wp-json' not in f and 'wp-content' not in f]

print(f"Found {len(html_files)} HTML files to update")

updated_count = 0
for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        original_content = content
        
        # Apply all replacements
        for old, new in replacements:
            content = content.replace(old, new)
        
        # Only write if content changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            updated_count += 1
            print(f"✓ Updated: {filepath}")
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")

print(f"\n{updated_count} files updated successfully")
