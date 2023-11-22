# %%
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, zscore, f_oneway
from sklearn.linear_model import LinearRegression
from statsmodels.stats.weightstats import ztest
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score


# %%
df = pd.read_csv('winequality-red.csv')
df

# %%
df.info()

# %%
df.describe()

# %%
df.isnull().sum()

# %%
sns.displot(df['alcohol'])

# %%
sns.distplot(df['residual sugar'])

# %%
sns.boxplot(df['residual sugar'])

# %% [markdown]
# outliers IRQ

# %%
q1 = df['residual sugar'].quantile(0.25)
q3 = df['residual sugar'].quantile(0.75)
iqr = q3-q1

# %%
upper_limit = q3 + (1.5 * iqr)
lower_limit = q1 - (1.5 * iqr)
lower_limit, upper_limit

# %%
sns.boxplot(df['residual sugar'])

# %%
# find the outliers
df.loc[(df['residual sugar'] > upper_limit) | (df['residual sugar'] < lower_limit)]

# %%
# trimming - delete the outlier data
new_df = df.loc[(df['residual sugar'] <= upper_limit) & (df['residual sugar'] >= lower_limit)]
print('before removing outliers:', len(df))
print('after removing outliers:',len(new_df))
print('outliers:', len(df)-len(new_df))

# %%
sns.boxplot(new_df['residual sugar'])

# %%
sns.scatterplot(x='alcohol',y='density',data=df)

# %%
df.corr()

# %%
correlation_matrix = df.corr()
plt.figure(figsize=(10, 10))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.show()

# %%
sns.scatterplot(x='fixed acidity',y='density',data=df)

# %%
sns.distplot(df['fixed acidity'])

# %%
df.describe()

# %%
am = df['alcohol'].mode()
print("Alcohol mode:",am)

# %%
am = df['alcohol'].median()
print("Alcohol median:",am)

# %%
am = df['alcohol'].mean()
print("Alcohol mode:",am)

# %%
sns.pairplot(data=df)

# %%
plt.figure(figsize=(20,6))
sns.barplot(data=df)
plt.show()

# %% [markdown]
# anova

# %%
f_statistic, p_value = f_oneway(df['alcohol'], df['residual sugar'], df['density'])
print(f'F-statistic: {f_statistic}')
print(f'P-value: {p_value}')

# Check significance
if p_value < 0.05:
    print("The groups have significantly different means.")
else:
    print("The groups do not have significantly different means.")

# %% [markdown]
# t test

# %%
t_statistic, p_value = ttest_ind(df['alcohol'], df['residual sugar'])

# Print results
print(f'T-statistic: {t_statistic}')
print(f'P-value: {p_value}')

# Check significance
if p_value < 0.05:
    print("The means of the two groups are significantly different.")
else:
    print("There is no significant difference in means between the two groups.")

# %% [markdown]
# z test

# %%
meana = df['density'].mean()
std = df['density'].std()
z_statistic, p_value = ztest(df['density'], value=meana, alternative='two-sided', ddof=1)
print(f'Z-statistic: {z_statistic}')
print(f'P-value: {p_value}')

# Check significance
if p_value < 0.05:
    print("The mean of the sample is significantly different from the hypothesized population mean.")
else:
    print("There is no significant difference in means.")

# %%
z_statistic, p_value = ztest(df['fixed acidity'], df['density'], alternative='two-sided', ddof=1)

# Print results
print(f'Z-statistic: {z_statistic}')
print(f'P-value: {p_value}')

# Check significance
if p_value < 0.05:
    print("The means of the two groups are significantly different.")
else:
    print("There is no significant difference in means between the two groups.")

# %%
X = df[['density']]
y = df[['pH']]

model = LinearRegression()
model.fit(X,y)
predictions = model.predict(X)
plt.scatter(X, y, label='Original data')
plt.plot(X, predictions, color='red', label='Linear regression')
plt.xlabel('density')
plt.ylabel('pH')
plt.legend()
plt.show()

# %%
slope = model.coef_[0]
intercept = model.intercept_

print(f"Slope: {slope}")
print(f"Intercept: {intercept}")

# %%
X = df[['density']]
y = df[['fixed acidity']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
print(f'R-squared: {r2}')

plt.scatter(X, y, label='Original data')
plt.plot(X, model.predict(X), color='red', label='Linear regression')
plt.scatter(X_test, y_test, color='green', label='Testing data')
plt.xlabel('density')
plt.ylabel('fixed acidity')
plt.legend()
plt.title('Linear Regression and Testing Data Plot')
plt.show()

# %%
plt.scatter(X, y, label='Original data')
plt.plot(X, model.predict(X), color='red', label='Linear regression')

# Plot the curve for original vs. predicted data
x_curve = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_curve = model.predict(x_curve)
plt.plot(x_curve, y_curve, linestyle='dashed', color='green', label='Curve for Original vs. Predicted')

plt.scatter(X_test, y_test, color='green', label='Testing data')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Linear Regression and Testing Data Plot with Curve')
plt.show()

# %%
plt.plot(X_test, y_test, marker='o', linestyle='', label='Actual data')
plt.plot(X_test, y_pred, marker='', linestyle='-', color='red', label='Predicted data')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.title('Predicted vs. Actual Data Line Chart')
plt.show()


