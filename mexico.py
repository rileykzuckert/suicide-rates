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
def mexico(file):
    '''
    This function deciphers which male age range has the greatest number of suicides from year 2015\n
    of the Mexican Drug War.
    Parameters:
        :file: name of csv file
    Returns: 
        A pie chart visualization of the suicide rate.
    '''
    df = pd.read_csv('master.csv', index_col=[0])
    mexico = df.loc['Mexico', 'year':'suicides_no']
    five_14 = mexico.iloc[-3, 3]
    fifteen_24 = mexico.iloc[-11, 3]
    twentyfive_34 = mexico.iloc[-12, 3]
    thirtyfive_54 = mexico.iloc[-9, 3]
    fiftyfive_74 = mexico.iloc[-8, 3]
    seventyfive = mexico.iloc[-10, 3]
    index = ['5-14', '15-24', '25-34', '35-54', '55-74', '75+']
    data = [137, 1347, 1195, 1560, 584, 163]
    df = pd.DataFrame(data, index)
    colors = ['palegoldenrod', 'lightcoral', 'paleturquoise', 'hotpink', 'cornflowerblue', 'plum']
    explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
    labels = ['5-14 Years', '15-24 Years', '25-34 Years', '35-54 Years', '55-74 Years', '75+ Years']
    sizes = [2.75, 27.02, 23.97, 31.29, 11.71, 3.27]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, autopct='%1.1f%%', shadow=False, startangle=90, textprops={'fontsize':8}, explode=(0, 0, 0, 0, 0, 0.1), colors=colors, labeldistance=1.05)
    ax1.legend(labels, title='Age Groups', loc='upper left')
    ax1.axis('equal')
    plt.title('Percentage Frequency Distribution of\n Male Suicides During the Mexican Drug War, 2015', weight='bold')
    
#==========================================================
def main():
    '''
    This file runs three tests extracting information from "master.csv" and creating visualizations\n
    of the three chosen countries' data.
    '''
    mexico('master.csv')
    plt.show()
    
if __name__ == '__main__':
    main()
