"""
Module: ecommerce_mapper.py
Description: Automated ETL script for mapping raw vendor inventory 
             to Shopify/WooCommerce bulk upload formats.
"""

import pandas as pd
import sys
import logging

# Set up logging for audit trails
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def map_inventory(input_csv, output_csv):
    """Processes raw inventory data for e-commerce migration."""
    try:
        logging.info(f"Processing source file: {input_csv}")
        df = pd.read_csv(input_csv)
        
        # Standardize columns: Remove whitespace and standardize casing
        df.columns = df.columns.str.strip().str.lower()
        
        # Data Transformation Logic
        if 'product_name' in df.columns:
            df['handle'] = df['product_name'].str.replace(' ', '-').str.lower()
        
        # Export processed data
        df.to_csv(output_csv, index=False)
        logging.info(f"Successfully exported cleaned data to: {output_csv}")
        
    except FileNotFoundError:
        logging.error("Source file not found. Please verify the input path.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage: python map_products.py input.csv output.csv
    if len(sys.argv) == 3:
        map_inventory(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python map_products.py <input_file> <output_file>")
