'''
Author: Riley Zuckert
Date: November 21, 2020
Class: ISTA131
Section Leader: Peter Ojum
Assignment: Final Project

Description:
This file extracts information from "master.csv" and creates visualizations of the suicide rates\n
according to different criteria in the countries El Salvador, Mexico, and Paraguay.
'''
import pandas as pd, numpy as np, matplotlib.pyplot as plt, statsmodels.api as sm
def paraguay(file):
    '''
    This function deciphers which year had the greatest number of suicides from men ages 25-34\n
    during the Insurgency in Paraguay.
    Parameters:
        :file: name of csv file
    Returns: 
        A scatterplot visualization of the suicide rate.
    '''
    df = pd.read_csv('master.csv', index_col=[0])
    paraguay = df.iloc[18768:18888, :4]
    yr_2005 = paraguay.iloc[5,3]
    yr_2006 = paraguay.iloc[15,3]
    yr_2007 = paraguay.iloc[25,3]
    yr_2008 = paraguay.iloc[37,3]
    yr_2009 = paraguay.iloc[51,3]
    yr_2010 = paraguay.iloc[62,3]
    yr_2011 = paraguay.iloc[74,3]
    yr_2012 = paraguay.iloc[86,3]
    yr_2013 = paraguay.iloc[98,3]
    yr_2014 = paraguay.iloc[109,3]
    index = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014]
    data = [24, 36, 40, 43, 43, 36, 57, 41, 60, 62]
    columns = ['Men Ages 25-35']
    df = pd.DataFrame(data, index, columns)
    plt.scatter(x=index, y=data, color='deeppink')
    plt.title('Frequency Distribution of the Suicide Rate During the\n Insurgency in Paraguay of Men Ages 25-34, 2005-2014', weight='bold')
    plt.xlabel('Year', size=12, weight='bold')
    plt.ylabel('Frequency of Suicides', size=12, weight='bold')
    x = df.index.values
    X = sm.add_constant(x)
    model = sm.OLS(df, X)
    line = model.fit()
    y = line.params['x1'] * x + line.params['const']
    plt.plot(x, y, color='lightpink')
    ax = plt.gca()
    ax.set_facecolor('aliceblue')
    plt.grid()

#==========================================================
def main():
    '''
    This file runs three tests extracting information from "master.csv" and creating visualizations\n
    of the three chosen countries' data.
    '''
    paraguay('master.csv')
    plt.show()

if __name__ == '__main__':
    main()
