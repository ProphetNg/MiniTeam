#!/usr/bin/env python3
"""
ArXiv CS Daily Paper Fetcher and HTML Generator
Fetches latest papers from arXiv API and generates a static HTML page with filtering and citation features.
"""

import requests
import xml.etree.ElementTree as ET
import datetime
import time
import json
import os
from urllib.parse import quote

# Constants
CATEGORIES = {
    'cs.AI': 'Artificial Intelligence',
    'cs.CV': 'Computer Vision', 
    'cs.CL': 'Computation and Language'
}
ARXIV_API_URL = "http://export.arxiv.org/api/query"
MAX_RESULTS_PER_CATEGORY = 10
OUTPUT_HTML = "index.html"

def fetch_arxiv_papers(category, max_results=MAX_RESULTS_PER_CATEGORY):
    """
    Fetch papers from arXiv API for a specific category
    """
    try:
        # Construct the query URL
        search_query = f"cat:{category}"
        url = f"{ARXIV_API_URL}?search_query={quote(search_query)}&start=0&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
        
        print(f"Fetching papers for {category}...")
        
        # Make the request with proper headers
        headers = {
            'User-Agent': 'ArXiv-Daily-Paper-Fetcher/1.0',
            'Accept': 'application/xml'
        }
        
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        return response.text
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {category}: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error fetching data for {category}: {e}")
        return None

def parse_arxiv_xml(xml_content, category):
    """
    Parse arXiv XML response and extract paper data
    """
    try:
        if not xml_content:
            return []
            
        # Parse XML
        root = ET.fromstring(xml_content)
        
        # Define namespace
        ns = {'atom': 'http://www.w3.org/2005/Atom',
              'arxiv': 'http://arxiv.org/schemas/atom'}
        
        papers = []
        
        for entry in root.findall('atom:entry', ns):
            try:
                # Extract title
                title = entry.find('atom:title', ns).text.strip() if entry.find('atom:title', ns) is not None else 'No title'
                
                # Extract authors
                authors = []
                for author in entry.findall('atom:author', ns):
                    name = author.find('atom:name', ns).text if author.find('atom:name', ns) is not None else 'Unknown'
                    authors.append(name)
                
                # Extract abstract
                abstract = entry.find('atom:summary', ns).text.strip() if entry.find('atom:summary', ns) is not None else 'No abstract'
                
                # Extract arXiv ID
                id_element = entry.find('atom:id', ns)
                arxiv_id = id_element.text.split('/')[-1] if id_element is not None else 'unknown'
                if 'v' in arxiv_id:
                    arxiv_id = arxiv_id.split('v')[0]
                
                # Extract published date
                published = entry.find('atom:published', ns).text if entry.find('atom:published', ns) is not None else None
                
                # Extract link
                link = entry.find('atom:link[@rel="alternate"]', ns).get('href') if entry.find('atom:link[@rel="alternate"]', ns) is not None else f"https://arxiv.org/abs/{arxiv_id}"
                
                # Extract DOI if available
                doi = None
                for link_element in entry.findall('atom:link', ns):
                    if link_element.get('title') == 'doi':
                        doi = link_element.get('href')
                        break
                
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
                
            except Exception as e:
                print(f"Error parsing entry: {e}")
                continue
        
        return papers
        
    except ET.ParseError as e:
        print(f"XML parsing error: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error parsing XML: {e}")
        return []

def generate_bibtex(paper):
    """
    Generate BibTeX citation for a paper
    """
    try:
        # Format authors for BibTeX
        author_names = []
        for author in paper['authors']:
            if ',' in author:
                author_names.append(author)
            else:
                # Split name into first and last name
                parts = author.split()
                if len(parts) > 1:
                    last_name = parts[-1]
                    first_names = ' '.join(parts[:-1])
                    author_names.append(f"{last_name}, {first_names}")
                else:
                    author_names.append(author)
        
        authors_str = ' and '.join(author_names)
        
        # Create citation key
        first_author_last = paper['authors'][0].split()[-1] if paper['authors'] else 'unknown'
        year = paper['published'].split('-')[0] if paper['published'] else 'unknown'
        citation_key = f"{first_author_last.lower()}{year}_{paper['arxiv_id']}"
        
        # Build BibTeX entry
        bibtex = f"@article{{{citation_key},\n"
        bibtex += f"  author = {{{authors_str}}},\n"
        bibtex += f"  title = {{{paper['title']}}},\n"
        bibtex += f"  journal = {{arXiv preprint arXiv:{paper['arxiv_id']}}},\n"
        if paper['published']:
            bibtex += f"  year = {{{paper['published'].split('-')[0]}}},\n"
        bibtex += f"  note = {{arXiv:{paper['arxiv_id']}}}\n"
        bibtex += "}"
        
        return bibtex
        
    except Exception as e:
        print(f"Error generating BibTeX: {e}")
        return ""

