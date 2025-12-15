# ArXiv CS Daily

A Python application that fetches the latest computer science papers from arXiv and generates a beautiful, interactive HTML page with filtering, citation features, and responsive design.

## 🎯 Project Overview

**ArXiv CS Daily** is an automated paper aggregation and presentation system designed specifically for computer science researchers and enthusiasts. It fetches the latest papers from selected arXiv CS categories and presents them in a clean, professional, and interactive web interface.

### Purpose

- **Stay Updated**: Automatically fetch and display the latest CS papers from arXiv
- **Easy Navigation**: Organize papers by categories with intuitive tabbed interface
- **Research Efficiency**: Quick access to paper details, abstracts, and citations
- **Citation Management**: One-click BibTeX citation generation and copying
- **Mobile Friendly**: Fully responsive design for desktop, tablet, and mobile devices

## ✨ Features & Functionality

### Core Features
- **Automated Fetching**: Fetches latest papers from arXiv API
- **Category Organization**: Groups papers by CS subfields (AI, Computer Vision, NLP)
- **Interactive Interface**: Tabbed navigation for easy category switching
- **Search & Filter**: Quick access to specific papers and categories
- **Responsive Design**: Works seamlessly on all devices

### Citation System ⭐
- **One-Click Citations**: Generate BibTeX citations instantly
- **Clipboard Copy**: Copy citations to clipboard with a single click
- **Modal Interface**: Clean, distraction-free citation viewing
- **Author Formatting**: Properly formatted author names in BibTeX
- **Citation Keys**: Automatically generated unique citation keys

### User Experience
- **Clean Design**: Modern, professional interface with smooth animations
- **Fast Loading**: Optimized for quick loading and smooth interactions
- **Accessibility**: Keyboard navigation and screen reader friendly
- **Print Support**: Optimized print layouts for offline reading

## 🚀 Installation & Usage

### Prerequisites
- Python 3.7 or higher
- Internet connection (for arXiv API access)
- Modern web browser

### Quick Start

1. **Clone or Download the Project**
   ```bash
   # If using git
   git clone <repository-url>
   cd arxiv_cs_daily_real
   ```

2. **Install Required Python Packages**
   ```bash
   pip install requests
   ```

3. **Run the Application**
   ```bash
   python build_arxiv.py
   ```

4. **Open the Generated HTML**
   ```bash
   # Open in your default browser
   open index.html
   # Or manually open the file in your web browser
   ```

### Detailed Usage Instructions

#### Running the Python Script
The `build_arxiv.py` script performs the following operations:
1. Fetches latest papers from configured arXiv categories
2. Parses XML data from arXiv API
3. Generates BibTeX citations for each paper
4. Creates a complete HTML file with styling and JavaScript
5. Saves the output as `index.html`

```bash
# Run with default settings
python build_arxiv.py

# The script will show progress:
# Starting ArXiv CS Daily Paper Fetcher...
# 
# Processing cs.AI (Artificial Intelligence)...
# Fetching papers for cs.AI...
# Successfully parsed 10 papers for cs.AI
# 
# Processing cs.CV (Computer Vision)...
# Fetching papers for cs.CV...
# Successfully parsed 10 papers for cs.CV
# 
# Processing cs.CL (Computation and Language)...
# Fetching papers for cs.CL...
# Successfully parsed 10 papers for cs.CL
# 
# Generating HTML...
# Success! HTML file 'index.html' has been generated.
# Total papers: 30
```

#### Viewing the Generated HTML
1. Open `index.html` in any modern web browser
2. Use the category tabs to switch between different CS fields
3. Click on paper titles to view full details
4. Use "View Paper" buttons to open papers on arXiv
5. Use "Cite" buttons to generate and copy BibTeX citations

## 🔧 Technical Details

### Technologies Used
- **Python 3.7+**: Core application logic
- **Requests Library**: HTTP requests to arXiv API
- **XML Parsing**: Built-in xml.etree.ElementTree
- **HTML5**: Modern semantic markup
- **CSS3**: Advanced styling with animations and responsive design
- **Vanilla JavaScript**: Interactive features without dependencies
- **arXiv API**: Official arXiv API for paper metadata

### arXiv API Integration
The application integrates with the arXiv API through:
- **RESTful Queries**: HTTP GET requests to `export.arxiv.org/api/query`
- **XML Response**: Parsing Atom XML format
- **Rate Limiting**: Built-in delays to respect API limits
- **Error Handling**: Robust error handling for network issues
- **Category Filtering**: Fetching papers by specific CS categories

**API Endpoint:**
```
http://export.arxiv.org/api/query?search_query=cat:{category}&start=0&max_results=10&sortBy=submittedDate&sortOrder=descending
```

