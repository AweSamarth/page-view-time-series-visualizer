#%%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col=0, parse_dates=True)

# Clean data
df = df[(df['value']<df['value'].quantile(0.975)) & (df['value']>df['value'].quantile(0.025))]
# print(df)


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 5))
    # fig.set()
    sns.lineplot(df, ax=ax).set(title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019", xlabel="Date", ylabel="Page Views")





    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    fig, ax = plt.subplots(figsize=(12, 5))

    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([df.index.year, df.index.month]).mean()
    df_bar.index.rename(["year", "month"], inplace=True)
    df_bar.rename(columns={'value':'avg'}, inplace=True)
    df_bar=df_bar.reset_index()
    df_bar['month'] = df_bar['month'].astype(str)

    # Draw bar plot 

    order=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    sns.barplot(df_bar, x='year', y="avg", hue="month",  hue_order=order)
    handles, labels = plt.gca().get_legend_handles_labels()
    plt.legend(handles, month_names, title="Months")

    # plt.xlabel="teri"
    ax.set_xlabel("Years") 
    ax.set_ylabel("Average Page Views")




    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)

    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    fig, ax = plt.subplots(1,2, figsize=(18, 9))
    y_tick_locations = range(0, 200001, 20000)

    ax[0].set_ylim(0, 200000)
    ax[0].set_yticks(y_tick_locations)
    
    newdf = df_box.groupby(by='month')['value'].sum()
    # print(newdf)
    
    order=['Jan','Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    # Draw box plots (using Seaborn)
    sns.boxplot(df_box, x='year', y="value", ax=ax[0])
    sns.boxplot(df_box, x='month', y="value", ax=ax[1], order=order)
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
    ax[0].set_title("Year-wise Box Plot (Trend)")
    ax[1].set_title('Month-wise Box Plot (Seasonality)')

    



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig


# draw_line_plot()
draw_bar_plot()
# draw_box_plot()