# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Homework 6, Part One: Lots and lots of questions about beer
# %% [markdown]
# ### Do your importing and your setup

# %%
import pandas as pd
import numpy as np
import matplotlib

# %% [markdown]
# ## Read in the file `craftcans.csv`, and look at the first first rows

# %%
ignore_na = ['Does not apply','NaN','nan']

df = pd.read_csv("craftcans.csv",na_values = ignore_na)

df

# %% [markdown]
# ## How many rows do you have in the data? What are the column types?

# %%
df.info()

# %% [markdown]
# # Checking out our alcohol
# %% [markdown]
# ## What are the top 10 producers of cans of beer?

# %%
df.Brewery.value_counts().head(10)

# %% [markdown]
# ## What is the most common ABV? (alcohol by volume)

# %%
df.ABV.value_counts().head(10)

# %% [markdown]
# ## Oh, weird, ABV isn't a number. Convert it to a number for me, please.
# 
# It's going to take a few steps!
# 
# ### First, let's just look at the ABV column by itself

# %%
df.ABV

# %% [markdown]
# ### Hm, `%` isn't part of  a number. Let's remove it.
# 
# When you're confident you got it right, save the results back into the `ABV` column.
# 
# - *Tip: In programming the easiest way to remove something is to *replacing it with nothing*.
# - *Tip: "nothing" might seem like `NaN` sinc we talked about it a lot in class, but in this case it isn't! It's just an empty string, like ""*
# - *Tip: `.replace` is used for replacing ENTIRE cells, while `.str.replace` is useful for replacing PARTS of cells (see my New York example)*

# %%
df.ABV = df.ABV.str.replace('%','')

# %% [markdown]
# ### Now let's turn `ABV` into a numeric data type
# 
# Save the results back into the `ABV` column (again), and then check `df.dtypes` to make sure it worked.
# 
# - *Tip: We used `.astype(int)` during class, but this has a decimal in it...*

# %%
df['ABV'] = df['ABV'].astype(float)

df.dtypes

# %% [markdown]
# ## What's the ABV of the average beer look like?
# 
# ### Show me in two different ways: one command to show the `median`/`mean`/etc, and secondly show me a chart

# %%
print(f'Mean:{df.ABV.mean().round(1)} & Median: {df.ABV.median()}')


# %%
df['ABV'].hist()

# %% [markdown]
# ### We don't have ABV for all of the beers, how many are we missing them from?
# 
# - *Tip: You can use `isnull()` or `notnull()` to see where a column is missing data.*
# - *Tip: You just want to count how many `True`s and `False`s there are.*
# - *Tip: It's a weird trick involving something we usually use to count things in a column*

# %%
df[df['ABV'].isnull()]


# %%
df['ABV'].isnull().value_counts()

# %% [markdown]
# # Looking at location
# 
# Brooklyn used to produce 80% of the country's beer! Let's see if it's still true.
# %% [markdown]
# ## What are the top 10 cities in the US for canned craft beer?

# %%
df['Location'].value_counts().head(10)

# %% [markdown]
# ## List all of the beer from Brooklyn, NY

# %%
df[df['Location'] == 'Brooklyn, NY']

# %% [markdown]
# ## What brewery in Brooklyn puts out the most cans of beer?

# %%
df[df['Location'] == 'Brooklyn, NY']['Brewery'].value_counts()

# %% [markdown]
# ## What are the five most popular styles of beer produced by Sixpoint?

# %%
df[df['Brewery'] == 'Sixpoint Craft Ales']['Style'].value_counts().head(5)


# %%
df

# %% [markdown]
# ## List all of the breweries in New York state.
# 
# - *Tip: We want to match *part* of the `Location` column, but not all of it.*
# - *Tip: Watch out for `NaN` values! You might be close, but you'll need to pass an extra parameter to make it work without an error.*

# %%
df_city_state = df["Location"].str.split(", ", expand=True).rename(
    columns={0: 'city', 1:'state'})

df = pd.concat([df,df_city_state],axis=1)


# %%
df[df['state'] == 'NY']

# %% [markdown]
# 
# ### Now *count* all of the breweries in New York state

# %%
df[df['state'] == 'NY']['Brewery'].value_counts()

# %% [markdown]
# # Measuring International Bitterness Units
# 
# ## Display all of the IPAs
# 
# Include American IPAs, Imperial IPAs, and anything else with "IPA in it."
# 
# IPA stands for [India Pale Ale](https://www.bonappetit.com/story/ipa-beer-styles), and is probably the most popular kind of beer in the US for people who are drinking [craft beer](https://www.craftbeer.com/beer/what-is-craft-beer).

# %%
df[df['Style'].str.contains("IPA",na=False)]

# %% [markdown]
# IPAs are usually pretty hoppy and bitter. IBU stands for [International Bitterness Unit](http://www.thebrewenthusiast.com/ibus/), and while a lot of places like to brag about having the most bitter beer (it's an American thing!), IBUs don't necessary *mean anything*.
# 
# Let's look at how different beers have different IBU measurements.
# %% [markdown]
# ## Try to get the average IBU measurement across all beers

# %%
df.describe()

