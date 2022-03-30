import io
import pandas as pd
import glob

def first_dataframe():
    myDF = df = pd.DataFrame(
        {
            "Name": [
                "Braund, Mr. Owen Harris",
                "Allen, Mr. William Henry",
                "Bonnell, Miss. Elizabeth",
                ],
            "Age": [22, 35, 58],
            "Sex": ["male", "male", "female"],
        }
    )
    print(myDF)

# Create a DataFrame from a set of Series objects
# https://stackoverflow.com/questions/23521511/pandas-creating-dataframe-from-series
def df_from_series():
    cols = ['id','name','amount']
    index = [0,1,2,3]
    idCol = pd.Series([1,2,3,4],index)
    nameCol = pd.Series(['Fred','Wilma','Barney','Betty'],index)
    amountCol = pd.Series([2000,2400,1800,2900],index)
    peopleColList = [idCol,nameCol,amountCol]
    peopleDF = pd.DataFrame(peopleColList,cols).transpose()
    print(peopleDF)
    print('Max age: '+str(peopleDF['amount'].max())+'\n'
        +'Min age: '+str(peopleDF['amount'].min())+'\n'
        +'Avg age: '+str(peopleDF['amount'].mean())+'\n'
        )
    print(peopleDF.describe())

def df_from_csv_file():
    basedir = '/home/keith/Documents/git-repos/github/jkeithr01/study/data'
    file = '/people.csv/initial/lucy.csv'
    load_target = basedir+file
    lucyDF = pd.read_csv(load_target)
    print(lucyDF)

def df_from_csv_files():
    path = r'/home/keith/Documents/git-repos/github/jkeithr01/study/data/people.csv'
    all_files = glob.glob(path + '/*/*.csv')
    peopleDF = pd.concat((pd.read_csv(f) for f in all_files))
    print(peopleDF)

def main():
    first_dataframe()
    df_from_series()
    df_from_csv_file()
    df_from_csv_files()

if __name__ == "__main__":
	main()
