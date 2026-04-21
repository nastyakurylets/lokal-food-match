import streamlit as st
import random

FOOD_DATA = [
    {"name": "Реберця", "img": "https://example.com/ribs.jpg", "category": "М'ясоїд"},
    {"name": "Бургер з яловичиною", "img": "https://example.com/burger.jpg", "category": "М'ясоїд"},
    {"name": "Паста Карбонара", "img": "https://example.com/carbonara.jpg", "category": "М'ясоїд"},
    {"name": "Стейк Рібай", "img": "https://example.com/steak.jpg", "category": "М'ясоїд"},
    {"name": "Курячі крильця BBQ", "img": "https://example.com/wings.jpg", "category": "Любитель гострого"},
    {"name": "Шашлик зі свинини", "img": "https://example.com/shashlik.jpg", "category": "М'ясоїд"},
    {"name": "Лазанья", "img": "https://example.com/lasagna.jpg", "category": "М'ясоїд"},
    {"name": "Сирний суп", "img": "https://example.com/cheese_soup.jpg", "category": "Комфортна їжа"},
    {"name": "Борщ з пампушками", "img": "https://example.com/borscht.jpg", "category": "Комфортна їжа"},
    {"name": "Вареники з картоплею", "img": "https://example.com/varenyky.jpg", "category": "Комфортна їжа"},
    {"name": "Деруни", "img": "https://example.com/deruny.jpg", "category": "Комфортна їжа"},
    {"name": "Суші Філадельфія", "img": "https://example.com/sushi.jpg", "category": "Любитель морепродуктів"},
    {"name": "Поке з лососем", "img": "https://example.com/poke.jpg", "category": "Любитель морепродуктів"},
    {"name": "Креветки темпура", "img": "https://example.com/tempura.jpg", "category": "Любитель морепродуктів"},
    {"name": "Рамен", "img": "https://example.com/ramen.jpg", "category": "Любитель гострого"},
    {"name": "Том Ям", "img": "https://example.com/tomyam.jpg", "category": "Любитель гострого"},
    {"name": "Фалафель", "img": "https://example.com/falafel.jpg", "category": "Веган"},
    {"name": "Хумус з пітою", "img": "https://example.com/hummus.jpg", "category": "Веган"},
    {"name": "Овочеве карі", "img": "https://example.com/curry.jpg", "category": "Веган"},
    {"name": "Салат Цезар", "img": "https://example.com/caesar.jpg", "category": "Легка їжа"},
    {"name": "Грецький салат", "img": "https://example.com/greek.jpg", "category": "Легка їжа"},
    {"name": "Авокадо тост", "img": "https://example.com/avocado_toast.jpg", "category": "Легка їжа"},
    {"name": "Сирники", "img": "https://example.com/syrnyky.jpg", "category": "Солодкоїжка"},
    {"name": "Чізкейк", "img": "https://example.com/cheesecake.jpg", "category": "Солодкоїжка"},
    {"name": "Брауні", "img": "https://example.com/brownie.jpg", "category": "Солодкоїжка"},
    {"name": "Наполеон", "img": "https://example.com/napoleon.jpg", "category": "Солодкоїжка"},
    {"name": "Тірамісу", "img": "https://example.com/tiramisu.jpg", "category": "Солодкоїжка"},
    {"name": "Млинці з Nutella", "img": "https://example.com/pancakes.jpg", "category": "Солодкоїжка"},
    {"name": "Піца Маргарита", "img": "https://example.com/margarita.jpg", "category": "Комфортна їжа"},
    {"name": "Кесадилья", "img": "https://example.com/quesadilla.jpg", "category": "Любитель гострого"},
    {"name": "Тако з куркою", "img": "https://example.com/taco.jpg", "category": "Любитель гострого"},
]

if 'index' not in st.session_state:
    st.session_state.index = 0
    st.session_state.stats = {}
    random.shuffle(FOOD_DATA)  

st.title("Food Match")

if st.session_state.index < len(FOOD_DATA):
    current_food = FOOD_DATA[st.session_state.index]
    
    # 1. Прогрес-бар
    progress = st.session_state.index / len(FOOD_DATA)
    st.progress(progress)
    
    # 2. Картка страви
    st.image(current_food['img'], use_container_width=True)
    st.subheader(current_food['name'])
    
    # 3. Кнопки вибору
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("❌", use_container_width=True):
            st.session_state.index += 1
            st.rerun()
            
    with col2:
        if st.button("❤️", use_container_width=True):
            category = current_food['category']
            st.session_state.stats[category] = st.session_state.stats.get(category, 0) + 1
            st.session_state.index += 1
            st.rerun()
else:
    # Екран результатів
    st.balloons()
    st.success("Гру завершено! Ми підібрали ваш профіль.")
    top_cat = max(st.session_state.stats, key=st.session_state.stats.get)
    st.write(f"Ви — справжній **{top_cat}**! Отримайте ваш бонус у LOKAL.")


st.markdown("""
    <style>
    .stButton>button {
        border-radius: 20px;
        height: 3em;
        background-color: #e30613; /* Червоний колір LOKAL */
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
