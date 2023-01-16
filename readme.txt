# banm.py

The program reads the links.txt file, opens Dmenu and shows you a few link/bookmark "folders". Whem you select
one, you will see the links in that are in that "folder". then you can select a links or note and it will copy
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

![dm1](https://user-images.githubusercontent.com/39969900/212649426-b01414d9-ca95-4778-822c-0791b4887eeb.png)
![dm2](https://user-images.githubusercontent.com/39969900/212649438-46e6b388-d3b9-41ca-9da4-103b2adf15d9.png)
