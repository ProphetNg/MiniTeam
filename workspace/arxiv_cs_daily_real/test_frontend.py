#!/usr/bin/env python3
"""
Test frontend functionality by analyzing HTML and JavaScript
"""

import re
import json
from html.parser import HTMLParser

class FrontendTester(HTMLParser):
    def __init__(self):
        super().__init__()
        self.issues = []
        self.current_tag = None
        self.tabs = []
        self.papers = []
        self.bibtex_buttons = []
        
    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        attrs_dict = dict(attrs)
        
        # Check for tabs
        if tag == 'button' and 'tab' in attrs_dict.get('class', ''):
            category = attrs_dict.get('data-category')
            if category:
                self.tabs.append(category)
        
        # Check for papers
        elif tag == 'article' and 'paper' in attrs_dict.get('class', ''):
            arxiv_id = attrs_dict.get('data-arxiv-id')
            if arxiv_id:
                self.papers.append(arxiv_id)
        
        # Check for BibTeX buttons
        elif tag == 'button' and 'btn-cite' in attrs_dict.get('class', ''):
            onclick = attrs_dict.get('onclick', '')
            if 'showBibTeX' in onclick:
                self.bibtex_buttons.append(onclick)

def test_html_structure():
    """Test HTML structure for completeness"""
    print("Testing HTML structure...")
    
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        issues = []
        
        # Check for required HTML5 structure
        required_elements = [
            '<!DOCTYPE html>',
            '<html lang="en">',
            '<head>',
            '<meta charset="UTF-8">',
            '<meta name="viewport"',
            '<title>',
            '</head>',
            '<body>',
            '</body>',
            '</html>'
        ]
        
        for element in required_elements:
            if element not in html_content:
                issues.append(f"Missing required HTML element: {element}")
        
        # Check for accessibility attributes
        accessibility_checks = [
            ('aria-label', 'ARIA labels'),
            ('role=', 'ARIA roles'),
            ('tabindex=', 'Tab indices'),
            ('alt=', 'Alt attributes')
        ]
        
        for attr, description in accessibility_checks:
            if attr not in html_content:
                issues.append(f"Missing accessibility feature: {description}")
        
        if issues:
            print("✗ HTML structure issues found:")
            for issue in issues:
                print(f"  - {issue}")
            return False
        else:
            print("✓ HTML structure is valid")
            return True
            
    except Exception as e:
        print(f"✗ Error reading HTML: {e}")
        return False

def test_javascript_functionality():
    """Test JavaScript functionality by analyzing the code"""
    print("Testing JavaScript functionality...")
    
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Extract JavaScript content
        js_start = html_content.find('<script>')
        js_end = html_content.find('</script>', js_start)
        
        if js_start == -1 or js_end == -1:
            print("✗ No JavaScript found")
            return False
        
        js_content = html_content[js_start:js_end + 9]
        
        # Check for required functions
        required_functions = [
            'showTab',
            'showBibTeX',
            'closeBibTeX',
            'copyBibTeX',
            'navigator.clipboard.writeText'
        ]
        
        missing_functions = []
        for func in required_functions:
            if func not in js_content:
                missing_functions.append(func)
        
        if missing_functions:
            print("✗ Missing JavaScript functions:")
            for func in missing_functions:
                print(f"  - {func}")
            return False
        
        # Check for error handling
        error_handling_patterns = [
            'try',
            'catch',
            'addEventListener',
            'setTimeout'
        ]
        
        missing_error_handling = []
        for pattern in error_handling_patterns:
            if pattern not in js_content:
                missing_error_handling.append(pattern)
        
        if missing_error_handling:
            print("⚠ Missing error handling patterns:")
            for pattern in missing_error_handling:
                print(f"  - {pattern}")
        
        # Check for modal functionality
        modal_patterns = [
            'bibtexModal',
            'modal-overlay',
            'classList.add',
            'classList.remove'
        ]
        
        missing_modal = []
        for pattern in modal_patterns:
            if pattern not in js_content:
                missing_modal.append(pattern)
        
        if missing_modal:
            print("✗ Missing modal functionality:")
            for pattern in missing_modal:
                print(f"  - {pattern}")
            return False
        
        print("✓ JavaScript functionality is complete")
        return True
        
    except Exception as e:
        print(f"✗ Error analyzing JavaScript: {e}")
        return False

