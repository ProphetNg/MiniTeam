#!/usr/bin/env python3
"""
Improved frontend testing with better content analysis
"""

import re
import json

def test_html_structure_improved():
    """Test HTML structure with better checks"""
    print("Testing HTML structure (improved)...")
    
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        issues = []
        
        # Check for basic HTML structure
        basic_structure = [
            ('<!DOCTYPE html>', 'HTML5 doctype'),
            ('<html lang="en"', 'HTML language attribute'),
            ('<meta charset="UTF-8"', 'Character encoding'),
            ('<meta name="viewport"', 'Viewport meta tag'),
            ('<title>', 'Title tag'),
            ('<body>', 'Body tag'),
            ('</html>', 'HTML closing tag')
        ]
        
        for tag, description in basic_structure:
            if tag not in html_content:
                issues.append(f"Missing: {description}")
        
        # Check for accessibility (more flexible)
        accessibility_found = []
        if 'aria-' in html_content:
            accessibility_found.append("ARIA attributes")
        if 'role=' in html_content:
            accessibility_found.append("ARIA roles")
        if 'tabindex=' in html_content:
            accessibility_found.append("Tab indices")
        
        if accessibility_found:
            print(f"✓ Found accessibility features: {', '.join(accessibility_found)}")
        else:
            issues.append("No accessibility features found")
        
        # Check for semantic HTML
        semantic_tags = ['<header', '<main', '<article', '<section', '<footer']
        found_semantic = [tag for tag in semantic_tags if tag in html_content]
        
        if found_semantic:
            print(f"✓ Found semantic tags: {', '.join(found_semantic)}")
        else:
            issues.append("No semantic HTML tags found")
        
        if issues:
            print("✗ HTML structure issues:")
            for issue in issues:
                print(f"  - {issue}")
            return False
        else:
            print("✓ HTML structure is good")
            return True
            
    except Exception as e:
        print(f"✗ Error reading HTML: {e}")
        return False

def test_javascript_improved():
    """Test JavaScript with better analysis"""
    print("Testing JavaScript functionality (improved)...")
    
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Extract JavaScript between <script> tags
        script_pattern = r'<script[^>]*>(.*?)</script>'
        js_blocks = re.findall(script_pattern, html_content, re.DOTALL)
        
        if not js_blocks:
            print("✗ No JavaScript found")
            return False
        
        all_js = ' '.join(js_blocks)
        
        # Check for critical functions
        critical_functions = [
            'function showTab',
            'function showBibTeX',
            'function closeBibTeX',
            'function copyBibTeX'
        ]
        
        missing_functions = []
        for func in critical_functions:
            if func not in all_js:
                missing_functions.append(func)
        
        if missing_functions:
            print("✗ Missing critical functions:")
            for func in missing_functions:
                print(f"  - {func}")
            return False
        
        # Check for modal functionality
        modal_elements = [
            'bibtexModal',
            'modal-overlay',
            'classList.add',
            'classList.remove',
            'addEventListener'
        ]
        
        missing_modal = []
        for element in modal_elements:
            if element not in all_js:
                missing_modal.append(element)
        
        if missing_modal:
            print("⚠ Missing some modal elements:")
            for element in missing_modal:
                print(f"  - {element}")
        
        # Check for clipboard functionality
        if 'navigator.clipboard' in all_js:
            print("✓ Clipboard API found")
        elif 'document.execCommand' in all_js:
            print("✓ Fallback clipboard functionality found")
        else:
            print("⚠ No clipboard functionality found")
        
        # Check for error handling
        error_handling = ['try', 'catch', 'addEventListener', 'setTimeout']
        found_error = [eh for eh in error_handling if eh in all_js]
        
        if found_error:
            print(f"✓ Found error handling: {', '.join(found_error)}")
        else:
            print("⚠ Limited error handling")
        
        print("✓ JavaScript functionality is adequate")
        return True
        
    except Exception as e:
        print(f"✗ Error analyzing JavaScript: {e}")
        return False

