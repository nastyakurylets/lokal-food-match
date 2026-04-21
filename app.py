import streamlit as st
import random
import time
import requests
import pandas as pd

# --- НАЛАШТУВАННЯ ТА ДАНІ ---
MAX_SWIPES = 11 # Обмежуємо кількість свайпів

if 'food_pool' not in st.session_state:
    FOOD_DATA = [
        {"name": "Реберця", "img": "ribs.jpg", "category": "М'ясоїд", "desc": "Полоски ребер свинні мариновані, смажені на мангалі. Соус на вибір: Барбекю, гірчичний або азійський."},
        {"name": "Бургер з яловичиною", "img": "burger.jpg", "category": "М'ясоїд", "desc": "Вершкова булка, рублена яловича котлета, мариновані огірки, смажений шпондер та сир чедер."},
        {"name": "Курячі крильця", "img": "wings.jpg", "category": "Любитель гострого", "desc": "Ті самі, ідеальні курячі крильця з хрусткою скоринкою з доставкою у Львові."},
        {"name": "Курячі крильця", "img": "wing.jpg", "category": "Любитель гострого", "desc": "Ті самі, ідеальні курячі крильця з хрусткою скоринкою з доставкою у Львові."},
        {"name": "Том Ям Кха Гай", "img": "tomyam.jpg", "category": "Кисло-гострий тайський том ям з куркою. На основі курячого бульйону з ароматним лемонграсом, імбиром та листям кафір-лайму та кокосовими вершками. Доповнений соковитим курячим філе, рибним соусом, печеним баклажаном у кукурудзяному крохмалі, гливами, броколі, салатом ромен та кінзою з додаванням зеленої олії. Пікантність додає тайська паста з сушеного чилі та соєвої олії — розмішуй за смаком. Подається з рисом, часточкою лайму та свіжою кінзою."},
        {"name": "Кесадилья", "img": "quesadilla.jpg", "category": "Любитель гострого", "desc": "Рвана яловичина, квасоля, сир, салат: кукурудза, авокадо, цибуля біла, сальса, маринована цибуля, «Крема Мексикана»."},
        {"name": "Борщ з пампушками", "img": "borscht.jpg", "category": "Комфортна їжа", "desc": "Бульйон яловичий, фреш буряка, картопля, капустка, засмажка, кістка яловича, шийна частина яловичини. Додатково: сметана, сало, цибуля зелена, солені лимони, квашенина і пампушки із соусом чімічурі."},
        {"name": "Вареники з картоплею", "img": "varenyky.jpg", "category": "Комфортна їжа", "desc": "Тісто: борошно пшеничне вищого ґатунку, вода питна, олія соняшникова рафінована, яйце куряче, сіль кухонна. Начинка: картопля варена, цибуля ріпчаста смажена, сіль кухонна, приправа перець чорний мелений. Містить алергени: глютен, яйце куряче."},
        {"name": "Пструг класичний", "img": "fish.jpg", "category": "Любитель морепродуктів", "desc": "Класична річкова форель, печена вже солена та злегка перчена, подається з цитриною."},
        {"name": "Лосось з мангалу", "img": "grilled_salmon.jpg", "category": "Любитель морепродуктів", "desc": "Лосось марнується у розмарині, оливковій олії, солі та перці. Подається з морквяний пюре, печеним гарбузом та броколі."},
        {"name": "Оладки з вишнею", "img": "cherry_pancakes.jpg", "category": "Солодкоїжка", "desc": "З нашим смородиновим варенням та шоколадом."},
        {"name": "Оладки з вишнею", "img": "cherry_pancake.jpg", "category": "Солодкоїжка", "desc": "З нашим смородиновим варенням та шоколадом."},
        {"name": "Рулет меренговий", "img": "meringue_roll.jpg", "category": "Солодкоїжка", "desc": "Меренговий корж, крем на основі сиру маскарпоне, вершків, фісташкової пасти, полуничний наповнювач."}
    ]
    st.session_state.food_pool = random.sample(FOOD_DATA, min(MAX_SWIPES, len(FOOD_DATA)))
    st.session_state.index = 0
    st.session_state.stats = []
    st.session_state.flipped = False # Стан: чи бачимо ми опис

