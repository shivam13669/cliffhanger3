#!/usr/bin/env python3
import os
import re
from pathlib import Path

# The CSS and JavaScript code to inject
DISABLE_SCRIPT = '''	<style>
		a,
		button,
		[role="button"],
		[onclick],
		.elementor-item,
		.elementor-button,
		.elementor-cta,
		.rs-layer,
		.ekit-element-link,
		.menu-item a,
		.elementor-nav-menu a,
		.elementor-sub-item {
			pointer-events: none !important;
			cursor: not-allowed !important;
		}
	</style>

	<script>
		document.addEventListener('DOMContentLoaded', function() {
			const disableClickHandler = function(e) {
				e.preventDefault();
				e.stopPropagation();
				return false;
			};

			const elements = document.querySelectorAll('a, button, [role="button"], [onclick], .elementor-item, .elementor-button, .elementor-cta, .rs-layer, .ekit-element-link, .menu-item a, .elementor-nav-menu a, .elementor-sub-item');

			elements.forEach(element => {
				element.addEventListener('click', disableClickHandler, true);
				element.addEventListener('mousedown', disableClickHandler, true);
				element.addEventListener('touchstart', disableClickHandler, true);
				element.removeAttribute('href');
				element.removeAttribute('onclick');
				element.setAttribute('disabled', 'disabled');
			});

			document.addEventListener('click', disableClickHandler, true);
		});

		if (document.readyState === 'loading') {
			document.addEventListener('DOMContentLoaded', function() {
				const elements = document.querySelectorAll('a, button, [role="button"], [onclick], .elementor-item, .elementor-button, .elementor-cta, .rs-layer, .ekit-element-link, .menu-item a, .elementor-nav-menu a, .elementor-sub-item');
				elements.forEach(element => {
					element.addEventListener('click', function(e) {
						e.preventDefault();
						e.stopPropagation();
						return false;
					}, true);
				});
			});
		}
	</script>
'''

def process_html_file(filepath):
    """Add disable script to HTML file if not already present"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already processed
        if 'disable-clicks-script' in content or 'pointer-events: none !important;' in content:
            return False
        
        # Check if it's an HTML file with body tag
        if '</body>' not in content:
            return False
        
        # Insert the script before </body>
        modified_content = content.replace(
            '</body>',
            DISABLE_SCRIPT + '\n</body>'
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(modified_content)
        
        return True
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

def main():
    # Find all index.html files
    html_files = Path('.').rglob('index.html')
    count = 0
    
    for filepath in html_files:
        # Skip certain directories
        if 'wp-content' in str(filepath) or 'wp-includes' in str(filepath):
            continue
        
        if process_html_file(str(filepath)):
            count += 1
            print(f"Updated: {filepath}")
    
    print(f"\nTotal files updated: {count}")

if __name__ == '__main__':
    main()