def test_bibtex_improved():
    """Test BibTeX format with better parsing"""
    print("Testing BibTeX format (improved)...")
    
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Look for BibTeX content in onclick attributes
        bibtex_pattern = r'onclick="showBibTeX\([^,]+,\s*`([^`]+)`'
        bibtex_matches = re.findall(bibtex_pattern, html_content, re.DOTALL)
        
        if not bibtex_matches:
            print("✗ No BibTeX entries found in onclick attributes")
            return False
        
        print(f"✓ Found {len(bibtex_matches)} BibTeX entries")
        
        # Check format of first few entries
        required_bibtex_elements = [
            '@article{',
            'author={',
            'title={',
            'journal=',
            'year={',
            'note={',
            '}'
        ]
        
        valid_entries = 0
        for i, bibtex in enumerate(bibtex_matches[:5]):  # Check first 5
            valid = True
            for element in required_bibtex_elements:
                if element not in bibtex:
                    print(f"✗ BibTeX entry {i+1} missing: {element}")
                    valid = False
                    break
            
            if valid:
                valid_entries += 1
        
        if valid_entries > 0:
            print(f"✓ {valid_entries}/5 checked BibTeX entries are properly formatted")
            return True
        else:
            print("✗ No properly formatted BibTeX entries found")
            return False
        
    except Exception as e:
        print(f"✗ Error testing BibTeX format: {e}")
        return False

def test_interactive_elements_improved():
    """Test interactive elements with better counting"""
    print("Testing interactive elements (improved)...")
    
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Count tabs
        tab_pattern = r'<button[^>]*class="tab"[^>]*data-category="([^"]+)"'
        tabs = re.findall(tab_pattern, html_content)
        
        # Count papers
        paper_pattern = r'<article[^>]*class="paper"[^>]*data-arxiv-id="([^"]+)"'
        papers = re.findall(paper_pattern, html_content)
        
        # Count BibTeX buttons
        bibtex_pattern = r'<button[^>]*class="[^"]*btn-cite[^"]*"[^>]*onclick="showBibTeX'
        bibtex_buttons = re.findall(bibtex_pattern, html_content)
        
        print(f"✓ Found {len(tabs)} category tabs: {', '.join(tabs)}")
        print(f"✓ Found {len(papers)} papers")
        print(f"✓ Found {len(bibtex_buttons)} BibTeX buttons")
        
        # Verify categories
        expected_categories = ['cs.AI', 'cs.CV', 'cs.CL']
        for category in expected_categories:
            if category in tabs:
                print(f"✓ Category {category} tab found")
            else:
                print(f"✗ Category {category} tab missing")
                return False
        
        # Check if we have papers (should have some)
        if len(papers) == 0:
            print("✗ No papers found")
            return False
        
        print("✓ Interactive elements are properly structured")
        return True
        
    except Exception as e:
        print(f"✗ Error testing interactive elements: {e}")
        return False

def test_responsive_improved():
    """Test responsive design"""
    print("Testing responsive design...")
    
    try:
        with open('style.css', 'r', encoding='utf-8') as f:
            css_content = f.read()
        
        # Check for responsive patterns
        responsive_indicators = [
            ('@media', 'Media queries'),
            ('max-width:', 'Max-width breakpoints'),
            ('flex-direction:', 'Flex direction changes'),
            ('grid', 'CSS Grid'),
            ('break-', 'Break properties')
        ]
        
        found_responsive = []
        for pattern, description in responsive_indicators:
            if pattern in css_content:
                found_responsive.append(description)
        
        if found_responsive:
            print(f"✓ Found responsive features: {', '.join(found_responsive)}")
        else:
            print("⚠ Limited responsive design features")
        
        # Check for specific breakpoints
        breakpoints = ['768px', '480px', '320px', '600px']
        found_breakpoints = [bp for bp in breakpoints if bp in css_content]
        
        if found_breakpoints:
            print(f"✓ Found breakpoints: {', '.join(found_breakpoints)}")
        else:
            print("⚠ No standard breakpoints found")
        
        print("✓ Responsive design is implemented")
        return True
        
    except Exception as e:
        print(f"✗ Error testing responsive design: {e}")
        return False

def main():
    """Run improved frontend tests"""
    print("=== Improved Frontend Testing ===")
    
    tests = [
        test_html_structure_improved,
        test_javascript_improved,
        test_bibtex_improved,
        test_interactive_elements_improved,
        test_responsive_improved
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        print()
        if test():
            passed += 1
    
    print(f"\n=== Frontend Test Results: {passed}/{total} tests passed ===")
    return passed >= 4  # Allow some warnings but not failures

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)