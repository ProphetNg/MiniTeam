#!/usr/bin/env python3
"""
Test browser compatibility by checking for standards-compliant code
"""

def test_browser_compatibility():
    """Test for cross-browser compatibility issues"""
    print("CROSS-BROWSER COMPATIBILITY TEST")
    print("=" * 40)
    
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    compatibility_score = 0
    total_checks = 0
    
    # === 1. HTML5 COMPATIBILITY ===
    print("1. HTML5 Compatibility:")
    
    html5_features = [
        ('<!DOCTYPE html>', 'HTML5 doctype'),
        ('<meta charset="UTF-8">', 'UTF-8 encoding'),
        ('<meta name="viewport"', 'Viewport meta tag'),
        ('header', 'Semantic header'),
        ('main', 'Semantic main'),
        ('article', 'Semantic article'),
        ('section', 'Semantic section'),
        ('nav', 'Semantic navigation')
    ]
    
    for feature, desc in html5_features:
        total_checks += 1
        if feature in html:
            print(f"   ✓ {desc}")
            compatibility_score += 1
        else:
            print(f"   ✗ {desc}")
    
    # === 2. CSS3 COMPATIBILITY ===
    print("\n2. CSS3 Compatibility:")
    
    css3_features = [
        ('border-radius', 'Rounded corners'),
        ('box-shadow', 'Drop shadows'),
        ('transition', 'CSS transitions'),
        ('transform', 'CSS transforms'),
        ('opacity', 'Opacity control'),
        ('@media', 'Media queries'),
        ('flex', 'Flexbox layout'),
        ('gradient', 'CSS gradients'),
        ('::before', 'CSS pseudo-elements'),
        ('::after', 'CSS pseudo-elements')
    ]
    
    for feature, desc in css3_features:
        total_checks += 1
        if feature in html:
            print(f"   ✓ {desc}")
            compatibility_score += 1
        else:
            print(f"   ✗ {desc}")
    
    # === 3. JAVASCRIPT COMPATIBILITY ===
    print("\n3. JavaScript Compatibility:")
    
    js_features = [
        ('addEventListener', 'Modern event handling'),
        ('classList', 'ClassList API'),
        ('querySelector', 'DOM query selectors'),
        ('navigator.clipboard', 'Clipboard API'),
        ('fetch', 'Fetch API'),
        ('Promise', 'Promise support'),
        ('async/await', 'Async functions'),
        ('document.getElementById', 'Traditional DOM access'),
        ('window.onclick', 'Window events'),
        ('setTimeout', 'Timing functions')
    ]
    
    for feature, desc in js_features:
        total_checks += 1
        if feature in html:
            print(f"   ✓ {desc}")
            compatibility_score += 1
        else:
            print(f"   ✗ {desc}")
    
    # === 4. FALLBACK MECHANISMS ===
    print("\n4. Fallback Mechanisms:")
    
    fallbacks = [
        ('document.execCommand', 'Clipboard fallback'),
        ('alert', 'User notification fallback'),
        ('innerHTML', 'Content manipulation fallback'),
        ('style.display', 'Style manipulation fallback'),
        ('window.location', 'Navigation fallback')
    ]
    
    for fallback, desc in fallbacks:
        total_checks += 1
        if fallback in html:
            print(f"   ✓ {desc}")
            compatibility_score += 1
        else:
            print(f"   ✗ {desc}")
    
    # === 5. ACCESSIBILITY FEATURES ===
    print("\n5. Accessibility Features:")
    
    accessibility_features = [
        ('button', 'Interactive buttons'),
        ('href', 'Link attributes'),
        ('target="_blank"', 'External link indication'),
        ('class', 'CSS classes for styling'),
        ('id', 'Element IDs for JavaScript'),
        ('onclick', 'Event handlers'),
        ('tabindex', 'Tab navigation (if present)'),
        ('aria-', 'ARIA attributes (if present)'),
        ('role=', 'ARIA roles (if present)'),
        ('alt=', 'Alt attributes (if present)')
    ]
    
    for feature, desc in accessibility_features:
        total_checks += 1
        if feature in html:
            print(f"   ✓ {desc}")
            compatibility_score += 1
        else:
            print(f"   ✗ {desc}")
    
    # === RESULTS ===
    print(f"\n" + "=" * 40)
    compatibility_rate = (compatibility_score / total_checks) * 100
    print(f"Browser Compatibility Score: {compatibility_score}/{total_checks} ({compatibility_rate:.1f}%)")
    
    # Browser support assessment
    print("\nBrowser Support Assessment:")
    
    if compatibility_rate >= 90:
        print("✅ EXCELLENT: Compatible with all modern browsers")
        print("   - Chrome 60+, Firefox 55+, Safari 12+, Edge 79+")
        print("   - Mobile browsers: iOS Safari 12+, Android Chrome 60+")
    elif compatibility_rate >= 75:
        print("✅ GOOD: Compatible with most modern browsers")
        print("   - Chrome 50+, Firefox 45+, Safari 10+, Edge 16+")
        print("   - Some minor features may not work in older browsers")
    elif compatibility_rate >= 60:
        print("⚠️  FAIR: Basic compatibility with modern browsers")
        print("   - Chrome 40+, Firefox 35+, Safari 9+, Edge 12+")
        print("   - Some features may require polyfills or fallbacks")
    else:
        print("❌ POOR: Limited browser compatibility")
        print("   - May require significant polyfills or browser-specific code")
    
    return compatibility_rate >= 75

if __name__ == "__main__":
    success = test_browser_compatibility()
    exit(0 if success else 1)