#!/usr/bin/env python3
"""
Test error handling for build_arxiv.py
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from build_arxiv import fetch_arxiv_papers, parse_arxiv_xml
import requests

def test_network_error():
    """Test handling of network errors"""
    print("Testing network error handling...")
    
    # Test with invalid URL
    try:
        result = fetch_arxiv_papers("cs.INVALID", max_results=1)
        if result is None:
            print("✓ Network error handled correctly")
            return True
        else:
            print("✗ Network error not handled properly")
            return False
    except Exception as e:
        print(f"✗ Exception during network error test: {e}")
        return False

def test_xml_parsing_error():
    """Test handling of XML parsing errors"""
    print("Testing XML parsing error handling...")
    
    # Test with invalid XML
    invalid_xml = "<invalid><xml></invalid>"
    try:
        result = parse_arxiv_xml(invalid_xml, "cs.AI")
        if result == []:
            print("✓ XML parsing error handled correctly")
            return True
        else:
            print("✗ XML parsing error not handled properly")
            return False
    except Exception as e:
        print(f"✗ Exception during XML parsing test: {e}")
        return False

def test_empty_xml():
    """Test handling of empty XML"""
    print("Testing empty XML handling...")
    
    try:
        result = parse_arxiv_xml("", "cs.AI")
        if result == []:
            print("✓ Empty XML handled correctly")
            return True
        else:
            print("✗ Empty XML not handled properly")
            return False
    except Exception as e:
        print(f"✗ Exception during empty XML test: {e}")
        return False

def main():
    """Run all error handling tests"""
    print("=== Error Handling Tests ===")
    
    tests = [
        test_network_error,
        test_xml_parsing_error,
        test_empty_xml
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"=== Results: {passed}/{total} tests passed ===")
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)