### Data Processing Workflow
1. **API Request**: Fetch XML data for each category
2. **XML Parsing**: Extract paper metadata (title, authors, abstract, etc.)
3. **Data Validation**: Clean and validate extracted data
4. **BibTeX Generation**: Create formatted citations for each paper
5. **HTML Generation**: Build complete web page with embedded data
6. **File Output**: Save generated HTML to `index.html`

## 📁 File Structure

```
arxiv_cs_daily_real/
├── README.md                 # This documentation file
├── build_arxiv.py           # Main Python application
├── index.html               # Generated HTML output (after running)
├── style.css               # Advanced CSS styling (optional)
├── test_*.py               # Test files for development
└── requirements.txt        # Python dependencies (if created)
```

### File Descriptions

- **`build_arxiv.py`**: Core application that fetches arXiv data and generates HTML
  - Contains arXiv API integration
  - XML parsing logic
  - BibTeX generation functions
  - HTML generation with embedded CSS and JavaScript
  - Command-line interface

- **`index.html`**: Generated web interface (created after running build_arxiv.py)
  - Complete standalone HTML file
  - Embedded CSS styling
  - Interactive JavaScript functionality
  - Responsive design for all devices

- **`style.css`**: Advanced styling file (optional enhancement)
  - CSS custom properties and variables
  - Advanced animations and transitions
  - Responsive design utilities
  - Print optimization styles

- **`test_*.py`**: Test files for development and verification
  - Various test scenarios for functionality verification
  - Browser compatibility testing
  - Error handling validation

## 🌐 Browser Compatibility

### Supported Browsers
- **Chrome/Chromium**: Version 80+ (Recommended)
- **Firefox**: Version 75+ (Full Support)
- **Safari**: Version 13+ (Full Support)
- **Edge**: Version 80+ (Full Support)
- **Mobile Browsers**: iOS Safari 13+, Chrome for Android 80+

### Compatibility Features
- **ES6+ JavaScript**: Modern JavaScript features
- **CSS Grid & Flexbox**: Advanced layout systems
- **CSS Custom Properties**: CSS variables for theming
- **Clipboard API**: Modern clipboard operations
- **Responsive Design**: Mobile-first approach
- **Accessibility**: ARIA labels and keyboard navigation

### Fallback Support
- **Clipboard Copy**: Falls back to `document.execCommand()` for older browsers
- **CSS Flexbox**: Graceful degradation for older browsers
- **JavaScript**: Non-critical features fail gracefully

## 📚 Citation Feature Documentation

### How to Use the "Cite" Buttons

The citation system is designed to be intuitive and efficient:

1. **Locate the Paper**: Find the paper you want to cite in any category tab
2. **Click "Cite" Button**: Each paper has a red "Cite" button in its action area
3. **View Citation**: A modal window appears with the formatted BibTeX citation
4. **Copy to Clipboard**: Click "Copy to Clipboard" button to copy the citation
5. **Confirmation**: A success message confirms the citation has been copied

### BibTeX Format Explanation

The application generates standard BibTeX format citations:

```bibtex
@article{shi2025_2512.10957,
  author = {Shi, Yukai and Li, Weiyu and Wang, Zihao and Li, Hongyang and Chen, Xingyu and Tan, Ping and Zhang, Lei},
  title = {SceneMaker: Open-set 3D Scene Generation with Decoupled De-occlusion and Pose Estimation Model},
  journal = {arXiv preprint arXiv:2512.10957},
  year = {2025},
  note = {arXiv:2512.10957}
}
```

**BibTeX Components:**
- **`@article`**: Entry type for journal articles
- **Citation Key**: Unique identifier (e.g., `shi2025_2512.10957`)
- **Author Field**: Formatted author names (Last, First format)
- **Title Field**: Complete paper title
- **Journal Field**: arXiv reference with ID
- **Year Field**: Publication year extracted from submission date
- **Note Field**: arXiv identifier for reference

### Clipboard Copy Functionality

The clipboard functionality uses modern web APIs with fallbacks:

**Modern Browsers (Clipboard API):**
```javascript
navigator.clipboard.writeText(bibtexText).then(() => {
    alert('BibTeX citation copied to clipboard!');
});
```

**Legacy Browsers (Fallback):**
```javascript
const textArea = document.createElement('textarea');
textArea.value = bibtexText;
document.body.appendChild(textArea);
textArea.select();
document.execCommand('copy');
document.body.removeChild(textArea);
```

### Citation Examples

