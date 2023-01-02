# CSV to JSON Converter

**Approach** 
- import `tkinter`, `csv` and `json`
- create a JSON_file dictionary, each representing a record (row) from the CSV file, with the Key as the column specified. 
- use `csv.DictReader()` to read the csv file
- use `jsonfile.write()` to write the data that collected from csv file where `jsonfile` contains the .json file path with write mode

**Demostration**
Sample .csv file :

![image](https://github.com/vamsikrishnarh7/Play-With-Python/blob/main/CSV%20to%20JSON%20Converter/images/sample%20csv%20file.png)


GUI looks like below :

![image](https://github.com/vamsikrishnarh7/Play-With-Python/blob/main/CSV%20to%20JSON%20Converter/images/gui1.png)

![image](https://github.com/vamsikrishnarh7/Play-With-Python/blob/main/CSV%20to%20JSON%20Converter/images/gui2.png)


Output : 

![image](https://github.com/vamsikrishnarh7/Play-With-Python/blob/main/CSV%20to%20JSON%20Converter/images/sample%20json%20output.png)
