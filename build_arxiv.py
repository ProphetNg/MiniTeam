
def main():
    all_papers = []
    for category in CATEGORIES:
        papers = fetch_papers(category)
        all_papers.extend(papers)

    html_content = generate_html(all_papers)
    with open('index.html', 'w') as file:
        file.write(html_content)

if __name__ == '__main__':
    main()