#### Example 1: Single Author
```bibtex
@article{wilson2025_2512.10937,
  author = {Wilson, Matt},
  title = {On Decision-Making Agents and Higher-Order Causal Processes},
  journal = {arXiv preprint arXiv:2512.10937},
  year = {2025},
  note = {arXiv:2512.10937}
}
```

#### Example 2: Multiple Authors
```bibtex
@article{tang2025_2512.10949,
  author = {Tang, Yiwen and Guo, Zoey and Zhu, Kaixin and Zhang, Ray and Chen, Qizhi and Jiang, Dongzhi and Liu, Junli and Zeng, Bohan and Song, Haoming and Qu, Delin and Bai, Tianyi and Xu, Dan and Zhang, Wentao and Zhao, Bin},
  title = {Are We Ready for RL in Text-to-3D Generation? A Progressive Investigation},
  journal = {arXiv preprint arXiv:2512.10949},
  year = {2025},
  note = {arXiv:2512.10949}
}
```

## 🛠 Technical Documentation

### HTML Structure Explanation

The generated HTML follows semantic structure:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Meta tags and title -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ArXiv CS Daily Papers - [Current Date]</title>
    
    <!-- Embedded CSS -->
    <style>
        /* CSS variables, layout, animations */
    </style>
</head>
<body>
    <!-- Main container -->
    <div class="container">
        <!-- Header section -->
        <header>
            <h1>ArXiv CS Daily Papers</h1>
            <div class="subtitle">Latest papers in Computer Science</div>
        </header>
        
        <!-- Navigation tabs -->
        <div class="tabs">
            <button class="tab active" onclick="showTab('cs.AI')">Artificial Intelligence</button>
            <button class="tab" onclick="showTab('cs.CV')">Computer Vision</button>
            <button class="tab" onclick="showTab('cs.CL')">Computation and Language</button>
        </div>
        
        <!-- Tab content sections -->
        <div id="cs.AI" class="tab-content active">
            <!-- Paper cards for AI category -->
        </div>
        
        <!-- Other category sections -->
        
    </div>
    
    <!-- BibTeX Modal -->
    <div id="bibtexModal" class="bibtex-modal">
        <!-- Citation display interface -->
    </div>
    
    <!-- JavaScript functionality -->
    <script>
        // Tab switching, modal management, clipboard operations
    </script>
</body>
</html>
```

### CSS Styling Approach

The application uses modern CSS with a systematic approach:

#### CSS Custom Properties
```css
:root {
    /* Color Palette */
    --primary-color: #2563eb;
    --primary-dark: #1d4ed8;
    --secondary-color: #7c3aed;
    
    /* Typography */
    --font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    
    /* Spacing & Layout */
    --spacing-md: 1rem;
    --spacing-lg: 1.5rem;
    
    /* Animations */
    --transition-normal: 300ms ease;
}
```

#### Responsive Design Strategy
- **Mobile-First**: Base styles for mobile devices
- **Media Queries**: Progressive enhancement for larger screens
- **Flexible Layouts**: CSS Grid and Flexbox for adaptive layouts
- **Touch-Friendly**: Larger tap targets for mobile interaction

#### Animation & Interaction Design
- **Smooth Transitions**: Consistent timing functions
- **Hover Effects**: Visual feedback for interactive elements
- **Loading States**: Animated loading indicators
- **Modal Animations**: Fade and scale effects for modals

### JavaScript Functionality Overview

#### Core Functions
1. **Tab Management**
   ```javascript
   function showTab(category) {
       // Hide all tab contents
       // Show selected tab content
       // Update active tab styling
   }
   ```

2. **BibTeX Modal Management**
   ```javascript
   function showBibTeX(arxivId, bibtex) {
       // Display BibTeX in modal
       // Show modal overlay
   }
   
   function closeBibTeX() {
       // Hide modal
   }
   ```

3. **Clipboard Operations**
   ```javascript
   function copyBibTeX() {
       // Modern clipboard API with fallback
       // User feedback on success/failure
   }
   ```

#### Event Handling
- **Click Events**: Tab switching, modal controls
- **Keyboard Events**: ESC key to close modal
- **Window Events**: Click outside modal to close
- **Touch Events**: Mobile interaction support

### Data Fetching and Processing Workflow

#### Step 1: API Configuration
```python
CATEGORIES = {
    'cs.AI': 'Artificial Intelligence',
    'cs.CV': 'Computer Vision', 
    'cs.CL': 'Computation and Language'
}
ARXIV_API_URL = "http://export.arxiv.org/api/query"
MAX_RESULTS_PER_CATEGORY = 10
```

#### Step 2: Data Fetching
```python
def fetch_arxiv_papers(category, max_results=MAX_RESULTS_PER_CATEGORY):
    search_query = f"cat:{category}"
    url = f"{ARXIV_API_URL}?search_query={quote(search_query)}&start=0&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
    
    headers = {
        'User-Agent': 'ArXiv-Daily-Paper-Fetcher/1.0',
        'Accept': 'application/xml'
    }
    
    response = requests.get(url, headers=headers, timeout=30)
    return response.text
