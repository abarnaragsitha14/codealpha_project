from dataloader import load_data, dataset_info
from visualization import (
    region_sales,
    product_category,
    sales_distribution,
    customer_type,
    sales_channel,
    discount_vs_sales
)

# Load dataset
df = load_data()

# Display dataset details
dataset_info(df)

# Generate visualizations
region_sales(df)
product_category(df)
sales_distribution(df)
customer_type(df)
sales_channel(df)
discount_vs_sales(df)