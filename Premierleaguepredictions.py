# Coded by Prajwal
# Program to build Multiple linear regression(MLR) models between Total points accumulated by a Premier league team with the independent variables like TotalWins,TotalDraws,TotalLosses,TotalGoalsscored, TotalGoalsconceded etc.
# Using the above models for the 2015-16, 2016-17 and 2017-18 seasons I will try to predict the Premier league winners for the current season

import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import numpy as np
import seaborn as sns
import statsmodels.formula.api as sm


# Program to plot teams and a few parameters such as total points, home points and away points accumulated over the season
# Taking the input of the season in excel format, for which the graphs have to be plotted
reqdseason = input("Enter the season to display the table in the format 'YYYY-YY.xlsx'=")
if(reqdseason!='2015-16.xlsx' and reqdseason!='2016-17.xlsx' and reqdseason!='2017-18.xlsx'):
    print("Either The entered season doesn't exist or the format entered is incorrect\n\n")

# Read the "Table" sheet in the inputted excel file
data_set=pd.read_excel(reqdseason,sheet_name='Table')

team=data_set.Teams

#Printing out a few important stats from the selected season
#Printing out the winners and the points they accumulated during the season
maxpts = data_set['TotalPts'].max()
winners = data_set.Teams[0]
print("The winners of this season were ",winners," with ",maxpts," points")

#Printing out the relegated teams and the points they accumulated during the season
relegated1 = data_set.Teams[17]
pts_relegated1 = data_set.TotalPts[17]
relegated2 = data_set.Teams[18]
pts_relegated2 = data_set.TotalPts[18]
relegated3 = data_set.Teams[19]
pts_relegated3 = data_set.TotalPts[19]
print("The relegated teams were",relegated1,",",relegated2,"and",relegated3," with ",pts_relegated1,",",pts_relegated2,",","and",pts_relegated3,"points respectively")

#Printing the team who scored the most and the least number of goals
goals_scored = data_set['TotalGF'].max()
goals_scored1 = data_set['TotalGF'].min()
hs_1=data_set['TotalGF'].idxmax()
hs=data_set.Teams[hs_1]
ls_1=data_set['TotalGF'].idxmin()
ls=data_set.Teams[ls_1]
print("The highest scoring team in this season was",hs,"with",goals_scored,"goals")
print("The lowest scoring team in this season was",ls,"with",goals_scored1,"goals")

#Printing the team who conceded the most and the least number of goals
goals_conceded = data_set['TotalGC'].max()
goals_conceded1 = data_set['TotalGC'].min()
hc_1=data_set['TotalGC'].idxmax()
hc=data_set.Teams[hc_1]
lc_1=data_set['TotalGC'].idxmin()
lc=data_set.Teams[lc_1]
print("The team to concede the least number of goals in this season was",lc,"with",goals_conceded1,"goals")
print("The team to concede the highest number of goals in this season was",hc,"with",goals_conceded,"goals")

#Printing the team that conceded the most fouls and accumulated the most yellow cards
fouls_conceded = data_set['FOULS'].max()
yc_accumulated = data_set['YC'].max()
fc_1=data_set['FOULS'].idxmax()
fc=data_set.Teams[fc_1]
yca_1=data_set['YC'].idxmax()
yca=data_set.Teams[yca_1]
print("The team to concede the highest number of fouls this season was",fc,"with",fouls_conceded,"fouls")
print("The team to accumulate the most yellow cards this season was",yca,"with",yc_accumulated,"yellow cards")

#Printing the team with the best and the worst shot conversion ratio
#Shot conversion ratio = (Goals scored / Shots on target)
conv_h = round(data_set['Conversion'].max(),3)
conv_l = round(data_set['Conversion'].min(),3)
bestconv_1=data_set['Conversion'].idxmax()
bestconv=data_set.Teams[bestconv_1]
worstconv_1=data_set['Conversion'].idxmin()
worstconv=data_set.Teams[worstconv_1]
print("The team with the best shot conversion ratio this season was",bestconv,"with a conversion ratio of",conv_h)
print("The team with the worst shot conversion ratio this season was",worstconv,"with a conversion ratio of",conv_l)

# Plotting "Teams" vs the "Total points" they've accumulated over the season
pts=data_set.TotalPts
plt.bar(team,pts)
plt.xlabel('Teams')
plt.ylabel('Total points')
plt.suptitle('Teams vs Total points')
plt.show()


