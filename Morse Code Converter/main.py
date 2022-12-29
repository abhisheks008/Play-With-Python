from tkinter import *
from tkinter import ttk

from morse import MorseCode


if __name__ == '__main__':
        morse = MorseCode()
        window = Tk()

        window.title('Morse Code Converter')
        window.geometry('500x650')
        window.resizable(0, 0)

        window.config(
            background='#eeeeee'
        )

        Label(
            window,
            text='Morse Code',
            font=('hack', 20, 'bold'),
            bg='#eeeeee',
            fg='#000000'
        ).pack(fill=X, pady=10)

        ttk.Separator(window).pack(fill=X)

        Label(
            window,
            text='Encryptor',
            font=('hack', 15, 'bold'),
            bg='#eeeeee',
            fg='#000000'
        ).pack(fill=X, pady=10)

        Message(
            window,
            text='Note: Letters will be separated by a space and words will be separated by two spaces',
            font=('hack', 10, 'bold'),
            width=450,
            bg='#eeeeee',
            fg='#000000'
        ).pack(fill=X, padx=10, pady=(0, 10))

        morse_code_e = StringVar()
        Entry(
            window,
            textvariable=morse_code_e,
            font=('hack', 15),
            bg='#ffffff',
            fg='#000000'
        ).pack(fill=X, padx=20)

        def encoder_button():
            text_e.set(morse.encryptor(morse_code_e.get()))

        Button(
            window,
            text='Encode',
            command=encoder_button,
            font=('hack', 12),
            bg='#eeeeee',
            fg='#000000'
        ).pack(pady=10)

        text_e = StringVar()
        Entry(
            window,
            textvariable=text_e,
            font=('hack', 15),
            bg='#ffffff',
            fg='#000000'
        ).pack(fill=X, padx=20)

        ttk.Separator(window).pack(fill=X, pady=10)

        Label(
            window,
            text='Decrypter',
            font=('hack', 15, 'bold'),
            bg='#eeeeee',
            fg='#000000'
        ).pack(fill=X, pady=10)

        Message(
            window,
            text='Note: Separate letters with one space and words with two spaces',
            font=('hack', 10, 'bold'),
            width=450,
            bg='#eeeeee',
            fg='#000000'
        ).pack(fill=X, padx=10, pady=(0, 10))

        morse_code_d = StringVar()
        Entry(
            window,
            textvariable=morse_code_d,
            font=('hack', 15),
            bg='#ffffff',
            fg='#000000'
        ).pack(fill=X, padx=20)

        def decoder_button():
            text_d.set(morse.decrypter(morse_code_d.get()))

        Button(
            window,
            text='Decode',
            command=decoder_button,
            font=('hack', 12),
            bg='#eeeeee',
            fg='#000000'
        ).pack(pady=10)

        text_d = StringVar()
        Entry(
            window,
            textvariable=text_d,
            font=('hack', 15),
            bg='#ffffff',
            fg='#000000'
        ).pack(fill=X, padx=20)

        def exit_button():
            print('Program is terminated!')
            window.destroy()

        Button(
            window,
            text='Exit',
            command=exit_button,
            font=('hack', 12),
            bg='#eeeeee',
            fg='#000000'
        ).pack(pady=50)

        window.mainloop()