# --- ФУНКЦІЇ АНАЛІТИКИ ---
def log_action(food_name, action):
    st.session_state.stats.append({
        "item": food_name,
        "action": action,
        "time": time.strftime("%H:%M:%S")
    })

# --- ІНТЕРФЕЙС ---
st.title("Food Match")

if st.session_state.index < len(st.session_state.food_pool):
    current_food = st.session_state.food_pool[st.session_state.index]
    
    st.progress(st.session_state.index / MAX_SWIPES)

    if not st.session_state.flipped:
        # Безпечне відображення картинки
        try:
            st.image(current_food['img'], width=None) # width=None автоматично розтягує
        except:
            st.warning(f"Фото {current_food['img']} не знайдено.")
            
        if st.button("ℹ️ Що всередині?"):
            st.session_state.flipped = True
            st.rerun()
    else:
        st.info(f"**{current_food['name']}**\n\n{current_food['desc']}")
        if st.button("⬅️ Назад до фото"):
            st.session_state.flipped = False
            st.rerun()

    st.subheader(current_food['name'])
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("❌", use_container_width=True, key="dislike"):
            log_action(current_food['name'], "dislike")
            st.session_state.index += 1
            st.session_state.flipped = False
            st.rerun()
    with col2:
        if st.button("❤️", use_container_width=True, key="like"):
            log_action(current_food['name'], "like")
            st.session_state.index += 1
            st.session_state.flipped = False
            st.rerun()

else:
    st.balloons()
    st.header("Твій смаковий профіль готовий!")
    
    # Розрахунок результату
    category_counts = {}
    for record in st.session_state.stats:
        if record["action"] == "like":
            for food in st.session_state.food_pool:
                if food["name"] == record["item"]:
                    cat = food["category"]
                    category_counts[cat] = category_counts.get(cat, 0) + 1

    top_cat = max(category_counts, key=category_counts.get) if category_counts else "Гурман"
    st.success(f"Ви — справжній **{top_cat}**!")
    
    st.divider()
    st.subheader("📝 Коротке опитування")
    
    with st.form("survey_form", clear_on_submit=True):
        q1 = st.radio("Чи було вам цікаво свайпати страви?", ["Дуже", "Так собі", "Ні, нудно"])
        q2 = st.radio("Чи допомогли описи страв зробити вибір?", ["Так", "Ні", "Не відкривав їх"])
        q3 = st.text_input("Яку страву ви б додали?")
        
        if st.form_submit_button("Надіслати відгук"):
            try:
                # ВСТАВЛЯЄМО ВАШІ ID ТУТ
                form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfoP8pa1VyCzdiX-I8fs5O3KFdErfMTcntv8DPp-hIbn6B4OQ/formResponse"
                
                payload = {
                    "entry.1137718514": time.strftime("%Y-%m-%d %H:%M:%S"), # Timestamp
                    "entry.2014803387": top_cat,                             # Result
                    "entry.2083659996": q1,                                  # Q1
                    "entry.1571929600": q2,                                  # Q2
                    "entry.1415007899": q3,                                  # Q3
                    "entry.1902153314": str(st.session_state.stats)          # Full Stats
                }
                
                requests.post(form_url, data=payload)
                st.success("Дані надіслано! Дякуємо!")
            except:
                st.error("Помилка")
# --- СТИЛІ ---
st.markdown("""
    <style>
    .stButton>button {
        border-radius: 20px;
        height: 3em;
        background-color: #e30613;
        color: white;
    }
    .stProgress > div > div > div > div {
        background-color: #e30613;
    }
    </style>
    """, unsafe_allow_html=True)
