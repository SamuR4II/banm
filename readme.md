# banm.py

The program reads the links.txt file, opens Dmenu and shows you a few link/bookmark "folders". When you select
one, you will see the links or notes that are in that "folder". then you can select a links or note and it will copy
it to your clipboard.

In the Links.txt file, "folders" are presented as a hashtag and text in brackets, like this: #[ExampleText]
Under them you can see the links or notes that you will be shown when the "folder" is selected.

# append links/notes
You kan append text that is stored in you're clipboard by selecting a "folder" and typing: '`'
this will add the text to the links.txt file.

# delete links/notes
When you have selected a "folder", you can select a link/note and press tab, you can then add a # hashtag after
the link or note that you have selected and press enter. The link/note will be removed from the links.txt file.

Example: 'selectedtext#'


# fmenu.py

fmenu.py only works with an exported booksmarks.html file that you can export from firefox. then you'll get
a list of links in dmenu that you can copy. The bookmarks.html file must be in the same directory.
