import os
import platform
import tkinter as tk
from tkinter import filedialog, messagebox


def export_bookmarks(save_format):
    if platform.system() == 'Windows':
        home_dir = os.path.expanduser('~').replace('\\', '/')
    else:
        home_dir = os.path.expanduser('~')

    chrome_bookmarks_file = f'{home_dir}/AppData/Local/Google/Chrome/User Data/Default/Bookmarks'

    cmd = f'powershell -Command "$json = Get-Content \'{chrome_bookmarks_file}\' -Raw | ConvertFrom-Json; $bookmarks = $json.roots.bookmark_bar.Children + $json.roots.other.Children; $output = \'\'; foreach ($bookmark in $bookmarks) {{ $folder = $bookmark.Parent; while ($folder) {{ $output += \'&nbsp;&nbsp;&nbsp;&nbsp;\'; $folder = $folder.Parent }}; $output += $bookmark.Name + \' => \' + $bookmark.Url + \'&lt;br&gt;\'; }}; $output"'

    output = os.popen(cmd).read()

    if save_format == 'HTML':
        with open('bookmarks.html', 'w') as f:
            f.write(f'<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n<title>Bookmarks</title>\n<style>\n    body {{ font-family: Arial, sans-serif; }}\n    h1 {{ text-align: center; }}\n    ul {{ list-style-type: none; padding: 0; margin: 0; }}\n    ul ul {{ margin-left: 15px; }}\n    a {{ text-decoration: none; color: #428bca; }}\n    a:hover {{ text-decoration: underline; }}\n</style>\n</head>\n<body>\n<h1>Bookmarks</h1>\n<ul>{output}</ul>\n</body>\n</html>')
        messagebox.showinfo('Export Complete', f'Bookmarks saved as {save_format.lower()}')
    elif save_format == 'PDF':
        with open('bookmarks.html', 'w') as f:
            f.write(f'<html><head><title>Bookmarks</title></head><body>{output}</body></html>')
        os.system('pandoc bookmarks.html -o bookmarks.pdf')
        os.remove('bookmarks.html')
        messagebox.showinfo('Export Complete', f'Bookmarks saved as {save_format.lower()}')
    elif save_format == 'TXT':
        with open('bookmarks.txt', 'w') as f:
            f.write(output)
        messagebox.showinfo('Export Complete', f'Bookmarks saved as {save_format.lower()}')


def select_save_format():
    selected_format = format_var.get()
    export_bookmarks(selected_format)


root = tk.Tk()
root.title('Bookmark Exporter')

format_var = tk.StringVar()
format_var.set('HTML')

html_radio = tk.Radiobutton(root, text='HTML', variable=format_var, value='HTML')
pdf_radio = tk.Radiobutton(root, text='PDF', variable=format_var, value='PDF')
txt_radio = tk.Radiobutton(root, text='TXT', variable=format_var, value='TXT')

export_button = tk.Button(root, text='Export', command=select_save_format)

html_radio.pack()
pdf_radio.pack()
txt_radio.pack()
export_button.pack()

root.mainloop()