def test_bibtex_format():
    """Test BibTeX format in the HTML"""
    print("Testing BibTeX format...")
    
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Find BibTeX entries
        bibtex_pattern = r'@article\{[^}]+,\s*author=\{[^}]+\},\s*title=\{[^}]+\},\s*journal=\{[^}]+\},\s*year=\{[^}]+\},\s*note=\{[^}]+\}\}'
        
        bibtex_matches = re.findall(bibtex_pattern, html_content, re.DOTALL)
        
        if not bibtex_matches:
            print("✗ No BibTeX entries found")
            return False
        
        print(f"✓ Found {len(bibtex_matches)} BibTeX entries")
        
        # Check format of first few entries
        required_fields = ['@article{', 'author={', 'title={', 'journal={', 'year={', 'note={']
        
        for i, bibtex in enumerate(bibtex_matches[:3]):  # Check first 3
            for field in required_fields:
                if field not in bibtex:
                    print(f"✗ BibTeX entry {i+1} missing field: {field}")
                    return False
        
        print("✓ BibTeX format is correct")
        return True
        
    except Exception as e:
        print(f"✗ Error testing BibTeX format: {e}")
        return False

def test_responsive_design():
    """Test responsive design CSS"""
    print("Testing responsive design...")
    
    try:
        with open('style.css', 'r', encoding='utf-8') as f:
            css_content = f.read()
        
        # Check for responsive design patterns
        responsive_patterns = [
            '@media',
            'max-width',
            'min-width',
            'flex-direction',
            'grid',
            'break-'
        ]
        
        missing_responsive = []
        for pattern in responsive_patterns:
            if pattern not in css_content:
                missing_responsive.append(pattern)
        
        if missing_responsive:
            print("✗ Missing responsive design patterns:")
            for pattern in missing_responsive:
                print(f"  - {pattern}")
            return False
        
        # Check for mobile-specific breakpoints
        mobile_breakpoints = ['768px', '480px', '320px']
        
        found_breakpoints = []
        for bp in mobile_breakpoints:
            if bp in css_content:
                found_breakpoints.append(bp)
        
        if not found_breakpoints:
            print("✗ No mobile breakpoints found")
            return False
        
        print(f"✓ Responsive design with breakpoints: {', '.join(found_breakpoints)}")
        return True
        
    except Exception as e:
        print(f"✗ Error testing responsive design: {e}")
        return False

def count_interactive_elements():
    """Count and verify interactive elements"""
    print("Counting interactive elements...")
    
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        parser = FrontendTester()
        parser.feed(html_content)
        
        print(f"✓ Found {len(parser.tabs)} category tabs")
        print(f"✓ Found {len(parser.papers)} papers")
        print(f"✓ Found {len(parser.bibtex_buttons)} BibTeX buttons")
        
        # Verify we have papers in all categories
        expected_categories = ['cs.AI', 'cs.CV', 'cs.CL']
        for category in expected_categories:
            if category in html_content:
                print(f"✓ Category {category} present")
            else:
                print(f"✗ Category {category} missing")
                return False
        
        return True
        
    except Exception as e:
        print(f"✗ Error counting elements: {e}")
        return False

def main():
    """Run all frontend tests"""
    print("=== Frontend Testing ===")
    
    tests = [
        test_html_structure,
        test_javascript_functionality,
        test_bibtex_format,
        test_responsive_design,
        count_interactive_elements
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        print()
        if test():
            passed += 1
    
    print(f"\n=== Frontend Test Results: {passed}/{total} tests passed ===")
    return passed == total

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)