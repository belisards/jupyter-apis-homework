# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %% [markdown]
# # Homework 5, Part 1: Building a pandas cheat sheet
# 
# **Use `animals.csv` to answer the following questions.** The data is small and the questions are pretty simple, so hopefully you can use this for pandas reference in the future.
# %% [markdown]
# ## 0) Setup
# 
# Import pandas **with the correct name**.

# %%
get_ipython().system('pip install pandas matplotlib')


# %%
import pandas as pd
import matplotlib

# %% [markdown]
# ## 1) Reading in a csv file
# 
# Use pandas to read in the animals CSV file, saving it as a variable with the normal name for a dataframe

# %%
df = pd.read_csv('animals.csv')
df

# %% [markdown]
# ## 2) Checking your data
# 
# Display the number of rows and columns in your data. Also display the names and data types of each column.

# %%
df.info()

# %% [markdown]
# ## 3) Display the first 3 animals
# 
# Hmmm, we know how to take the first 5, but maybe the first 3. Maybe there is an option to change how many you get? Use `?` to check the documentation on the command.

# %%
df[:3]


# %%
df.head(3)

# %% [markdown]
# ## 4) Sort the animals to show me the 3 longest animals
# 
# > **TIP:** You can use `.head()` after you sort things!

# %%
df.sort_values(by='length',ascending=False).head(3)

# %% [markdown]
# ## 5) Get the mean and standard deviation of animal lengths
# 
# You can do this with separate commands or with a single command.

# %%
mean = round(df['length'].mean())
stdev = round(df['length'].std())

print(f'The mean is {mean} and the standard deviation is {stdev}')

# %% [markdown]
# ## 6) How many cats do we have and how many dogs?
# 
# You only need one command to do this

# %%
df.groupby(by='animal').count()['name']

# %% [markdown]
# ## 7) Only display the dogs
# 
# > **TIP:** It's probably easiest to make it display the list of `True`/`False` first, then wrap the `df[]` around it.

# %%
df[df['animal'] == 'dog']


# %%



# %%



# %%


# %% [markdown]
# ## 8) Only display the animals that are longer than 40cm

# %%
df[df['length'] > 40]

# %% [markdown]
# ## 9) `length` is the animal's length in centimeters. Create a new column called `inches` that is the length in inches.

# %%
df['inches'] = (df['length'] * 0.393701).round()

df

# %% [markdown]
# ## 10) Save the cats to a separate variable called `cats`. Save the dogs to a separate variable called `dogs`.
# 
# This is the same as listing them, but you just save the result to a variable instead of looking at it. Be sure to use `.head()` to make sure your data looks right.
# 
# Once you do this, every time you use `cats` you'll only be talking about the cats, and same for the dogs.

# %%
dogs = df[df['animal'] == 'dog']
cats = df[df['animal'] == 'cat']


# %%
dogs


# %%
cats

# %% [markdown]
# ## 11) Display all of the animals that are cats and above 12 inches long.
# 
# First do it using the `cats` variable, then also do it using your `df` dataframe.
# 
# > **TIP:** For multiple conditions, you use `df[(one condition) & (another condition)]`

# %%
cats[cats['inches'] > 12]


# %%
df[(df['inches'] > 12)&(df['animal'] == 'cat')]


# %%


# %% [markdown]
# ## 12) What's the mean length of a cat? What's the mean length of a dog?

# %%
cats['length'].mean()


# %%
dogs['length'].mean()

# %% [markdown]
# ## 13) If you didn't already, use `groupby` to do #12 all at once

# %%
df.groupby(by='animal').mean()['length']

# %% [markdown]
# ## 14) Make a histogram of the length of dogs.
# 
# We didn't talk about how to make a histogram in class! It **does not** use `plot()`. Imagine you're a programmer who doesn't want to type out `histogram` - what do you think you'd type instead?
# 
# > **TIP:** The method is four letters long
# >
# > **TIP:** First you'll say "I want the length column," then you'll say "make a histogram"
# >
# > **TIP:** This is the worst histogram ever

# %%
dogs['length'].hist()

# %% [markdown]
# ## 15) Make a horizontal bar graph of the length of the animals, with the animal's name as the label
# 
# > **TIP:** It isn't `df['length'].plot()`, because it needs *both* columns. Think about how we did the scatterplot in class.
# >
# > **TIP:** Which is the `x` axis and which is the `y` axis? You'll notice pandas is kind of weird and wrong.
# >
# > **TIP:** Make sure you specify the `kind` of graph or else it will be a weird line thing
# >
# > **TIP:** If you want, you can set a custom size for your plot by sending it something like `figsize=(15,2)`

# %%
df.sort_values(by='length').plot.barh(x='name',y='length',figsize=(15,2))

# %% [markdown]
# ## 16) Make a sorted horizontal bar graph of the cats, with the larger cats on top
# 
# > **TIP:** Think in steps, even though it's all on one line - first make sure you can sort it, then try to graph it.

# %%
cats.sort_values(by='length').plot.barh(x='name',y='length')

# %% [markdown]
# ## 17) As a reward for getting down here: run the following code, then plot the number of dogs vs. the number of cats
# 
# > **TIP:** Counting the number of dogs and number of cats does NOT use `.groupby`! That's only for calculations.
# >
# > **TIP:** You can set a title with `title="Number of animals"`

# %%
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


# %%
df.groupby(by='animal').count()['name'].plot.barh(x='name',y='length',title="Number of animals")


