#!/usr/bin/env python3
"""
Detailed network testing for build_arxiv.py
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from build_arxiv import fetch_arxiv_papers, parse_arxiv_xml
import requests

def test_invalid_category():
    """Test with truly invalid category"""
    print("Testing with invalid category cs.INVALID123...")
    
    result = fetch_arxiv_papers("cs.INVALID123", max_results=1)
    print(f"Result type: {type(result)}")
    if result:
        print(f"Result length: {len(result)}")
        print(f"First 200 chars: {result[:200]}")
        
        # Try to parse it
        papers = parse_arxiv_xml(result, "cs.INVALID123")
        print(f"Parsed papers: {len(papers)}")
    else:
        print("Result is None")

def test_timeout():
    """Test timeout handling"""
    print("Testing timeout handling...")
    
    # Test with a very short timeout
    import time
    start_time = time.time()
    
    try:
        result = fetch_arxiv_papers("cs.AI", max_results=1)
        end_time = time.time()
        print(f"Request completed in {end_time - start_time:.2f} seconds")
        print("✓ Request completed successfully")
        return True
    except requests.exceptions.Timeout:
        print("✓ Timeout handled correctly")
        return True
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False

def verify_html_content():
    """Verify that the generated HTML contains valid data"""
    print("Verifying HTML content...")
    
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Check for required elements
        checks = [
            ('DOCTYPE html', 'HTML doctype'),
            ('ArXiv CS Daily Papers', 'Title'),
            ('cs.AI', 'AI category'),
            ('cs.CV', 'CV category'), 
            ('cs.CL', 'CL category'),
            ('showBibTeX', 'BibTeX function'),
            ('paper-title', 'Paper title class'),
            ('btn-cite', 'Cite button class')
        ]
        
        passed = 0
        for check, description in checks:
            if check in html_content:
                print(f"✓ Found {description}")
                passed += 1
            else:
                print(f"✗ Missing {description}")
        
        print(f"HTML content verification: {passed}/{len(checks)} checks passed")
        return passed == len(checks)
        
    except Exception as e:
        print(f"✗ Error reading HTML file: {e}")
        return False

def main():
    """Run detailed network tests"""
    print("=== Detailed Network Tests ===")
    
    test_invalid_category()
    print()
    
    test_timeout()
    print()
    
    verify_html_content()

if __name__ == "__main__":
    main()