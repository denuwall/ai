import streamlit as st
#from docx import Document

# Функция для анализа текста (заглушка)
#def analyze_text_with_nn(text):
#    category1 = "BB"
#    categoryru = "BB-"
#    highlighted_text = "«Эксперт РА» подтвердил кредитный рейтинг <span style='background-color: #ff9c9c'>«ООО «НТЦ Евровент»»</span> на уровне."
#    return category1, categoryru, highlighted_text

def predict(features):
    categories = neuronka_ebanaya(features)
    return categories

# Функция для загрузки файла Word
def upload_file():
    uploaded_file = st.file_uploader("Загрузите файл Word (.docx)", type=["docx"])
    if uploaded_file is not None:
        #doc = Document(uploaded_file)
        full_text = "\n".join([p.text for p in doc.paragraphs])
        return full_text
    return None

# Функция для страницы "Авторы"
def authors_page():
    st.title("Авторы")
    
    authors = [
        ("**Зеленцов Александр** - ML", "tg: @Ktotoktoya"),
        ("**Щеткин Денис** - FullStack", "tg: @saint_onion"),
        ("**Тыркалов Никита** - сидит на парах", "tg: @DIOkk"),
        ("**Безднин Алексей** - сидит на парах", "tg: @Bezdnin"),
        ("**Никита Юрьев** - сидит в дискорде и делает метрику", "tg: @Serfett0")
    ]
    
    for author, link in authors:
        st.write(f"**{author}**")
        st.write(link)


#Скрытие нижней хуйни
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: ;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


# Главная часть приложения
def main():
    st.title("Анализатор текстовых пресс-релизов")

    st.markdown("---")

    # Инициализация внутреннего состояния
    if "text" not in st.session_state:
        st.session_state.text = ""

    # Стилизация менюшки
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

    # Варианты навигации в меню
    if st.sidebar.button("Анализатор", key="analyzer"):
        st.session_state.menu_selection = "Анализатор"
    if st.sidebar.button("FAQ", key="faq"):
        st.session_state.menu_selection = "FAQ"
    if st.sidebar.button("Авторы", key="authors"):
        st.session_state.menu_selection = "Авторы"

    menu_selection = st.session_state.get("menu_selection", "Анализатор")

    if menu_selection == "Анализатор":
        st.header("Анализатор")

        # Загрузка текста
        st.subheader("Загрузите текст:")
        default_text = ""
        text = st.text_area("Введите текст сюда", value=st.session_state.text)
        uploaded_text = upload_file()
        if uploaded_text is not None:
            text = uploaded_text

        # Кнопка анализа текста
        if st.button("Анализировать"):
            if text:
                st.session_state.text = text  # Обновляем значение внутреннего состояния

                categories = predict(text)  # Используем нейронку

                # Отображение результата
                st.subheader("Результат анализа:")
                st.markdown(f"**Категория:** {categories[0]}")
                st.markdown(f"**Категория_ru:** {categories[1]}")
                st.markdown(f"**Выделенные элементы:** {highlighted_text}", unsafe_allow_html=True)
            else:
                st.warning("Загрузите текст для анализа")

    elif menu_selection == "FAQ":
        st.header("FAQ")
        st.markdown("1. **Что делает Анализатор текстовых пресс-релизов?**")
        st.markdown("   Анализатор позволяет провести глубокий анализ текстовых пресс-релизов.")
        st.markdown("2. **Как загрузить текст для анализа?**")
        st.markdown("   Вы можете ввести текст в поле ввода или загрузить файл Word с помощью кнопки 'Загрузить файл'.")

    elif menu_selection == "Авторы":
        authors_page()

if __name__ == "__main__":
    main()