import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("C:/Users/sumit/Downloads/cleaned_tea_dataset.csv")
sns.set(style="whitegrid")

# OBJECTIVE 1: Export by Country

plt.figure(figsize=(10,5))
sns.barplot(x='Country', y='Export', hue='Tea_Type', data=df,
            palette=['green','blue'])
plt.title("Clustered Export Comparison by Country", fontsize=14)
plt.xlabel("Country")
plt.ylabel("Export")
plt.xticks(rotation=45)
plt.legend(title="Tea Type")
plt.tight_layout()
plt.show()

# OBJECTIVE 2: Sales by State

plt.figure(figsize=(10,5))
sns.barplot(x='State', y='Sales', hue='Tea_Type', data=df,
            palette=['green','blue'])
plt.title("Clustered Sales Comparison by State", fontsize=14)
plt.xlabel("State")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.legend(title="Tea Type")
plt.tight_layout()
plt.show()

# OBJECTIVE 3: Production vs Price

plt.figure(figsize=(8,5))
sns.scatterplot(x='Production', y='Price', hue='Tea_Type', data=df,
                palette=['green','blue'])
plt.title("Production vs Price Relationship", fontsize=14)
plt.xlabel("Production")
plt.ylabel("Price")
plt.legend(title="Tea Type")
plt.tight_layout()
plt.show()

# OBJECTIVE 4: Price Trend

plt.figure(figsize=(10,5))
sns.lineplot(x='Year', y='Price', hue='Tea_Type', data=df,
             palette=['green','blue'], marker='o')
plt.title("Price Variation Over Years", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Price")
plt.legend(title="Tea Type")
plt.tight_layout()
plt.show()

# OBJECTIVE 5: Business Analysis
# Profit Comparison

plt.figure(figsize=(6,4))
sns.barplot(x='Tea_Type', y='Profit', data=df,
            palette=['green','blue'])
plt.title("Profit Comparison", fontsize=14)
plt.xlabel("Tea Type")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

# Revenue Comparison
plt.figure(figsize=(6,4))
sns.barplot(x='Tea_Type', y='Revenue', data=df,
            palette=['green','blue'])
plt.title("Revenue Comparison", fontsize=14)
plt.xlabel("Tea Type")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()
