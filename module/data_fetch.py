import pandas as pd
import os


class Modularization:


    def __init__(self):
        print("Import the module you need...")


    def fetch(self,filepaths):

       self.filepaths=filepaths
       for fp in self.filepaths:
        # Split the extension from the path and normalise it to lowercase.
        ext = os.path.splitext(fp)[-1].lower()

        # Now we can simply use == to check for equality, no need for wildcards.
        if ext == ".csv":
            print(fp, "is an csv!")
            self.dataset = pd.read_csv(fp)
            return self.dataset

        elif ext == ".xlsx":
             print(fp, "is a excel file!")
             self.dataset = pd.read_excel(fp)
             return self.dataset

        elif ext == ".txt":
             print(fp, "is a text file!")
             self.dataset = pd.read_fwf(fp)
             return self.dataset

        elif ext == ".html":
             print(fp, "is a url file!")
             self.dataset = pd.read_html(fp)
             return self.dataset

        elif ext == ".pkl":
             print(fp, "is a pickel file!")
             self.dataset = pd.read_pickle(fp)
             return self.dataset

        elif ext == ".pkl":
             print(fp, "is a pickel file!")
             self.dataset = pd.read_pickle(fp)
             return self.dataset

        elif ext == ".parquet":
             print(fp, "is a parquet file!")
             self.dataset = pd.read_parquet(fp)
             return self.dataset

        # elif ext == ".sql":
        #      print(fp, "is a database file!")
        #      self.dataset = pd.read_sql(fp,con="")
        #      print(self.dataset)
        else:
            print(fp, "is a non-supported file format.")


if __name__=="__main__":

    module=Modularization()
    module.fetch(filepaths = ["../../datasets/dataset1.csv", "../../datasets/salaries.csv"])



