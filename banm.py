#!/usr/bin/python
# 88""Yb    db    88b 88 8b    d8 
# 88__dP   dPYb   88Yb88 88b  d88 
# 88""Yb  dP__Yb  88 Y88 88YbdP88 
# 88oodP dP""""Yb 88  Y8 88 YY 88 
# by SamuR4II

# Bookmarks And Notes Menu

import re
import subprocess
import pyperclip
import os

# where the program is located
path = str(os.path.dirname(os.path.abspath(__file__)) + "/")

# --

def parse_lines(lines):
    
    pattern = re.compile(r'#\[[^\]]+\]')

    matches = [line for line in lines if pattern.search(line)]

    names = [line[line.index('[')+1:line.index(']')] for line in matches]

    blocks = []
    current_block = []
    block_start = False
    for line in lines:
        if line in matches:
            if block_start:
                blocks.append(current_block)
                current_block = []
            else:
                block_start = True
        elif block_start:
            current_block.append(line)
    blocks.append(current_block)
    return names, blocks

def show_menu(items, prompt):
    # Use dmenu to show the menu of items
    dmenu_proc = subprocess.Popen(['dmenu', '-l', '10', '-p', prompt, '-nb', '#191919', '-nf', '#ff0f87', '-sb', '#3d3d3d', '-sf', '#ff0f87'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    # Send the list of items to dmenu
    dmenu_proc.stdin.write('\n'.join(items).encode())
    dmenu_proc.stdin.close()

    selected_item = dmenu_proc.stdout.read().decode().strip()
    return selected_item

def copy_text(text):
    pyperclip.copy(text)

def paste_text():
    xsel_proc = subprocess.Popen(['xsel', '-ob'], stdout=subprocess.PIPE)
    return xsel_proc.stdout.read().decode().strip()

def main():
    with open(path + 'links.txt', 'r') as f:
        lines = f.read().splitlines()

    names, blocks = parse_lines(lines)
    selected_name = show_menu(names, 'Select section:')
    selected_index = names.index(selected_name)
    selected_block = blocks[selected_index]
    selected_text = show_menu(selected_block, 'Select text or enter "`" to append:')
    # Check if the selected text is in the list of lines
    if selected_text == '`':
        written_text = str(paste_text())

        if written_text == "":
            exit()

        # Append the written text to the text file under the selected hashtag and text in brackets line
        with open(path + 'links.txt', 'w') as f:
            for line in lines:
                if line == f'#[{selected_name}]':
                    f.write(line)
                    f.write('\n')
                    f.write(written_text)
                    f.write('\n')
                else:
                    f.write(line)
                    f.write('\n')
    elif selected_text.endswith("#"):
            # Removes the selected text from the list if end with #
            selected_text = selected_text[:-1] 
            lines.remove(selected_text)
            with open(path + 'links.txt', 'w') as f:
                for line in lines:
                    f.write(line)
                    f.write('\n')
    else:
        copy_text(selected_text)

if __name__ == '__main__':
    main()

