import numpy as np
import pandas as pd


monthly_report = pd.read_csv('monthly_report.csv')

####Summarizing the Sample

#print the head of monthly_report:
print(monthly_report.head())

#calculate and print sample_size:
sample_size = len(monthly_report)
print(sample_size)
#calculate and print num_purchased:
num_purchased = np.sum(monthly_report.purchase == "y")
print(num_purchased)

####Simulating Randomness

simulate one visitor:
one_visitor = np.random.choice(['y', 'n'], size = 1, p=[0.1, 0.9])
print(one_visitor)

#simulate 500 visitors:
simulated_monthly_visitors = np.random.choice(['y', 'n'], size = 500, p=[0.1, 0.9])
print(simulated_monthly_visitors)

####Simulating the Null Distribution I

simulate 500 visitors:
simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

#calculate the number of simulated visitors who made a purchase:
num_purchased = np.sum(simulated_monthly_visitors == 'y')
print(num_purchased)

####Simulating the Null Distribution II

null_outcomes = []

#start for loop here:
for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

  num_purchased = np.sum(simulated_monthly_visitors == 'y')
  null_outcomes.append(num_purchased)



#calculate the minimum and maximum values in null_outcomes here:

null_min = np.min(null_outcomes)
null_max = np.max(null_outcomes)

print(null_min)
print(null_max)


#### Inspecting the null distribution 

null_outcomes = []

for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

  num_purchased = np.sum(simulated_monthly_visitors == 'y')

  null_outcomes.append(num_purchased)

#plot the histogram here:
plt.hist(null_outcomes)
plt.axvline(41,color='r')
plt.show()

####### Confidence Intervals

null_outcomes = []

for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

  num_purchased = np.sum(simulated_monthly_visitors == 'y')

  null_outcomes.append(num_purchased)

#calculate the 90% interval here:
null_90CI = np.percentile(null_outcomes, [5, 95])
print(null_90CI)


#####Calculating a One-Sided P-Value

null_outcomes = []

for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

  num_purchased = np.sum(simulated_monthly_visitors == 'y')

  null_outcomes.append(num_purchased)

#calculate the p-value here:

null_outcomes = np.array(null_outcomes)
p_value = np.sum(null_outcomes <= 41)/len(null_outcomes)
print(p_value)


##### Calculating a Two-Sided P-Value

null_outcomes = []

for i in range(10000):
  simulated_monthly_visitors = np.random.choice(['y', 'n'], size=500, p=[0.1, 0.9])

  num_purchased = np.sum(simulated_monthly_visitors == 'y')

  null_outcomes.append(num_purchased)

#calculate the p-value here:
null_outcomes = np.array(null_outcomes)
p_value = np.sum((null_outcomes <= 41) | (null_outcomes >= 59))/len(null_outcomes)

print(p_value)


##### Writing a Binomial Test Function


def simulation_binomial_test(observed_successes, n, p):
  #initialize null_outcomes
  null_outcomes = []
  
  #generate the simulated null distribution
  for i in range(10000):
    simulated_monthly_visitors = np.random.choice(['y', 'n'], size=n, p=[p, 1 - p])
    num_purchased = np.sum(simulated_monthly_visitors == 'y')
    null_outcomes.append(num_purchased)

  #calculate a 1-sided p-value
  null_outcomes = np.array(null_outcomes)
  p_value = np.sum(null_outcomes <= observed_successes)/len(null_outcomes) 
  
  #return the p-value
  return p_value

#Test your function below by uncommenting the code below. You should see that your simulation function gives you a very similar answer to the binom_test function from scipy:

p_value1 = simulation_binomial_test(45, 500, .1)
print("simulation p-value: ", p_value1)

p_value2 = binom_test(45, 500, .1, alternative = 'less')
print("binom_test p-value: ", p_value2)


### Binomial Testing with Scipy

from scipy.stats import binom_test

# calculate p_value_2sided here:
p_value_2sided = binom_test(41, n=500, p=0.1 )
print(p_value_2sided)
# calculate p_value_1sided here:
p_value_1sided = binom_test(41, n=500, p=0.1, alternative= 'less')
print(p_value_1sided)


##### Function for less than, not equal and more than

from scipy.stats import binom_test

def simulation_binomial_test(observed_successes, n, p, alternative_hypothesis):
  #initialize null_outcomes
  null_outcomes = []
  
  #generate the simulated null distribution
  for i in range(10000):
    simulated_monthly_visitors = np.random.choice(['y', 'n'], size=n, p=[p, 1-p])
    num_purchased = np.sum(simulated_monthly_visitors == 'y')
    null_outcomes.append(num_purchased)

  null_outcomes = np.array(null_outcomes)

  if alternative_hypothesis == 'less':
    p_value = np.sum(null_outcomes <= observed_successes)/len(null_outcomes) 
  elif alternative_hypothesis == 'greater':
    p_value = np.sum(null_outcomes >= observed_successes)/len(null_outcomes)
  else:
    difference = np.abs(p*n - observed_successes)
    upper = p*n + difference
    lower = p*n - difference
    p_value = np.sum((null_outcomes >= upper) | (null_outcomes <= lower))/len(null_outcomes)
  
  #return the p-value
  return p_value

#Test your function:
print('lower tail one-sided test:')
p_value1 = simulation_binomial_test(45, 500, .1, alternative_hypothesis = 'less')
print("simulation p-value: ", p_value1)

p_value2 = binom_test(45, 500, .1, alternative = 'less')
print("binom_test p-value: ", p_value2)

print('upper tail one-sided test:')
p_value1 = simulation_binomial_test(53, 500, .1, alternative_hypothesis = 'greater')
print("simulation p-value: ", p_value1)

p_value2 = binom_test(53, 500, .1, alternative = 'greater')
print("binom_test p-value: ", p_value2)

print('two-sided test:')
p_value1 = simulation_binomial_test(42, 500, .1, alternative_hypothesis = 'not_equal')
print("simulation p-value: ", p_value1)

p_value2 = binom_test(42, 500, .1)
print("binom_test p-value: ", p_value2)