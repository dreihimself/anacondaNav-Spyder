# -*- coding: utf-8 -*-
"""
Created on Sun Sept  2 14:58:34 2022

@author: Paolo Hilado
"""

# Activity 5 -------------------------------------------------
# Descriptive Analytics on file 'Plant Experiment.xlsx' 
# Work on Variable: Weight
# Load necessary packages
print(os.getcwd())
import pandas as pd
# Load dataset to variable df
df = pd.read_excel('PlantExperiment.xlsx')
# Check for missing cases
df.isnull().values.any()
# Check structure of dataframe
df.info()

# Exploratory Data Analysis
#Conduct Normality testing
# Null Hypothesis: The distribution is approximately normal
import scipy.stats as stats
Wtx = df[(df['Group'] == 'Treatment')].Weight
Wcon = df[(df['Group'] == 'Control')].Weight
stats.anderson(Wtx, dist='norm')
stats.anderson(Wcon, dist='norm')
# Data Visualization - Boxplot
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
sns.set(style = "whitegrid")
plt.figure(figsize=(10,8))
ax = sns.boxplot(x = 'Group', y = 'Weight', data=df, orient="v")

# Data Visualization - Distribution plot
sns.set(style = "whitegrid")
plt.figure(figsize=(10,8))
bx = sns.distplot(df[df["Group"]== "Control"].Weight)
cx = sns.distplot(df[df["Group"]== "Treatment"].Weight)
# Conduct Test for Homogeneity
stats.levene(Wtx, Wcon, center='mean')

#Descriptive Analysis
Desc = df['Weight'].groupby(df['Group']).describe()
Desc.to_csv("DescRes.csv")

#Inferential Analysis
# Condition: Distributions Approximately Normal | Variance is Homogenous
import researchpy as rp
rp.ttest(Wtx, Wcon, equal_variances= True, paired= False)


# Activity 6 -------------------------------------------------
# Descriptive Analytics on file 'SleepData.xlsx'
# Work on Variable Sleep per Employment
# Load necessary packages
import pandas as pd
# Load dataset to variable df
df = pd.read_excel('SleepData.xlsx')
# Check for missing cases
df.isnull().values.any()
# Check structure of dataframe
df.info()

# Exploratory Data Analysis
#Conduct Normality testing
# Null Hypothesis: The distribution is approximately normal
import scipy.stats as stats
df = df.rename(columns= {"sleep(hrs)/weeknights":"Sleep"})
SlpPerm = df[(df['Employment'] == 'Permanent')].Sleep
SlpProb = df[(df['Employment'] == 'Probationary')].Sleep
stats.anderson(SlpPerm, dist='norm')
stats.anderson(SlpProb, dist='norm')
# Data Visualization - Boxplot
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
sns.set(style = "whitegrid")
plt.figure(figsize=(10,8))
ax = sns.boxplot(x = 'Employment', 
                 y = 'Sleep', 
                 data=df, 
                 orient="v")

# Data Visualization - Distribution plot
sns.set(style = "whitegrid")
plt.figure(figsize=(10,8))
bx = sns.distplot(SlpPerm)
cx = sns.distplot(SlpProb)

# Data Visualization - Quartile - Quartile Plots
import statsmodels.api as sm
sm.qqplot(SlpPerm, line="s")
sm.qqplot(SlpProb, line="s")

# Conduct Test for Homogeneity
stats.levene(SlpPerm, SlpProb, center='mean')

#Descriptive Analysis
Desc = df['Sleep'].groupby(df['Employment']).describe()
Desc.to_csv("DescRes.csv")


#Inferential Analysis
# Condition: Distributions Approximately Normal | Variance is not Homogenous
import researchpy as rp
rp.ttest(SlpProb, SlpPerm, equal_variances= False, paired= False)



# Activity 7 -------------------------------------------------
# Descriptive Analytics on file 'PlantExperiment.xlsx'
# Work on Variable Length
# Load necessary packages

# Load dataset to variable df

# Check for missing cases

# Check structure of dataframe


# Exploratory Data Analysis
#Conduct Normality testing
# Null Hypothesis: The distribution is approximately normal


# Data Visualization - Boxplot


# Data Visualization - Distribution plot


# Conduct Test for Homogeneity
# Null Hypothesis: The variances are Homogenous


#Descriptive Analysis



#Inferential Analysis
# Condition: Distributions Approximately Normal | Variance is not Homogenous



