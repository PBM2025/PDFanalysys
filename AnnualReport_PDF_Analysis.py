import streamlit as st
import PyPDF2
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import nltk

# Download NLTK stopwords
nltk.download('stopwords')
stops = set(stopwords.words('english'))

# Title of the app
st.title("PDF Text Processing and WordCloud Generator")
st.write("""Upload a PDF file, extract text, preprocess it, remove stopwords, and generate a WordCloud of the most frequent words.""")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    # Read PDF file
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    st.subheader("Extracted Text")
    st.write(text[:500] + "..." if len(text) > 500 else text)

    # Preprocess text
    st.subheader("Preprocessing Text")
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\W+', ' ', text)  # Remove non-alphanumeric characters
    text = re.sub(r'\d+', '', text)  # Remove digits
    words = text.split()
    filtered_words = [word for word in words if word not in stops]  # Remove stopwords

    st.write(f"Total Words After Preprocessing: {len(filtered_words)}")

    # Generate WordCloud
    st.subheader("WordCloud of Processed Text")
    wordcloud = WordCloud(width=1000, height=500, max_words=500, collocations=False, colormap="plasma").generate(' '.join(filtered_words))

    # Display WordCloud
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

    st.success("WordCloud Generated Successfully!")