# %% [markdown]
# ### Oh no, it doesn't work!
# 
# It looks like some of those values *aren't numbers*. There are two ways to fix this:
# 
# 1. Do the `.replace` and `np.nan` thing we did in class. Then convert the column to a number. This is boring.
# 2. When you're reading in your csv, there [is an option called `na_values`](http://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.read_csv.html). You can give it a list of **numbers or strings to count as `NaN`**. It's a lot easier than doing the `np.nan` thing, although you'll need to go add it up top and run all of your cells again.
# 
# - *Tip: Make sure you're giving `na_values` a LIST, not just a string*
# 
# ### Now try to get the average IBUs again

# %%
df['IBUs'].unique()


# %%
df['IBUs'] = df['IBUs'].astype(float)
df['IBUs'].mean().round(2)

# %% [markdown]
# ## Draw the distribution of IBU measurements, but with *twenty* bins instead of the default of 10
# 
# - *Tip: Every time I ask for a distribution, I'm looking for a histogram*
# - *Tip: Use the `?` to get all of the options for building a histogram*
# - *Tip: Make sure your `matplotlib` thing is set up right!*

# %%
df['IBUs'].hist(bins=20)

# %% [markdown]
# ## Hm, Interesting distribution. List all of the beers with IBUs above the 75th percentile
# 
# - *Tip: There's a single that gives you the 25/50/75th percentile*
# - *Tip: You can just manually type the number when you list those beers*

# %%
high_ibu = df[df['IBUs'] > df.IBUs.quantile(0.75)]


# %%
high_ibu

# %% [markdown]
# ## List all of the beers with IBUs below the 25th percentile

# %%
low_ibu = df[df['IBUs'] < df.IBUs.quantile(0.25)]

low_ibu

# %% [markdown]
# ## List the median IBUs of each type of beer. Graph it.
# 
# Put the highest at the top, and the missing ones at the bottom.
# 
# - Tip: Look at the options for `sort_values` to figure out the `NaN` thing. The `?` probably won't help you here.

# %%
# Not sure if this is what we are looking for..

df.groupby(by='Style').median('IBUs').sort_values(by='IBUs',ascending=False).plot.barh(y='IBUs').invert_yaxis()

# %% [markdown]
# ## Hmmmm, it looks like they are generally different styles. What are the most common 5 styles of high-IBU beer vs. low-IBU beer?
# 
# - *Tip: You'll want to think about it in three pieces - filtering to only find the specific beers beers, then finding out what the most common styles are, then getting the top 5.*
# - *Tip: You CANNOT do this in one command. It's going to be one command for the high and one for the low.*
# - *Tip: "High IBU" means higher than 75th percentile, "Low IBU" is under 25th percentile*

# %%
high_ibu.groupby(by='Style').median('IBUs').head(5)


# %%
low_ibu.groupby(by='Style').median('IBUs').head(5)

# %% [markdown]
# ## Get the average IBU of "Witbier", "Hefeweizen" and "American Pale Wheat Ale" styles
# 
# I'm counting these as wheat beers. If you see any other wheat beer categories, feel free to include them. I want ONE measurement and ONE graph, not three separate ones. And 20 to 30 bins in the histogram, please.
# 
# - *Tip: I hope that `isin` is in your toolbox*

# %%
list = ['Witbier','Hefeweizen','American Pale Wheat Ale']

df[df['Style'].isin(list)].groupby(by='Style').median('IBUs')

# %% [markdown]
# ## Draw a histogram of the IBUs of those beers

# %%
df[df['Style'].isin(list)].groupby(by='Style').median('IBUs').hist('IBUs')

# %% [markdown]
# ## Get the average IBU of any style with "IPA" in it (also draw a histogram)

# %%
df[df['Style'].str.contains("IPA",na=False)].groupby(by='Style').median('IBUs')


# %%
df[df['Style'].str.contains("IPA",na=False)].groupby(by='Style').median('IBUs').hist('IBUs')

# %% [markdown]
# ## Plot those two histograms on top of one another
# 
# To plot two plots on top of one another, you do two steps.
# 
# 1. First, you make a plot using `plot` or `hist`, and you save it into a variable called `ax`.
# 2. You draw your second graph using `plot` or `hist`, and send `ax=ax` to it as a parameter.
# 
# It would look something like this:
# 
# ```python
# ax = df.plot(....)
# df.plot(ax=ax, ....)
# ``` 
# 
# (...except totally different)

# %%
ax = df[df['Style'].str.contains("IPA",na=False)].groupby(by='Style').median('IBUs').hist('IBUs')

df[df['Style'].isin(list)].groupby(by='Style').median('IBUs').hist('IBUs',ax=ax)

# side by side works?

# %% [markdown]
# ## Compare the ABV of wheat beers vs. IPAs : their IBUs were really different, but how about their alcohol percentage?
# 
# Wheat beers might include witbier, hefeweizen, American Pale Wheat Ale, and anything else you think is wheaty. IPAs probably have "IPA" in their name.

# %%
df['Style'].sort_values().unique()


# %%
ABV_list= ['IPA','Hefeweizen','American Pale Wheat Ale','Wheat']

# transform to regex
ABV_list = '|'.join(ABV_list)

ipa_wit = df[df['Style'].str.contains(ABV_list,na=False)]


# %%
ipa_wit['Style_Type'] = np.where((ipa_wit.Style.str.contains('IPA')), 'IPA', 'Wheat')

ipa_wit.sort_values(by='IBUs')


# %%
px.scatter(ipa_wit,x='IBUs',y='ABV',color='Style_Type',hover_data=['Beer'])

# %% [markdown]
# ## Good work!
# 
# If you made it this far you deserve a drink.

# %%
# o/


