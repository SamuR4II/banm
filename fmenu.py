#!/usr/bin/python
# by SamuR4II

import subprocess
import html.parser

class BookmarksParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            attrs = dict(attrs)
            self.links.append(attrs.get('href', ''))

def parse_bookmarks(html_text):
    parser = BookmarksParser()
    parser.feed(html_text)
    return parser.links

def show_menu(links):
    # Use dmenu with the specified options
    dmenu_proc = subprocess.Popen(['dmenu', '-l', '10', '-nb', '#191919', '-nf', '#ff0f87', '-sb', '#3d3d3d', '-sf', '#ff0f87'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    # Send the list of links to dmenu
    dmenu_proc.stdin.write('\n'.join(links).encode())
    dmenu_proc.stdin.close()
    # Get the selected link
    selected_link = dmenu_proc.stdout.read().decode().strip()
    return selected_link

def copy_link(link):
    # Copy the selected link to the clipboard
    subprocess.run(['xclip', '-selection', 'clipboard'], input=link.encode())

def main():
    # Read the contents of the bookmarks HTML file
    with open('bookmarks.html', 'r') as f:
        html_text = f.read()
    # Parse the bookmarks HTML file to extract the list of links
    links = parse_bookmarks(html_text)
    # Show the menu of links and get the selected link
    selected_link = show_menu(links)
    # Copy the selected link to the clipboard
    copy_link(selected_link)

if __name__ == '__main__':
    main()
