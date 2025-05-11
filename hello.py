import pandas as pd
import plotly.express as px
import preswald

# 0. Load the CSV (unchanged)
df = pd.read_csv('data/sample.csv')

# 1. Compute a new metric: value per unit
df['unit_value'] = df['value'] / df['quantity']

# 2. Intro text + raw table
preswald.text("# Welcome to Preswald!")
preswald.text("This mini-app shows how you can spin up simple metrics and visuals.")
preswald.table(df, title="Original Data with Unit Value")

# 3. Summary statistics
preswald.text("## Summary Statistics")
preswald.table(df[['quantity','value','unit_value']].describe().reset_index(), 
               title="count • mean • std • min • max • etc.")

# 4. Filter for “high unit value” items
high_uv = df[df['unit_value'] > df['unit_value'].mean()]
preswald.text(f"## {len(high_uv)} Items Above Avg Unit Value ({df['unit_value'].mean():.1f})")
preswald.table(high_uv, title="Above-Average Unit Value")

# 5. Scatter: quantity vs. value, colored by unit_value
fig1 = px.scatter(
    df, 
    x='quantity', 
    y='value', 
    color='unit_value',
    size='quantity',
    hover_name='item',
    title='Quantity vs. Value (colored by Unit Value)',
    labels={
      'quantity':'Quantity',
      'value':'Value',
      'unit_value':'Value per Unit'
    },
    template='plotly_white'
)
preswald.plotly(fig1)

# 6. Bar: top 5 items by unit_value
top5 = df.nlargest(5, 'unit_value')
fig2 = px.bar(
    top5, 
    x='item', 
    y='unit_value', 
    text='unit_value',
    title='Top 5 Items by Unit Value',
    labels={'unit_value':'Value per Unit'},
    template='plotly_white'
)
fig2.update_traces(textposition='outside')
preswald.plotly(fig2)
