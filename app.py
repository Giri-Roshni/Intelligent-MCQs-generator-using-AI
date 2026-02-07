import streamlit as st
from utils import read_syllabus
from gemini_mcq import generate_mcqs
from pdf_generator import generate_pdf

st.set_page_config(page_title="AI MCQ Generator", layout="centered")
st.title("Intelligent MCQs Generator Using AI")
st.subheader("Upload Engineering Syllabus → Get MCQs PDF")

uploaded_file = st.file_uploader("Upload syllabus (PDF or TXT)", type=["pdf", "txt"])
num_questions = st.slider("Number of MCQs", 10, 100, 50)

if uploaded_file:
    syllabus_text = read_syllabus(uploaded_file)

    if not syllabus_text.strip():
        st.error("⚠️ Could not extract text from the uploaded syllabus. Make sure it's a text-based PDF.")
        st.stop()

    st.write("Syllabus text extracted successfully (preview):")
    st.text_area("Preview", syllabus_text[:1000], height=200)

    if st.button("Generate MCQs"):
        with st.spinner("Generating MCQs strictly from your syllabus..."):
            # Split syllabus if too long
            max_chars = 3000
            chunks = [syllabus_text[i:i+max_chars] for i in range(0, len(syllabus_text), max_chars)]
            all_mcqs = ""
            per_chunk_questions = max(10, num_questions // len(chunks))

            for chunk in chunks:
                mcqs = generate_mcqs(chunk, per_chunk_questions)
                if mcqs.startswith("ERROR"):
                    st.error(mcqs)
                    st.stop()
                all_mcqs += mcqs + "\n\n"

            st.success("✅ MCQs Generated Successfully!")
            st.text_area("Generated MCQs", all_mcqs, height=400)

            pdf_file = generate_pdf(all_mcqs)
            with open(pdf_file, "rb") as f:
                st.download_button(
                    "📥 Download MCQs PDF",
                    f,
                    file_name="Generated_MCQs.pdf",
                    mime="application/pdf"
                )
