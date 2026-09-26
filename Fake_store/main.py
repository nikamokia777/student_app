import streamlit as st
import requests


url = "https://fakestoreapi.com/products"

try:
    with st.spinner("Loading products..."):
        response = requests.get(url)
        response.raise_for_status()
        products = response.json()

except requests.exceptions.RequestException:
    st.error("Failed to load products")
    products = []


st.title("Fake Store Products")

categories = list(set(product["category"] for product in products))
categories.insert(0, "All")

category = st.sidebar.selectbox(
    "Category",
    categories
)

max_price = max(product["price"] for product in products)

maximum_price = st.sidebar.slider(
    "Maximum Price",
    0.0,
    float(max_price),
    float(max_price)
)

search = st.sidebar.text_input("Search")
filtered_products = products

if category != "All":
    filtered_products = [
        product for product in filtered_products
        if product["category"] == category
    ]

filtered_products = [
    product for product in filtered_products
    if product["price"] <= maximum_price
]

if search:
    filtered_products = [
        product for product in filtered_products
        if search.lower() in product["title"].lower()
    ]
for product in filtered_products:
    st.write("ID:", product["id"])
    st.write("Title:", product["title"])
    st.write("Price:", product["price"])
    st.write("Category:", product["category"])
    st.image(product["image"])
    st.write("Rating:", product["rating"]["rate"])
    st.write("Rating Count:", product["rating"]["count"])

    with st.expander("View details"):
        st.write(product["description"])

    st.write("--------------------")