def generate_html(papers_by_category):
    """
    Generate HTML page with papers organized by category
    """
    try:
        # Get current date
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        
        # Start HTML
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ArXiv CS Daily Papers - {current_date}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
            line-height: 1.6;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #2c3e50;
            text-align: center;
            margin-bottom: 10px;
            font-size: 2.5em;
        }}
        .subtitle {{
            text-align: center;
            color: #7f8c8d;
            margin-bottom: 30px;
            font-size: 1.1em;
        }}
        .tabs {{
            display: flex;
            margin-bottom: 30px;
            border-bottom: 2px solid #ecf0f1;
        }}
        .tab {{
            padding: 15px 25px;
            cursor: pointer;
            background: #ecf0f1;
            border: none;
            margin-right: 5px;
            border-radius: 5px 5px 0 0;
            font-size: 1em;
            transition: all 0.3s ease;
        }}
        .tab.active {{
            background: #3498db;
            color: white;
        }}
        .tab:hover {{
            background: #2980b9;
            color: white;
        }}
        .tab-content {{
            display: none;
        }}
        .tab-content.active {{
            display: block;
        }}
        .paper {{
            background: #f8f9fa;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 8px;
            border-left: 4px solid #3498db;
            transition: all 0.3s ease;
        }}
        .paper:hover {{
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            transform: translateY(-2px);
        }}
        .paper-title {{
            font-size: 1.3em;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 10px;
        }}
        .paper-authors {{
            color: #7f8c8d;
            font-style: italic;
            margin-bottom: 10px;
        }}
        .paper-abstract {{
            margin-bottom: 15px;
            color: #34495e;
            text-align: justify;
        }}
        .paper-meta {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 10px;
        }}
        .paper-links {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}
        .btn {{
            padding: 8px 16px;
            text-decoration: none;
            border-radius: 4px;
            font-size: 0.9em;
            transition: all 0.3s ease;
            border: none;
            cursor: pointer;
        }}
        .btn-primary {{
            background: #3498db;
            color: white;
        }}
        .btn-primary:hover {{
            background: #2980b9;
        }}
        .btn-cite {{
            background: #e74c3c;
            color: white;
        }}
        .btn-cite:hover {{
            background: #c0392b;
        }}
        .paper-date {{
            color: #95a5a6;
            font-size: 0.9em;
        }}
        .bibtex-modal {{
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.5);
            z-index: 1000;
        }}
        .bibtex-content {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: white;
            padding: 30px;
            border-radius: 10px;
            max-width: 80%;
            max-height: 80%;
            overflow: auto;
        }}
        .bibtex-text {{
            background: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
            white-space: pre-wrap;
            margin: 15px 0;
        }}
        .close-btn {{
            float: right;
            cursor: pointer;
            font-size: 1.5em;
            color: #95a5a6;
        }}
        .close-btn:hover {{
            color: #2c3e50;
        }}
        @media (max-width: 768px) {{
            .container {{
                padding: 15px;
            }}
            .tabs {{
                flex-direction: column;
            }}
            .tab {{
                margin-bottom: 5px;
                margin-right: 0;
            }}
            .paper-meta {{
                flex-direction: column;
                align-items: flex-start;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>ArXiv CS Daily Papers</h1>
        <div class="subtitle">Latest papers in Computer Science - {current_date}</div>
        
        <div class="tabs">
"""

        # Add tabs
        for i, (category, name) in enumerate(CATEGORIES.items()):
            active_class = "active" if i == 0 else ""
            html += f'            <button class="tab {active_class}" onclick="showTab(\'{category}\')">{name}</button>\n'

        html += """        </div>
"""

        # Add tab content
        for i, (category, name) in enumerate(CATEGORIES.items()):
            active_class = "active" if i == 0 else ""
            html += f'        <div id="{category}" class="tab-content {active_class}">\n'
            
            if category in papers_by_category and papers_by_category[category]:
                for paper in papers_by_category[category]:
                    bibtex_data = generate_bibtex(paper)
                    html += f"""            <div class="paper" data-arxiv-id="{paper['arxiv_id']}">
                <div class="paper-title">{paper['title']}</div>
                <div class="paper-authors">{', '.join(paper['authors'])}</div>
                <div class="paper-abstract">{paper['abstract']}</div>
                <div class="paper-meta">
                    <div class="paper-date">Published: {paper['published'][:10] if paper['published'] else 'Unknown'}</div>
                    <div class="paper-links">
                        <a href="{paper['link']}" class="btn btn-primary" target="_blank">View Paper</a>
                        <button class="btn btn-cite" onclick="showBibTeX('{paper['arxiv_id']}', `{bibtex_data.replace('`', '\\`')}`)">Cite</button>
                    </div>
                </div>
            </div>
"""
            else:
                html += f'            <p>No papers found for {name}.</p>\n'
            
            html += '        </div>\n'

        # Add JavaScript and close HTML
        html += """    </div>

    <!-- BibTeX Modal -->
    <div id="bibtexModal" class="bibtex-modal">
        <div class="bibtex-content">
            <span class="close-btn" onclick="closeBibTeX()">&times;</span>
            <h3>BibTeX Citation</h3>
            <div id="bibtexText" class="bibtex-text"></div>
            <button class="btn btn-primary" onclick="copyBibTeX()">Copy to Clipboard</button>
            <button class="btn" onclick="closeBibTeX()">Close</button>
        </div>
    </div>

    <script>
        function showTab(category) {
            // Hide all tab contents
            const tabContents = document.querySelectorAll('.tab-content');
            tabContents.forEach(content => {
                content.classList.remove('active');
            });
            
            // Remove active class from all tabs
            const tabs = document.querySelectorAll('.tab');
            tabs.forEach(tab => {
                tab.classList.remove('active');
            });
            
            // Show selected tab content
            document.getElementById(category).classList.add('active');
            
            // Add active class to clicked tab
            event.target.classList.add('active');
        }

        function showBibTeX(arxivId, bibtex) {
            document.getElementById('bibtexText').textContent = bibtex;
            document.getElementById('bibtexModal').style.display = 'block';
        }

        function closeBibTeX() {
            document.getElementById('bibtexModal').style.display = 'none';
        }

        function copyBibTeX() {
            const bibtexText = document.getElementById('bibtexText').textContent;
            navigator.clipboard.writeText(bibtexText).then(() => {
                alert('BibTeX citation copied to clipboard!');
            }).catch(() => {
                // Fallback for older browsers
                const textArea = document.createElement('textarea');
                textArea.value = bibtexText;
                document.body.appendChild(textArea);
                textArea.select();
                document.execCommand('copy');
                document.body.removeChild(textArea);
                alert('BibTeX citation copied to clipboard!');
            });
        }

        // Close modal when clicking outside
        window.onclick = function(event) {
            const modal = document.getElementById('bibtexModal');
            if (event.target === modal) {
                closeBibTeX();
            }
        }
    </script>
</body>
</html>"""

        return html

    except Exception as e:
        print(f"Error generating HTML: {e}")
        return None

def main():
    """
    Main function to fetch arXiv data and generate HTML
    """
    print("Starting ArXiv CS Daily Paper Fetcher...")
    
    papers_by_category = {}
    
    # Fetch papers for each category
    for category in CATEGORIES:
        print(f"\nProcessing {category} ({CATEGORIES[category]})...")
        
        # Fetch XML data
        xml_content = fetch_arxiv_papers(category)
        
        if xml_content:
            # Parse XML and extract papers
            papers = parse_arxiv_xml(xml_content, category)
            
            if papers:
                papers_by_category[category] = papers
                print(f"Successfully parsed {len(papers)} papers for {category}")
            else:
                print(f"No papers found for {category}")
                papers_by_category[category] = []
        else:
            print(f"Failed to fetch data for {category}")
            papers_by_category[category] = []
        
        # Small delay to be respectful to the API
        time.sleep(1)
    
    # Generate HTML
    if papers_by_category:
        print("\nGenerating HTML...")
        html_content = generate_html(papers_by_category)
        
        if html_content:
            # Write HTML file
            try:
                with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
                    f.write(html_content)
                print(f"\nSuccess! HTML file '{OUTPUT_HTML}' has been generated.")
                print(f"Total papers: {sum(len(papers) for papers in papers_by_category.values())}")
            except Exception as e:
                print(f"Error writing HTML file: {e}")
        else:
            print("Failed to generate HTML content.")
    else:
        print("No papers were fetched. HTML generation skipped.")

if __name__ == "__main__":
    main()