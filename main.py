import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

print("========== Titanic Survival DATA ANALYSIS ==========")
try : 
    
    path = input("Enter Dataset Path (e.g. data/sales_data.csv): ").strip()
    data = pd.read_csv(path) 
    print("Data Loaded Successfully!")
    
except :
    print('File Not Found')

print("========== EXPLORE DATASET ==========")
print("1. Display First 5 Rows")
print("2. Display Last 5 Rows")
print("3. Display Column Names")
print("4. Display Data Types")
print("5. Display Dataset Information")
print("6. Display Statistical Summary")

try :
    choice = input("Enter Your Choice: ")

    if choice == '1' :
        print(data.head())

    elif choice == '2' :
        print(data.tail())

    elif choice == '3' :
        print(data.columns)

    elif choice == '4' :
        print(data.dtypes)

    elif choice == '5' :
        print(data.info())

    elif choice == '6' :
        print(data.describe())

    else :
        print("Enter Valid Choice!")

except :
    print("First load Dataset")

print("========== CLEAN DATASET ==========")
print("1. Display Rows with Missing Values")
print("2. Fill Missing Values with Mean")
print("3. Drop Rows with Missing Values")
print("4. Fill Missing Values With First ")


try :
    choice = input("Enter Your Choice: ")

    if choice == '1' :
        print(data.isnull().sum())

    elif choice == '2' :
        print(data.fillna().mean(numeric_only=True))
        print(data.isnull().sum())

    elif choice == '3' :
        print(data.dropna(inplace=True))
        print(data.isnull().sum())

    elif choice == '4' :
        print(data.ffill())

    else :
        print("Invalid Choice!")

except :
    print(" First load Dataset!")


print("========== TITANIC ADVANCED ANALYSIS ==========")
print("1. Calculate Survival Rate by Age Group")
print("2. Find Highest and Lowest Survival Rate by Passenger Class")
print("3. Analyze Survival Rate by Gender and Passenger Class")
print("4. Find Most Expensive Fare and Its Survival Rate")
print("5. Analyze Family Size and Survival")
print("6. Find Top 5 Passenger Classes with Highest Survival Rate") 
print("7. Create Final Titanic Report")

try :
    choice = input("Enter Your Choice: ")

    if choice == '1' :
        print(data.groupby('Survived')['Age'].mean().round(2))

    elif choice == '2' :
        print("Minimum", data.groupby('Survived')['Pclass'].min())
        print("Maximum", data.groupby('Survived')['Pclass'].max())

    elif choice == '3' :
        print(data.groupby('Gender')[['Survived','Pclass']].sum())

    elif choice == '4' :
        print("Most Expensive Fare:", data["Fare"].max())

    elif choice == '5' : 
        data['Family Size'] = data['SibSp'] + data['Parch'] + 1
        print(data.groupby('Family Size')['Survived'].mean() * 100)

    elif choice == '6': 
        print((data.groupby('Pclass')['Survived'].mean() * 100).round(2).sort_values(ascending=False).head(5))

    elif choice == '7':
        print("========== FINAL TITANIC REPORT ==========")
        print("Total Passengers:", len(data))
        print("Total Survived:", data['Survived'].sum())
        print("Total Not Survived:", len(data) - data['Survived'].sum())
        print("Overall Survival Rate:", (data['Survived'].mean() * 100).round(2))
        print(data[['Survived', 'Pclass', 'Age', 'Fare']].describe())

    else:
        print("Invalid Choice.")

except :
    print("First load Dataset!") 

print("========== TITANIC DATA VISUALIZATION ==========")
print("1. Passenger Class vs Average Age Line Chart")
print("2. Survival Rate by Gender Bar Chart")
print("3. Age vs Fare Scatter Plot")
print("4. Survival Rate by Passenger Class Pie Chart")
print("5. Age Distribution Histogram")
print("6. Correlation Heatmap")

