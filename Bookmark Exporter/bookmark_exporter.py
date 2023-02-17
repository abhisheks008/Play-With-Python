import os
import platform

# Get the user's home directory
if platform.system() == 'Windows':
    home_dir = os.path.expanduser('~').replace('\\', '/')
else:
    home_dir = os.path.expanduser('~')

# Get the path to the Chrome bookmarks file
chrome_bookmarks_file = f'{home_dir}/AppData/Local/Google/Chrome/User Data/Default/Bookmarks'

# Run a PowerShell command to get the bookmarks from the Chrome bookmarks file
cmd = f'powershell -Command "$json = Get-Content \'{chrome_bookmarks_file}\' -Raw | ConvertFrom-Json; $bookmarks = $json.roots.bookmark_bar.Children + $json.roots.other.Children; $output = \'\'; foreach ($bookmark in $bookmarks) {{ $folder = $bookmark.Parent; while ($folder) {{ $output += \'&nbsp;&nbsp;&nbsp;&nbsp;\'; $folder = $folder.Parent }}; $output += $bookmark.Name + \' => \' + $bookmark.Url + \'&lt;br&gt;\'; }}; $output"'

# Run the command and store the output in a variable
output = os.popen(cmd).read()

# Ask the user what format they want to save the bookmarks in
while True:
    save_format = input('In what format would you like to save your bookmarks? (HTML, PDF, or TXT): ').upper()
    if save_format in ['HTML', 'PDF', 'TXT']:
        break
    else:
        print('Invalid format. Please enter HTML, PDF, or TXT.')

# Save the output in the chosen format
if save_format == 'HTML':
    with open('bookmarks.html', 'w') as f:
        #f.write(f'<html><head><title>Bookmarks</title></head><body>{output}</body></html>')
        f.write(f'<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n<title>Bookmarks</title>\n<style>\n    body {{ font-family: Arial, sans-serif; }}\n    h1 {{ text-align: center; }}\n    ul {{ list-style-type: none; padding: 0; margin: 0; }}\n    ul ul {{ margin-left: 15px; }}\n    a {{ text-decoration: none; color: #428bca; }}\n    a:hover {{ text-decoration: underline; }}\n</style>\n</head>\n<body>\n<h1>Bookmarks</h1>\n<ul>{output}</ul>\n</body>\n</html>')

elif save_format == 'PDF':
    with open('bookmarks.html', 'w') as f:
        f.write(f'<html><head><title>Bookmarks</title></head><body>{output}</body></html>')
    os.system('pandoc bookmarks.html -o bookmarks.pdf')
    os.remove('bookmarks.html')
elif save_format == 'TXT':
    with open('bookmarks.txt', 'w') as f:
        f.write(output)
    
print(f'Bookmarks saved as {save_format.lower()}')
