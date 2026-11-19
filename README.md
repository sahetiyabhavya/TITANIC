#  Titanic Data Analysis

### A Python-based data analysis project to explore Titanic passenger data, survival rates, age, fare, passenger class, and family size.

---

##  Project Overview

This project analyzes the Titanic dataset using Python.  
It helps us understand which passengers survived, how survival changed by gender, passenger class, age, fare, and family size.

The project includes data cleaning, exploratory data analysis, visualizations, and result interpretation.

---

##  Dataset

The dataset contains information about Titanic passengers

### Dataset Columns

| Column Name | Description |
|---|---|
| PassengerId | Unique ID of each passenger |
| Survived | Survival status: 0 = Not Survived, 1 = Survived |
| Pclass | Passenger class: 1, 2, or 3 |
| Name | Passenger name |
| Sex | Gender of the passenger |
| Age | Age of the passenger |
| SibSp | Number of siblings or spouses aboard |
| Parch | Number of parents or children aboard |
| Ticket | Ticket number |
| Fare | Ticket fare |
| Cabin | Cabin number |
| Embarked | Port of embarkation |

---

##  Technologies Used

- NumPy
- Matplotlib
- Python
- Seaborn
- Jupyter Notebook
- Pandas


---

##  Data Analysis Performed

- Family Size and Survival Analysis
- Top Passenger Classes with Highest Survival Rate
- Missing Age Data and Survival Analysis
- Final Titanic Report
- Average Age by Survival
- Minimum and Maximum Passenger Class by Survival
- Survival and Passenger Class Analysis by Sex
- Most Expensive Fare and Its Survival Rate


---

##  Project Structure

```text
 
│
├── main.ipynb
├── README.md
└── titanic.csv 
```

### Files Description

| File Name | Description |
|---|---|
| `titanic_analysis.ipynb` | Main Jupyter Notebook containing the complete analysis |
| `titanic.csv` | Dataset used for analysis |
| `README.md` | Project documentation |

---

##  Installation

Make sure Python is installed on your system.

Install the required libraries using this command:

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

---

##  How to Run

1. Download or clone this project.
2. Open the `titanic` folder.
3. Open Command Prompt or Terminal in that folder.
4. Run Jupyter Notebook:

```bash
jupyter notebook
```

5. Open `titanic_analysis.ipynb`.
6. Run all cells one by one.
7. Check the analysis results and graphs.


---

##  Visualizations

- Passenger Class vs Average Age Line Chart
- Survival Rate by Sex Bar Chart
- Age vs Fare Scatter Plot
- Age Distribution Histogram
- Correlation Heatmap
- Survival Rate by Passenger Class Pie Chart


---

##  Future Improvements

- Add more Titanic datasets.
- Perform machine learning-based survival prediction.
- Analyze cabin and ticket data in more detail.
- Create interactive dashboards.
- Compare survival rates across different age groups.


---

##  Key Insights

- Passenger class affected survival rate.
- Female passengers had a higher survival rate compared to male passengers.
- Age and fare showed variation among passengers.
- Missing age data was analyzed separately.
- Family size may have affected survival chances.
- This analysis shows observed data patterns, not direct cause-and-effect.


---

##  Author
Bhavya sahetiya  