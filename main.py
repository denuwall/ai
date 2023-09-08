import streamlit as st
from docx import Document

# Функция для анализа текста (заглушка)
def analyze_text_with_nn(text):
    return "Это результат анализа."

# Функция для загрузки файла Word
def upload_file():
    uploaded_file = st.file_uploader("Загрузите файл Word (.docx)", type=["docx"])
    if uploaded_file is not None:
        doc = Document(uploaded_file)
        full_text = "\n".join([p.text for p in doc.paragraphs])
        return full_text
    return None

# Главная часть приложения
def main():
    st.title("Анализатор текстовых пресс-релизов")

    # Стилизация блочного меню
    menu_style = """
        div.sidebar-element {
            padding: 10px 0;
            text-align: center;
        }
        div.sidebar-element:hover {
            background-color: #f0f0f0;
        }
    """
    st.markdown(f'<style>{menu_style}</style>', unsafe_allow_html=True)

    # Варианты навигации в блочном меню
    if st.sidebar.button("Анализатор", key="analyzer"):
        st.session_state.menu_selection = "Анализатор"
    if st.sidebar.button("FAQ", key="faq"):
        st.session_state.menu_selection = "FAQ"

    menu_selection = st.session_state.get("menu_selection", "Анализатор")

    if menu_selection == "Анализатор":
        st.header("Анализатор")

        # Загрузка текста
        st.subheader("Загрузите текст:")
        text = st.text_area("Введите текст сюда")
        uploaded_text = upload_file()
        if uploaded_text is not None:
            text = uploaded_text

        # Кнопка анализа текста
        if st.button("Анализировать"):
            if text:
                analysis_result = analyze_text_with_nn(text)
                st.subheader("Результат анализа:")
                st.write(analysis_result)
            else:
                st.warning("Загрузите текст для анализа")

    elif menu_selection == "FAQ":
        st.header("FAQ")
        st.markdown("1. **Что делает Анализатор текстовых пресс-релизов?**")
        st.markdown("   Анализатор позволяет провести глубокий анализ текстовых пресс-релизов, выявляя ключевую информацию и важные моменты.")
        st.markdown("2. **Как загрузить текст для анализа?**")
        st.markdown("   Вы можете ввести текст в поле ввода или загрузить файл Word с помощью кнопки 'Загрузить файл'.")

if __name__ == "__main__":
    main()