# Plotting "Teams" vs the "Total wins" they've accumulated over the season
plt.bar(team,data_set.TotalW)
plt.xlabel('Teams')
plt.ylabel('Total Wins')
plt.suptitle('Teams vs Total Wins')
plt.show()

# Plotting "Teams" vs the "Total draws" they've accumulated over the season
plt.bar(team,data_set.TotalD)
plt.xlabel('Teams')
plt.ylabel('Total Draws')
plt.suptitle('Teams vs Total Draws')
plt.show()

# Plotting "Teams" vs the "Total losses" they've accumulated over the season
plt.bar(team,data_set.TotalL)
plt.xlabel('Teams')
plt.ylabel('Total Losses')
plt.suptitle('Teams vs Total Losses')
plt.show()

# Plotting "Teams" vs the "Total goals scored" over the season
plt.bar(team,data_set.TotalGF)
plt.xlabel('Teams')
plt.ylabel('Total Goals Scored')
plt.suptitle('Teams vs Total Goals Scored')
plt.show()

# Plotting "Teams" vs the "Total goals conceded" over the season
plt.bar(team,data_set.TotalGC)
plt.xlabel('Teams')
plt.ylabel('Total Goals Conceded')
plt.suptitle('Teams vs Total Goals Conceded')
plt.show()

# Plotting "Teams" vs the "Total fouls" they've commited throughout the season
plt.bar(team,data_set.FOULS)
plt.xlabel('Teams')
plt.ylabel('Total Fouls')
plt.suptitle('Teams vs Total Fouls')
plt.show()

# Plotting "Teams" vs the "Total yellow cards" they've accumulated over the season
plt.bar(team,data_set.YC)
plt.xlabel('Teams')
plt.ylabel('Total Yellow cards')
plt.suptitle('Teams vs Total yellow cards')
plt.show()

# Plotting "Teams" vs the "Total red cards" they've accumulated over the season
plt.bar(team,data_set.RC)
plt.xlabel('Teams')
plt.ylabel('Total red cards')
plt.suptitle('Teams vs Total red cards')
plt.show()

# Plotting "Teams" vs the "Shot conversion ratio" they've accumulated over the season
plt.bar(team,data_set.Conversion)
plt.xlabel('Teams')
plt.ylabel('Shot conversion ratio')
plt.suptitle('Teams vs Shot conversion ratio')
plt.show()

#Displaying the table for the selected season
print("\nThe table for the selected season is:\n")
print(data_set)

# Plotting the variation in totalpts
sns.distplot(data_set['TotalPts'],hist=True,kde=True,bins=int(350/50),color='red')
plt.suptitle('Histogram displaying the distribution of the Total points')
plt.show()

#Plotting the relation between Total points and all the other variables in the file
print(pd.DataFrame(data_set.corr()['TotalPts']))
sns.pairplot(data=data_set,y_vars=['TotalPts'],x_vars=['TotalP','TotalW','TotalD','TotalL','TotalGF','TotalGC','HomePts','HomeP','HomeW','HomeD','HomeL','HomeGF','HomeGC','AwayPts','AwayP','AwayW','AwayD','AwayL','AwayGF','AwayGC','RC','YC','ST','FOULS','Conversion'])
plt.suptitle("Relationship b/w Total pts and the independent variables")
plt.show()


# Creating Multiple Linear Regression (MLR) Model for Total points w.r.t. the independent variables(i.e.Total points, Total Wins and so on
result = sm.ols(formula = "TotalPts ~ TotalP + TotalW + TotalD + TotalL + TotalGF + TotalGC + HomePts + HomeP + HomeW + HomeD + HomeL + HomeGF + HomeGC + AwayPts + AwayP + AwayW + AwayD + AwayL + AwayGF + AwayGC + RC + YC + FOULS + ST + Conversion", data=data_set).fit()
print("\nThe result parameters are:\n",result.params)
print("\nThe result summary is:\n",result.summary())

# Creating a reduced MLR model for Total points excluding some of the previously included independent variables such Total wins, total losses, home points, home wins, away points, away wins etc.
result_reduced = sm.ols(formula = "TotalPts ~ TotalGF + TotalGC + HomeGF + HomeGC + AwayGF + AwayGC + RC + YC + FOULS + ST + Conversion", data=data_set).fit()
print("The parameters of the reduced model are:\n",result_reduced.params)
print("\nThe Summary of the reduced model is:\n",result_reduced.summary())

