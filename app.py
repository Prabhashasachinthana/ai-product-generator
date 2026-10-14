import streamlit as st
from google import genai

# Page Configuration
st.set_page_config(
    page_title="AI Product Description & SEO Generator",
    page_icon="🛒",
    layout="centered"
)

st.title("🛒 AI Product Description & SEO Generator")
st.markdown("A smart side-hustle tool for online sellers to instantly generate high-converting product descriptions, catch titles, and SEO tags.")

# Sidebar for API Configuration
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

st.sidebar.markdown("---")
st.sidebar.markdown("### About Hacktoberfest 2026")
st.sidebar.markdown("Built for Week 2: Open-Source AI / Side Hustle Challenge.")

# Main Input Section
product_name = st.text_input("Product Name", placeholder="e.g. Handmade Ceramic Coffee Mug")
product_features = st.text_area("Key Features & Details", placeholder="e.g. 12oz capacity, dishwasher safe, matte black glaze, ergonomic handle")
platform = st.selectbox("Target Selling Platform", ["Etsy", "Daraz / eBay", "Shopify", "Instagram Store"])

if st.button("Generate Product Content", type="primary"):
    if not api_key:
        st.error("Please enter your Gemini API Key in the sidebar.")
    elif not product_name:
        st.warning("Please enter a product name to begin.")
    else:
        with st.spinner("Generating optimized listing..."):
            try:
                # Initialize the Google GenAI client
                client = genai.Client(api_key=api_key)
                
                prompt = f"""
                You are an expert e-commerce copywriter and SEO specialist. 
                Generate a professional product listing for the following item:
                - Product Name: {product_name}
                - Key Features: {product_features}
                - Target Platform: {platform}

                Provide the output in a clean, structured format containing:
                1. Optimized Product Title
                2. Compelling Product Description (with a catchy hook and bullet points)
                3. High-Ranking SEO Tags / Keywords (comma-separated)
                """
                
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt
                )
                
                st.success("Listing generated successfully!")
                st.markdown("---")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")