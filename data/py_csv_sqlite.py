#!/usr/bin/python
import csv
import sqlite3
import os
import fnmatch

UP_FOLDER = os.path.dirname(os.getcwd())
DATABASE_FOLDER = os.path.join(UP_FOLDER, "Databases")
DBNAME = "ml_data.db"


def getBaseNameNoExt(givenPath):
    """Returns the basename of the file without the extension"""
    filename = os.path.splitext(os.path.basename(givenPath))[0]
    return filename


def find(pattern, path):
    """Utility to find files wrt a regex search"""
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


if __name__ == "__main__":
    Database_Path = os.path.join(DATABASE_FOLDER, DBNAME)

    # change to 'sqlite:///your_filename.db'
    csv_files = find('*.csv', DATABASE_FOLDER)
    con = sqlite3.connect(Database_Path)
    cur = con.cursor()
    for each in csv_files:
        with open(each, 'r') as fin:  # `with` statement available in 2.5+
            # csv.DictReader uses first line column headings by default
            dr = csv.DictReader(fin)  # "," by default
            TABLE_NAME = getBaseNameNoExt(each)
            Cols = dr.fieldnames
            numCols = len(Cols)
            # [print(i.values()) for i in dr]
            to_db = [tuple(i.values()) for i in dr]
            print(TABLE_NAME)

            # use your column names here
            ColString = ','.join(Cols)
            QuestionMarks = ["?"] * numCols
            ToAdd = ','.join(QuestionMarks)
            cur.execute(f"CREATE TABLE {TABLE_NAME} ({ColString});")
            cur.executemany(
                f"INSERT INTO {TABLE_NAME} ({ColString}) VALUES ({ToAdd});", to_db)
            con.commit()
    con.close()
    print("Execution Complete!")