#Boxplots to identify the outliers, to find the lower quartile (25th percentile), median (50th percentile), upper quartile (75th percentile) and the maximum of a continuous variable
fig, axs = plt.subplots(3,4)
axs[0, 0].boxplot(data_set['TotalGF'])
axs[0, 0].set_title('TotalGF')

axs[0, 1].boxplot(data_set['TotalGC'])
axs[0, 1].set_title('TotalGC')

axs[0, 2].boxplot(data_set['HomeGF'])
axs[0, 2].set_title('HomeGF')

axs[0, 3].boxplot(data_set['HomeGC'])
axs[0, 3].set_title('HomeGC')

axs[1, 0].boxplot(data_set['AwayGF'])
axs[1, 0].set_title('AwayGF')

axs[1, 1].boxplot(data_set['AwayGC'])
axs[1, 1].set_title('AwayGC')

axs[1, 2].boxplot(data_set['RC'])
axs[1, 2].set_title('RC')

axs[1, 3].boxplot(data_set['YC'])
axs[1, 3].set_title('YC')

axs[2, 0].boxplot(data_set['FOULS'])
axs[2, 0].set_title('FOULS')

axs[2, 1].boxplot(data_set['ST'])
axs[2, 1].set_title('ST')

axs[2, 2].boxplot(data_set['Conversion'])
axs[2, 2].set_title('Conversion')

fig.subplots_adjust(left=0.04, right=0.80,hspace=0.5,wspace=0.5)
plt.suptitle("Boxplots")
plt.show()




#Displaying the summary and parameters of the selected season

#If the season selected is 2015-16
if(reqdseason=='2015-16.xlsx'):
   
    # Final MLR model for the 2015-16 season which contains the independent variables Total goals conceded, yellow cards accumulated and the fouls commited throughout the season 
    result_final = sm.ols(formula = "TotalPts ~ TotalGC + YC + FOULS", data=data_set).fit()
    print("The final model for the 2015-16 season's Total points is")
    print("\nThe parameters of the final model are:\n",result_final.params)
    print("\nThe summary of the final model is:\n",result_final.summary())
    print("\nThe final model for the season 2015-16 is:\n Total points = 130.3956 - (1.1317 * Total goals conceded) - (0.38 * Yellow cards) + (0.0042 * Fouls)")
    print("\nUsing the above equation, the Winner for the current season would be:\nLiverpool with 92.75 points followed by Manchester City with 90.12 points. The 3 teams to get relegated would be Cardiff, Huddersfield and Fulham with 30.34, 26.74 and 19.55 points respectively")

#If the season selected is 2016-17
elif(reqdseason=='2016-17.xlsx'):

    # Final MLR model for the 2016-17 season which contains the independent variables Total goals conceded, Shot conversion ratio and the away goals conceded
    result_final = sm.ols(formula = "TotalPts ~ TotalGC + Conversion + AwayGC", data=data_set).fit()
    print("The final model for the 2016-17 season's Total points is")
    print("\nThe parameters of the final model are:\n",result_final.params)
    print("\nThe summary of the final model is:\n",result_final.summary())
    print("\nThe final model for the season 2016-17 is:\n Total points = 54.3818 - (0.4581 * Total goals conceded) - (0.9804 * Away goals conceded) + (164.6356 * Conversion)")
    print("\nUsing the above equation, the Winner for the current season would be:\nLiverpool with 97.35 points followed by Manchester City with 94.19 points. The 3 teams to get relegated would be Cardiff, Fulham and Huddersfield with 35.56, 13.07 and 6.95 points respectively")

#If the season selected is 2017-18
elif(reqdseason=='2017-18.xlsx'):
    # Final MLR model for the 2016-17 season which contains only the independent variable Away goals conceded
    result_final = sm.ols(formula = "TotalPts ~ AwayGC", data=data_set).fit()
    print("The final model for the 2017-18 season's Total points is:")
    print("\nThe parameters of the final model are:\n",result_final.params)
    print("\nThe summary of the final model is:\n",result_final.summary())
    print("\nThe final model for the season 2017-18 is:\n Total points = 110.2051 - (1.9985 * Away goals conceded)")
    print("\nUsing the above equation, the Winner for the current season would be:\nManchester City with 90.22 points followed by Liverpool with 86.22 points. The 3 teams to get relegated would be Burnley, Huddersfield and Fulham with 38.26, 22.27 and 20.27 points respectively")

print("\n\nThe END")
