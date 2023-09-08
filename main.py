import streamlit as st
#from docx import Document
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
# Функция для анализа текста (заглушка)
def analyze_text_with_nn(text):
    # Пример анализа: категория и выделенные элементы
    category1 = "BB"
    categoryru = "BB-"
    highlighted_text = "«Эксперт РА» подтвердил кредитный рейтинг <span style='background-color: #ff9c9c'>«ООО «НТЦ Евровент»»</span> на уровне."
    return category1, categoryru, highlighted_text

# Функция для загрузки файла Word
def upload_file():
    uploaded_file = st.file_uploader("Загрузите файл Word (.docx)", type=["docx"])
    if uploaded_file is not None:
        #doc = Document(uploaded_file)
        full_text = "\n".join([p.text for p in doc.paragraphs])
        return full_text
    return None

# Главная часть приложения
def main():
    st.title("Анализатор текстовых пресс-релизов")

    # Инициализация внутреннего состояния
    if "text" not in st.session_state:
        st.session_state.text = "«Эксперт РА» подтвердил кредитный рейтинг «ООО «НТЦ Евровент»» на уровне."

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
        text = st.text_area("Введите текст сюда", value=st.session_state.text, disabled=True)
        uploaded_text = upload_file()
        if uploaded_text is not None:
            text = uploaded_text

        # Кнопка анализа текста
        if st.button("Анализировать"):
            if text:
                st.session_state.text = text  # Обновляем значение внутреннего состояния

                category1, categoryru, highlighted_text = analyze_text_with_nn(text)

                # Отображение результата
                st.subheader("Результат анализа:")
                st.markdown(f"**Категория:** {category1}")
                st.markdown(f"**Категория_ru:** {categoryru}")
                st.markdown(f"**Выделенные элементы:** {highlighted_text}", unsafe_allow_html=True)
            else:
                st.warning("Загрузите текст для анализа")

    elif menu_selection == "FAQ":
        st.header("FAQ")
        st.markdown("1. **Что делает Анализатор текстовых пресс-релизов?**")
        st.markdown("   Анализатор позволяет провести глубокий анализ текстовых пресс-релизов.")
        st.markdown("2. **Как загрузить текст для анализа?**")
        st.markdown("   Вы можете ввести текст в поле ввода или загрузить файл Word с помощью кнопки 'Загрузить файл'.")

if __name__ == "__main__":
    main()
