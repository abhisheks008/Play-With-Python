# Speech to Text App

This is done with the help of Google Speech Recognition.
*This requires an active internet connection to work*. However, there are certain offline Recognition systems such as PocketSphinx,
but have a very rigorous installation process that requires several dependencies. Google Speech Recognition is one of the easiest to use. 

## Insatllation Required
- Python speech recognition module

  ```pip install speechrecognition```
- Python pyttsx3 module: 

  ```pip install pyttsx3```

## Approach

This app build using `tkinter 3.9.14`, `speechrecognition` and `pyttsx3`.
- Import the `tkinter`, `speechrecognition` and `pyttsx3` modules.
- initiate `Recognizer()`
- access microphone using `Microphone()` and use `listen()` to listen what you are saying
- convert the speech to text using `recognize_google()` by passing the speech that is collected using `listen()`

## Demonstration



https://user-images.githubusercontent.com/89008784/209456864-90e11a0c-f7f7-4356-97ac-55aae59a46bd.mp4



[**Durga Vamsi Krishna**](https://github.com/vamsikrishnarh7/)
