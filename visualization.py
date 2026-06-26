import matplotlib.pyplot as plt

def region_sales(df):
    data = df.groupby("Region")["Sales_Amount"].sum()

    plt.figure(figsize=(6,5))
    data.plot(kind="bar")
    plt.title("Total Sales by Region")
    plt.xlabel("Region")
    plt.ylabel("Sales Amount")
    plt.grid(axis="y")
    plt.show()


def product_category(df):
    data = df.groupby("Product_Category")["Sales_Amount"].sum()

    plt.figure(figsize=(6,6))
    data.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Sales by Product Category")
    plt.ylabel("")
    plt.show()


def sales_distribution(df):
    plt.figure(figsize=(6,5))
    plt.hist(df["Sales_Amount"], bins=10)
    plt.title("Sales Amount Distribution")
    plt.xlabel("Sales Amount")
    plt.ylabel("Frequency")
    plt.show()


def customer_type(df):
    data = df.groupby("Customer_Type")["Quantity_Sold"].sum()

    plt.figure(figsize=(6,5))
    data.plot(kind="bar")
    plt.title("Quantity Sold by Customer Type")
    plt.xlabel("Customer Type")
    plt.ylabel("Quantity Sold")
    plt.grid(axis="y")
    plt.show()


def sales_channel(df):
    data = df.groupby("Sales_Channel")["Sales_Amount"].sum()

    plt.figure(figsize=(6,5))
    data.plot(kind="bar")
    plt.title("Sales by Sales Channel")
    plt.xlabel("Sales Channel")
    plt.ylabel("Sales Amount")
    plt.grid(axis="y")
    plt.show()


def discount_vs_sales(df):
    plt.figure(figsize=(6,5))
    plt.scatter(df["Discount"], df["Sales_Amount"])
    plt.title("Discount vs Sales Amount")
    plt.xlabel("Discount")
    plt.ylabel("Sales Amount")
    plt.grid(True)
    plt.show()