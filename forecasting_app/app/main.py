import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.title("Forecasting Test App")

    data = pd.DataFrame({
        "Date": pd.date_range(start="2023-01-01", periods=30),
        "Value": np.random.randn(30).cumsum()
    })
    
    st.write("Sample Data:", data)
    st.line_chart(data.set_index("Date"))
    print("test")

if __name__ == "__main__":
    main()