import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

import codecademylib3
np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('./nba_games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())
#1
knicks_pts_10 = nba_2010[nba_2010.fran_id == 'Knicks']['pts']
nets_pts_10 = nba_2010[nba_2010.fran_id == 'Nets']['pts']

#2
knicks_mean_score = np.mean(knicks_pts_10)
nets_mean_score = np.mean(nets_pts_10)

diff_means = knicks_mean_score - nets_mean_score
#3

plt.hist(knicks_pts_10, alpha=0.8, normed=True, label='knicks')
plt.hist(nets_pts_10, alpha=0.8, normed=True, label='nets')
plt.legend()
plt.title("2010 Season")
plt.show()
plt.clf()
# 4

knicks_pts_14 = nba_2014[nba_2014.fran_id == 'Knicks']['pts']
nets_pts_14 = nba_2014[nba_2014.fran_id == 'Nets']['pts']

knicks_mean_score = np.mean(knicks_pts_10)
nets_mean_score = np.mean(nets_pts_10)

diff_means_2014 = knicks_mean_score - nets_mean_score

plt.hist(knicks_pts_10, alpha=0.8, normed=True, label='knicks')
plt.hist(nets_pts_10, alpha=0.8, normed=True, label='nets')
plt.legend()
plt.title("2014 Season")
plt.show()
plt.clf()

print(diff_means)
print(diff_means_2014)

# 5
sns.boxplot(data= nba_2010, x = 'fran_id', y = 'pts')
plt.show()

# 6

location_result_freq = pd.crosstab(nba_2010.game_result, nba_2010.game_location)

print(location_result_freq)

# 7

location_result_proportions = location_result_freq/len(nba_2010)
print(location_result_proportions)

#8
chi2, pval, dof, expected = chi2_contingency(location_result_freq)
print(expected)
print(chi2)

#9

point_diff_forecast_cov = np.cov(nba_2010.point_diff, nba_2010.forecast)
print(point_diff_forecast_cov)

#10

point_diff_forecast_corr, p = pearsonr(nba_2010.forecast,nba_2010.point_diff)
print(point_diff_forecast_corr)

#11

plt.clf()
plt.scatter('forecast', 'point_diff', data=nba_2010)
plt.xlabel('Forecasted Win Prob.')
plt.ylabel('Point Differential')
plt.show()