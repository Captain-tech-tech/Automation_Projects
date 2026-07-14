from utils.file_handler import load_dataset
import pandas as pd

def main():
    path = input("Enter the path of the file: ")
    dataframe = load_dataset(path)
    print(dataframe.head())



main()


print("Rest of the code")