try :
    choice = input("Enter Your Choice: ")

    if choice == '1' :
        data1 = data.groupby('Pclass')['Age'].mean().reset_index()
        sns.lineplot(
            data = data1,
            x='Pclass',
            y='Age',
            marker='*'
        )
        plt.title('Passenger Class vs Average Age Chart')
        plt.xticks(rotation=45)
        plt.xlabel('Passenger Class')
        plt.ylabel('Age')
        plt.legend()
        plt.tight_layout()
        plt.show()

    elif choice == '2' :
        data2 = data.groupby('Gender')['Survived'].mean().reset_index()
        sns.barplot(
            data= data2,
            x= 'Gender',
            y= 'Survived',
            hue= 'Gender')
        
        plt.title('Survival Rate by Gender Bar Chart')
        plt.xticks(rotation=45)
        plt.xlabel('Passenger Class')
        plt.ylabel('Age')
        plt.legend()
        plt.tight_layout()
        plt.show()

    elif choice == '3':
        sns.scatterplot(x='Age', y='Fare', data=data, hue='Survived')
        plt.title("Age vs Fare Scatter Plot")
        plt.xlabel("Age")
        plt.ylabel("Fare")
        plt.legend(title="Survived")
        plt.show()

    elif choice == '4':
        survival_rate = data.groupby('Pclass')['Survived'].mean() * 100

        plt.figure(figsize=(6, 6))
        plt.pie(survival_rate, labels=survival_rate.index, autopct='%1.2f%%')
        plt.legend()
        plt.title("Survival Rate by Passenger Class")
        plt.show()

    elif choice == '5':
        sns.histplot(data['Age'], bins=20, kde=True)
        plt.title("Age Distribution Histogram")
        plt.xlabel("Age")
        plt.ylabel("Count")
        plt.show()

    elif choice == '6':
        numeric_data = data[['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']]
        sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0)
        plt.title("Correlation Heatmap")
        plt.show()

    else:
        print("Enter Valid Choice!")

except :
    print("First load Dataset !")

print("========== TITANIC DATA ANALYSIS ==========")
print("1. Calculate Average Age by Survival")
print("2. Find Minimum and Maximum Passenger Class by Survival")
print("3. Analyze Survival and Passenger Class by Sex")
print("4. Find Most Expensive Fare and Its Survival Rate")
print("5. Analyze Family Size and Survival")
print("6. Find Top 5 Passenger Classes with Highest Survival Rate")
print("7. Analyze Missing Age Data and Survival")
print("8. Create Final Titanic Report")
try:
        
    choice = input("Enter Your Choice: ")

    if choice == '1':
        print(data.groupby('Survived')['Age'].mean().round(2))

    elif choice == '2':
        print("Minimum:", data.groupby('Survived')['Pclass'].min())
        print("Maximum:", data.groupby('Survived')['Pclass'].max())

    elif choice == '3':
        print(data.groupby('Gender')[['Survived', 'Pclass']].mean())

    elif choice == '4':
        print("Most Expensive Fare:", data['Fare'].max())
        highest_fare = data['Fare'].max()
        highest_fare_data = data[data['Fare'] == highest_fare]
        print("Survival Rate for Most Expensive Fare:", (highest_fare_data['Survived'].mean() * 100).round(2))

    elif choice == '5':
        data['Family Size'] = data['SibSp'] + data['Parch'] + 1
        print(data.groupby('Family Size')['Survived'].mean() * 100)

    elif choice == '6':
        print((data.groupby('Pclass')['Survived'].mean() * 100).round(2).sort_values(ascending=False).head(5))

    elif choice == '7':
        missing_age = data[data['Age'].isnull()]
        print("Total Missing Age Records:", len(missing_age))
        print("Survival Rate for Missing Age Data:", (missing_age['Survived'].mean() * 100).round(2))

    elif choice == '8':
        print("========== FINAL TITANIC REPORT ==========")
        print("Total Passengers:", len(data))
        print("Total Survived:", data['Survived'].sum())
        print("Total Not Survived:", len(data) - data['Survived'].sum())
        print("Overall Survival Rate:", (data['Survived'].mean() * 100).round(2))
        print(data[['Survived', 'Pclass', 'Age', 'Fare']].describe())

    else:
        print("Invalid Choice!")

except :
    print("First load Dataset!")

