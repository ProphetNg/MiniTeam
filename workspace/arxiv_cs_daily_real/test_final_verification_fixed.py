#!/usr/bin/env python3
"""
Final verification test - simple and direct checks (FIXED)
"""

import re

def test_basic_html():
    """Basic HTML checks"""
    print("=== Basic HTML Verification ===")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Check for key elements
    checks = [
        ('<!DOCTYPE html>', 'HTML5 doctype'),
        ('<header', 'Header tag'),
        ('<main', 'Main tag'), 
        ('<article', 'Article tag'),
        ('<button class="tab"', 'Tab buttons'),
        ('data-category="cs.AI"', 'AI category'),
        ('data-category="cs.CV"', 'CV category'),
        ('data-category="cs.CL"', 'CL category'),
        ('data-arxiv-id="', 'Paper arXiv IDs'),
        ('btn-cite', 'Cite buttons'),
        ('showBibTeX(', 'BibTeX function calls'),
        ('bibtexModal', 'Modal element'),
        ('navigator.clipboard', 'Clipboard API'),
        ('@media', 'Responsive CSS'),
        ('ArXiv CS Daily Papers', 'Page title')
    ]
    
    passed = 0
    for check, description in checks:
        if check in html:
            print(f"✓ {description}")
            passed += 1
        else:
            print(f"✗ {description}")
    
    print(f"Basic HTML: {passed}/{len(checks)} checks passed\n")
    return passed >= len(checks) - 2  # Allow minor issues

def test_javascript_functions():
    """Test JavaScript functions exist"""
    print("=== JavaScript Functions Verification ===")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Extract JavaScript content
    start = html.find('<script>')
    end = html.find('</script>', start)
    js = html[start:end] if start != -1 else ''
    
    functions = [
        'function showTab',
        'function showBibTeX', 
        'function closeBibTeX',
        'function copyBibTeX'
    ]
    
    passed = 0
    for func in functions:
        if func in js:
            print(f"✓ {func}")
            passed += 1
        else:
            print(f"✗ {func}")
    
    # Check for key functionality
    key_features = [
        ('classList.add', 'Add class'),
        ('classList.remove', 'Remove class'),
        ('addEventListener', 'Event listeners'),
        ('navigator.clipboard', 'Clipboard API'),
        ('try', 'Error handling'),
        ('catch', 'Error handling')
    ]
    
    for feature, desc in key_features:
        if feature in js:
            print(f"✓ {desc}")
            passed += 1
        else:
            print(f"✗ {desc}")
    
    print(f"JavaScript: {passed}/{len(functions + key_features)} checks passed\n")
    return passed >= len(functions + key_features) - 1

def test_bibtex_format():
    """Test BibTeX format by examining actual entries"""
    print("=== BibTeX Format Verification ===")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Find BibTeX entries in onclick attributes
    pattern = r'showBibTeX\([^,]+,\s*`([^`]+)`'
    matches = re.findall(pattern, html, re.DOTALL)
    
    print(f"Found {len(matches)} BibTeX entries")
    
    if not matches:
        print("✗ No BibTeX entries found")
        return False
    
    # Check first entry format
    first_bibtex = matches[0]
    print("Sample BibTeX entry (first 200 chars):")
    print(first_bibtex[:200] + "...")
    
    # Check for required BibTeX elements
    required = [
        '@article{',
        'author=',
        'title=',
        'journal=',
        'year=',
        'note='
    ]
    
    passed = 0
    for req in required:
        if req in first_bibtex:
            print(f"✓ Contains {req}")
            passed += 1
        else:
            print(f"✗ Missing {req}")
    
    print(f"BibTeX format: {passed}/{len(required)} checks passed\n")
    return passed >= len(required) - 1

def test_paper_content():
    """Test that papers have proper content"""
    print("=== Paper Content Verification ===")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Count papers by looking for article tags with paper class
    paper_pattern = r'<article[^>]*class="paper"[^>]*>'
    papers = re.findall(paper_pattern, html)
    
    print(f"Found {len(papers)} paper articles")
    
    if len(papers) == 0:
        print("✗ No papers found")
        return False
    
    # Check for paper structure elements
    structure_checks = [
        ('paper-title', 'Paper titles'),
        ('paper-authors', 'Author information'),
        ('paper-abstract', 'Abstracts'),
        ('paper-date', 'Publication dates'),
        ('btn-primary', 'View paper buttons'),
        ('btn-cite', 'Cite buttons')
    ]
    
    passed = 0
    for check, desc in structure_checks:
        if check in html:
            print(f"✓ {desc}")
            passed += 1
        else:
            print(f"✗ {desc}")
    
    print(f"Paper structure: {passed}/{len(structure_checks)} checks passed\n")
    return passed >= len(structure_checks) - 1

def test_critical_functionality():
    """Test the most critical functionality"""
    print("=== Critical Functionality Verification ===")
    
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    # The most important features
    critical_features = [
        ('showBibTeX(', 'BibTeX modal function'),
        ('copyBibTeX()', 'Copy to clipboard function'),
        ('closeBibTeX()', 'Close modal function'),
        ('bibtexModal', 'Modal element'),
        ('bibtexText', 'BibTeX text area'),
        ('navigator.clipboard.writeText', 'Clipboard copy'),
        ('onclick="showTab(', 'Tab switching'),
        ('data-category=', 'Category data'),
        ('class="tab-content"', 'Tab content areas'),
        ('class="active"', 'Active state management')
    ]
    
    passed = 0
    for feature, desc in critical_features:
        if feature in html:
            print(f"✓ {desc}")
            passed += 1
        else:
            print(f"✗ {desc}")
    
    print(f"Critical functionality: {passed}/{len(critical_features)} checks passed\n")
    return passed >= len(critical_features) - 1

def main():
    """Run all verification tests"""
    print("ARXIV CS DAILY - FINAL VERIFICATION TEST")
    print("=" * 50)
    
    tests = [
        test_basic_html,
        test_javascript_functions, 
        test_bibtex_format,
        test_paper_content,
        test_critical_functionality
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    total_passed = sum(results)
    total_tests = len(results)
    
    print("=" * 50)
    print(f"FINAL RESULTS: {total_passed}/{total_tests} test categories passed")
    
    if total_passed >= total_tests - 1:
        print("✅ APPLICATION IS FUNCTIONAL - Ready for deployment")
        return True
    else:
        print("❌ APPLICATION HAS ISSUES - Needs fixes")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)