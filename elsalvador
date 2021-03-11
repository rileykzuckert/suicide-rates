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
def elsalvador(file):
    '''
    This function deciphers which year of the Salvadoran Civil War had the greatest number of suicides\n
    between men and women ages 15-24 and across years 1990-1992.
    Parameters:
        :file: name of csv file
    Returns: 
        A bar chart visualization of the suicide rate.
    '''
    df = pd.read_csv('master.csv', index_col=[0])
    elsalvador = df.loc['El Salvador', 'year':'suicides_no']
    yr_1990 = elsalvador.iloc[[2,3], 3]
    yr_1991 = elsalvador.iloc[[14,16], 3]
    yr_1992 = elsalvador.iloc[[28,37], 3]
    index = [1990, 1991, 1992]
    data = [[127, 112], [98, 97], [83, 87]]
    columns = ['Male Ages 15-24', 'Female Ages 15-24']
    df = pd.DataFrame(data, index, columns)
    df.plot.bar(color=['lightskyblue', 'lightpink'])
    #x_ticks = [1990, 1991, 1992]
    plt.xticks(rotation='horizontal')
    plt.title('Frequency Distribution of Suicide Rates\n During the Salvadoran Civil War, 1990-1992', weight='bold')
    plt.xlabel('Year', size=12, weight='bold')
    plt.ylabel('Frequency of Suicides', size=12, weight='bold')
    ax = plt.gca()
    ax.set_facecolor('aliceblue')
    
#==========================================================
def main():
    '''
    This file runs three tests extracting information from "master.csv" and creating visualizations\n
    of the three chosen countries' data.
    '''
    elsalvador('master.csv')
    plt.show()
    
if __name__ == '__main__':
    main()