```

#### Step 3: XML Parsing
```python
def parse_arxiv_xml(xml_content, category):
    root = ET.fromstring(xml_content)
    ns = {'atom': 'http://www.w3.org/2005/Atom',
          'arxiv': 'http://arxiv.org/schemas/atom'}
    
    papers = []
    for entry in root.findall('atom:entry', ns):
        # Extract title, authors, abstract, etc.
        paper = {
            'title': title,
            'authors': authors,
            'abstract': abstract,
            'arxiv_id': arxiv_id,
            'published': published,
            'link': link,
            'doi': doi,
            'category': category
        }
        papers.append(paper)
```

#### Step 4: BibTeX Generation
```python
def generate_bibtex(paper):
    # Format authors
    author_names = []
    for author in paper['authors']:
        if ',' in author:
            author_names.append(author)
        else:
            parts = author.split()
            last_name = parts[-1]
            first_names = ' '.join(parts[:-1])
            author_names.append(f"{last_name}, {first_names}")
    
    # Create citation key
    first_author_last = paper['authors'][0].split()[-1]
    year = paper['published'].split('-')[0]
    citation_key = f"{first_author_last.lower()}{year}_{paper['arxiv_id']}"
    
    # Build BibTeX entry
    bibtex = f"@article{{{citation_key},\n"
    bibtex += f"  author = {{{' and '.join(author_names)}}},\n"
    bibtex += f"  title = {{{paper['title']}}},\n"
    bibtex += f"  journal = {{arXiv preprint arXiv:{paper['arxiv_id']}}},\n"
    bibtex += f"  year = {{{paper['published'].split('-')[0]}}},\n"
    bibtex += f"  note = {{arXiv:{paper['arxiv_id']}}}\n"
    bibtex += "}"
    
    return bibtex
```

#### Step 5: HTML Generation
```python
def generate_html(papers_by_category):
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <title>ArXiv CS Daily Papers - {current_date}</title>
    <style>
        /* Embedded CSS */
    </style>
</head>
<body>
    <!-- HTML structure with paper data -->
    <!-- JavaScript functionality -->
</body>
</html>"""
    
    return html
```

## 🔧 Development Notes

### How to Modify Categories

To add, remove, or modify arXiv categories:

1. **Edit the CATEGORIES Dictionary** in `build_arxiv.py`:
   ```python
   CATEGORIES = {
       'cs.AI': 'Artificial Intelligence',
       'cs.CV': 'Computer Vision', 
       'cs.CL': 'Computation and Language',
       # Add new categories here
       'cs.LG': 'Machine Learning',
       'cs.RO': 'Robotics'
   }
   ```

2. **Supported Category Formats**:
   - Use official arXiv category codes (e.g., 'cs.AI', 'cs.CV')
   - Full list available at: https://arxiv.org/category_taxonomy
   - Format: `cs.SUBJECT` for Computer Science subjects

3. **Category Display Names**:
   - The dictionary value is the display name shown in the web interface
   - Can be customized for better user experience

**Example: Adding New Categories**
```python
CATEGORIES = {
    'cs.AI': 'Artificial Intelligence',
    'cs.CV': 'Computer Vision', 
    'cs.CL': 'Computation and Language',
    'cs.LG': 'Machine Learning',
    'cs.RO': 'Robotics',
    'cs.IR': 'Information Retrieval'
}
```

### How to Customize the Styling

#### Method 1: Modify Embedded CSS (Simple)
Edit the CSS section in `build_arxiv.py` within the `generate_html()` function:

```python
# Find this section in generate_html()
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <style>
        /* Modify colors, fonts, spacing here */
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f5f5f5;
            /* Add your custom styles */
        }}
        
        .container {{
            max-width: 1200px;
            /* Customize container */
        }}
        
        /* Add more custom styles */
    </style>
</head>
"""
```

#### Method 2: Use External CSS File (Advanced)
1. Create a custom CSS file (e.g., `custom.css`)
2. Modify `build_arxiv.py` to include external CSS:
   ```python
   # In generate_html() function
   html = f"""<!DOCTYPE html>
   <html lang="en">
   <head>
       <link rel="stylesheet" href="custom.css">
       <!-- Keep embedded CSS as fallback -->
   </head>
   """
   ```

#### Customization Examples
```css
/* Change color scheme */
:root {
    --primary-color: #2c3e50;
    --secondary-color: #e74c3c;
}

