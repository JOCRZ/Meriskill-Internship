import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# data

df = pd.read_csv('Sales.csv')


# Kpi 1 , total Sales
total_sales = df.Sales.sum().round()
f_sales = f"{total_sales/1e6:.2f}M"

# Kpi 2 , total quantity sold
total_quantity_sold = df['Quantity Ordered'].sum().round()
f_Qsold = f"{total_quantity_sold/1e3:.2f}K"

# Kpi 3 , average sales per order
average_sales_per_order = df['Sales'].mean().round()
f_avgsalesperorder = f"{average_sales_per_order/1e0:.0f}K"

# Kpi 4 , total customera
total_customers = df['Customer ID'].nunique()
f_tcust = f"{total_customers/1e3:.1f}K"

#kpi 5, retention rate
quarter_2_df = df[df['Month'].isin([12])]
# Identify unique customers in the 2nd quarter.
customers_in_2nd_quarter = quarter_2_df['Customer ID'].unique()
# Calculate the total number of unique customers in the 1st quarter.
total_customers_in_1st_quarter = df[df['Month'].isin([1,2,3,4,5,6,7,8,9,10,11])]['Customer ID'].nunique()
# Calculate the customer retention rate.
retention_rate = f"{len(customers_in_2nd_quarter) / total_customers_in_1st_quarter:.2%}"


st.title('Sales Dashboard')

kpi1,kpi2,kpi3,kpi4,kpi5 = st.columns(5)

kpi1.metric(label= "Total Sales" ,value= f_sales)
kpi2.metric(label= "Total Quantity Sold" ,value= f_Qsold)
kpi3.metric(label= "Avg Sales per Order" ,value= f_avgsalesperorder)
kpi4.metric(label= "Total Customers" ,value= f_tcust)
kpi5.metric(label= "Retention rate" ,value= retention_rate)


data_container1 = st.container()

with data_container1:
    col1, col2 = st.columns(2)
    with col1:

        st.text('Total Sales by Product')
        sns.set(style="whitegrid")
        fig1, ax1 = plt.subplots(figsize=(7, 5))
        product_sales = df.groupby('Product')['Sales'].sum().reset_index()
        sns.barplot(data=product_sales, x="Sales", y="Product", ci=None, order=product_sales.sort_values(by="Sales", ascending=False)['Product'],ax=ax1)
        plt.xlabel("Total Sales")
        plt.ylabel("Product")
        plt.title("Total Sales by Product")
        plt.tight_layout()
        st.pyplot(fig1)
        
    with col2:
    
        st.text('Total Sales by City')
        sns.set(style="whitegrid")
        fig2, ax2 = plt.subplots(figsize=(7, 5))
        product_sales = df.groupby('City')['Sales'].sum().reset_index()
        sns.barplot(data=product_sales, x="Sales", y="City", ci=None, order=product_sales.sort_values(by="Sales", ascending=False)['City'],ax=ax2)
        plt.xlabel("Total Sales")
        plt.ylabel("City")
        plt.title("Total Sales by City")
        plt.tight_layout()
        st.pyplot(fig2)

data_container2 = st.container()

with data_container2:
    col3, col4 = st.columns(2)
    with col3:

        st.text('Total Sales Over Month')
        sns.set(style="whitegrid")
        fig3, ax3 = plt.subplots(figsize=(7, 5))
        sns.lineplot(data=df, x="Month", y="Sales", ci=None,ax=ax3)
        plt.xlabel("Month")
        plt.ylabel("Sales")
        plt.title("Sales Over Months")
        plt.tight_layout()
        plt.show()
        st.pyplot(fig3)
        
    with col4:
    
        st.text('Total Sales Over Hour')
        sns.set(style="whitegrid")
        fig4, ax4 = plt.subplots(figsize=(7, 5))
        sns.lineplot(data=df, x="Hour", y="Sales", ci=None,ax=ax4)
        plt.xlabel("Hour")
        plt.ylabel("Sales")
        plt.title("Sales Over Hours")
        plt.tight_layout()
        plt.show()
        st.pyplot(fig4)