/* Modify typography */
body {
    font-family: 'Georgia', serif;
    font-size: 18px;
}

/* Adjust layout */
.container {
    max-width: 1400px;
    padding: 40px;
}

/* Customize paper cards */
.paper {
    background: linear-gradient(135deg, #f8f9fa, #e9ecef);
    border-left: 5px solid var(--primary-color);
}
```

### How to Extend Functionality

#### Adding New Features
1. **Additional Paper Information**:
   ```python
   # In parse_arxiv_xml() function
   paper['comments'] = entry.find('arxiv:comment', ns).text if entry.find('arxiv:comment', ns) is not None else None
   ```

2. **New Export Formats**:
   ```python
   def generate_ris_citation(paper):
       # Implement RIS format
       ris = f"TY  - JOUR\n"
       ris += f"AU  - {' and '.join(paper['authors'])}\n"
       ris += f"TI  - {paper['title']}\n"
       ris += f"JO  - arXiv:{paper['arxiv_id']}\n"
       ris += f"PY  - {paper['published'].split('-')[0]}\n"
       ris += f"ER  - \n"
       return ris
   ```

3. **Search Functionality**:
   ```javascript
   // Add to HTML/JavaScript
   function searchPapers(query) {
       // Implement client-side search
       const papers = document.querySelectorAll('.paper');
       papers.forEach(paper => {
           const title = paper.querySelector('.paper-title').textContent.toLowerCase();
           const authors = paper.querySelector('.paper-authors').textContent.toLowerCase();
           if (title.includes(query.toLowerCase()) || authors.includes(query.toLowerCase())) {
               paper.style.display = 'block';
           } else {
               paper.style.display = 'none';
           }
       });
   }
   ```

#### Integration Options
1. **Database Storage**: Add SQLite/PostgreSQL integration for historical data
2. **Email Notifications**: Send daily summaries via email
3. **RSS Feed**: Generate RSS feed for latest papers
4. **API Endpoint**: Create REST API for programmatic access

### Troubleshooting Common Issues

#### Network/Connection Issues
**Problem**: "Error fetching data for category"
**Solution**: 
- Check internet connection
- Verify arXiv API is accessible
- Increase timeout in `fetch_arxiv_papers()`

```python
# Increase timeout from 30 to 60 seconds
response = requests.get(url, headers=headers, timeout=60)
```

#### XML Parsing Errors
**Problem**: "XML parsing error"
**Solution**:
- Verify arXiv API response format
- Add error handling for malformed XML
- Check namespace definitions

```python
try:
    root = ET.fromstring(xml_content)
except ET.ParseError as e:
    print(f"XML parsing failed: {e}")
    return []
```

#### Rate Limiting
**Problem**: Too many requests to arXiv API
**Solution**:
- Increase delay between requests
- Add exponential backoff
- Respect arXiv's terms of service

```python
import time
import random

# Add random delay between 1-3 seconds
time.sleep(1 + random.random() * 2)
```

#### Browser Compatibility Issues
**Problem**: Features not working in older browsers
**Solution**:
- Add feature detection
- Provide fallbacks for older browsers
- Test across different browsers

```javascript
// Check for clipboard API support
if (!navigator.clipboard) {
    // Use fallback method
    console.log('Clipboard API not supported, using fallback');
}
```

#### Memory Issues with Large Datasets
**Problem**: Application crashes with many papers
**Solution**:
- Implement pagination
- Reduce papers per category
- Add lazy loading

```python
# Reduce papers per category
MAX_RESULTS_PER_CATEGORY = 5  # Instead of 10
```

#### Citation Format Issues
**Problem**: Incorrect BibTeX formatting
**Solution**:
- Validate author name formatting
- Check special character handling
- Verify citation key generation

```python
# Add author name validation
def format_author_name(author):
    # Remove extra spaces, handle special characters
    author = ' '.join(author.split())
    # Add more formatting logic as needed
    return author
```

## 📄 License

This project is provided as-is for educational and research purposes. Please respect arXiv's terms of service when using their API.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and enhancement requests.

## 📞 Support

If you encounter any issues or have questions:
1. Check this documentation for troubleshooting
2. Review the code comments in `build_arxiv.py`
3. Test with different browsers if facing UI issues

---

**Last Updated**: December 2025  
**Version**: 1.0  
**Python Requirement**: 3.7+  
**Browser Support**: Modern browsers (Chrome 80+, Firefox 75+, Safari 13+, Edge 80+)