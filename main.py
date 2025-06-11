import streamlit as st

# 페이지 설정 (화려한 테마와 넓은 레이아웃)
st.set_page_config(
    page_title="✨ MBTI 맞춤형 직업 추천 💫",
    page_icon="🌈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 스타일링 (CSS) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');
    body {
        font-family: 'Noto Sans KR', sans-serif;
        background-color: #f0f2f6; /* 부드러운 배경색 */
    }
    .main {
        background-color: #ffffff; /* 컨텐츠 영역 흰색 배경 */
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); /* 부드러운 그림자 */
    }
    .stSelectbox > div > div {
        background-color: #e6f7ff; /* 셀렉트 박스 배경색 */
        border-radius: 10px;
        border: 1px solid #90caf9;
        padding: 10px;
    }
    .stButton > button {
        background-color: #ff69b4; /* 버튼 색상 (핫핑크) */
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
        box-shadow: 0 4px 10px rgba(255, 105, 180, 0.4);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #ff1493; /* 호버 시 진한 핑크 */
        transform: translateY(-2px);
        box-shadow: 0 6px 15px rgba(255, 105, 180, 0.6);
    }
    .stMarkdown h1 {
        color: #8a2be2; /* 보라색 제목 */
        text-align: center;
        font-size: 3.5em;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 30px;
    }
    .stMarkdown h2 {
        color: #ff4500; /* 주황색 소제목 */
        border-bottom: 3px solid #ffd700;
        padding-bottom: 10px;
        margin-top: 40px;
        font-size: 2em;
    }
    .stMarkdown h3 {
        color: #4682b4; /* 파란색 부제목 */
        font-size: 1.5em;
        margin-top: 20px;
    }
    .job-list {
        background-color: #fffacd; /* 레몬시폰 배경 */
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        border: 1px dashed #ffa07a;
    }
    .job-item {
        font-size: 1.1em;
        margin-bottom: 10px;
        color: #333;
    }
    .emoji {
        font-size: 1.5em;
        margin-right: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- MBTI 데이터 (이모지와 함께) ---
mbti_data = {
    "ISTJ": {
        "description": "✅ 현실적이고 체계적인 당신!",
        "jobs": ["회계사 📊", "공무원 🏛️", "경찰관 👮‍♀️", "군인 🎖️", "은행원 🏦", "연구원 🔬"]
    },
    "ISFJ": {
        "description": "💖 따뜻하고 헌신적인 당신!",
        "jobs": ["간호사 👩‍⚕️", "사회복지사 🤝", "유치원 교사 🍎", "사서 📚", "영양사 🥗", "행정 보조 📋"]
    },
    "INFJ": {
        "description": "🌟 통찰력 있는 이상주의자 당신!",
        "jobs": ["심리 상담사 🗣️", "작가 ✍️", "예술가 🎨", "성직자 🙏", "대학교수 🧑‍🏫", "환경 운동가 🌍"]
    },
    "INTJ": {
        "description": "🧠 전략적이고 독립적인 당신!",
        "jobs": ["과학자 🧪", "프로그래머 💻", "건축가 🏗️", "재무 분석가 📈", "변호사 ⚖️", "엔지니어 🛠️"]
    },
    "ISTP": {
        "description": "🔧 논리적이고 호기심 많은 당신!",
        "jobs": ["기술자 🧑‍🔧", "파일럿 ✈️", "탐정 🕵️‍♀️", "운동선수 🏅", "사진작가 📸", "요리사 👨‍🍳"]
    },
    "ISFP": {
        "description": "🎨 예술적이고 자유로운 당신!",
        "jobs": ["디자이너 👗", "음악가 🎶", "댄서 💃", "조경사 🌳", "패션 스타일리스트 🛍️", "플로리스트 💐"]
    },
    "INFP": {
        "description": "🦄 창의적이고 사려 깊은 당신!",
        "jobs": ["작가 📝", "시인 📜", "일러스트레이터 🖍️", "초등 교사 👩‍🏫", "편집자 📖", "동물 조련사 🐶"]
    },
    "INTP": {
        "description": "🤔 분석적이고 혁신적인 당신!",
        "jobs": ["컴퓨터 프로그래머 💻", "수학자 ➕", "철학자 🧐", "교수 🎓", "연구원 🔬", "데이터 과학자 📊"]
    },
    "ESTP": {
        "description": "🚀 활동적이고 에너지가 넘치는 당신!",
        "jobs": ["기업가 💡", "영업 관리자 📞", "경찰 🚨", "소방관 🚒", "스포츠 코치 ⚽", "배우 🎭"]
    },
    "ESFP": {
        "description": "🥳 사교적이고 즉흥적인 당신!",
        "jobs": ["연예인 🎤", "이벤트 플래너 🎉", "관광 가이드 🗺️", "미용사 💇‍♀️", "방송인 📺", "댄스 강사 🕺"]
    },
    "ENFP": {
        "description": "✨ 열정적이고 영감을 주는 당신!",
        "jobs": ["마케터 📣", "컨설턴트 🗣️", "크리에이터 🎥", "강사 👨‍🏫", "PR 전문가 📢", "예술 치료사 🧡"]
    },
    "ENTP": {
        "description": "💡 재치 있고 똑똑한 당신!",
        "jobs": ["발명가 ⚙️", "기업가 💰", "변호사 🧑‍⚖️", "엔지니어 👷", "과학 기자 ✍️", "전략 기획자 🗺️"]
    },
    "ESTJ": {
        "description": "📈 현실적이고 효율적인 당신!",
        "jobs": ["경영자 💼", "관리자 👩‍💼", "세일즈 매니저 💲", "교장 선생님 🏫", "프로젝트 매니저 📌", "재무 관리자 💵"]
    },
    "ESFJ": {
        "description": "🌸 친화력 있고 협력적인 당신!",
        "jobs": ["교사 👩‍🏫", "상담사 🗨️", "인사 담당자 🧑‍🤝‍🧑", "영업 사원 🤝", "결혼 플래너 👰", "간호사 🏥"]
    },
    "ENFJ": {
        "description": "💖 리더십 있고 통솔력 있는 당신!",
        "jobs": ["교사 🧑‍🏫", "정치인 🏛️", "사회 운동가 📢", "코치 🏆", "HR 전문가 👩‍💻", "성직자 🛐"]
    },
    "ENTJ": {
        "description": "👑 타고난 리더십의 소유자 당신!",
        "jobs": ["CEO 🏢", "경영 컨설턴트 📈", "정치가 🧑‍⚖️", "투자 은행가 💰", "사업가 🚀", "변호사 👩‍⚖️"]
    },
}

# --- 타이틀 및 설명 ---
st.markdown("<h1>✨ 나의 MBTI는? 💫 <br> 🌈 직업 추천 탐험! 🚀</h1>", unsafe_allow_html=True)
st.markdown("### 당신의 성격 유형에 딱 맞는 ✨ 환상의 직업을 찾아보세요! 🤩", unsafe_allow_html=True)

st.image("https://images.unsplash.com/photo-1517430154093-6c8a7d656828?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
         caption="✨ 당신의 미래를 탐험해요! ✨",
         use_column_width=True)

st.markdown("---")

# --- MBTI 선택 드롭다운 ---
st.markdown("<h2>👇 당신의 MBTI를 선택해주세요! 👇</h2>", unsafe_allow_html=True)
selected_mbti = st.selectbox(
    "MBTI 유형을 선택하세요:",
    options=["MBTI를 선택해주세요!"] + sorted(list(mbti_data.keys())),
    index=0,
    help="당신의 4글자 MBTI 코드를 선택해주세요. 😊"
)

# --- 결과 표시 ---
if selected_mbti != "MBTI를 선택해주세요!":
    st.markdown(f"<h2>🎉 {selected_mbti} 유형을 선택하셨군요! 🎉</h2>", unsafe_allow_html=True)
    st.markdown(f"<h3>{mbti_data[selected_mbti]['description']}</h3>", unsafe_allow_html=True)

    st.markdown("<h3>🎯 당신에게 어울리는 직업들은 다음과 같아요! 🎯</h3>", unsafe_allow_html=True)
    st.markdown("<div class='job-list'>", unsafe_allow_html=True)
    for job in mbti_data[selected_mbti]['jobs']:
        st.markdown(f"<p class='job-item'><span class='emoji'>✨</span> {job}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
        <p style="text-align: center; margin-top: 30px; font-size: 1.2em; color: #6a5acd;">
            🚀 이것은 단지 추천일 뿐! 당신의 꿈과 열정을 따라가세요! 💖<br>
            ✨ 세상은 당신의 잠재력으로 가득 차 있답니다! ✨
        </p>
    """, unsafe_allow_html=True)

else:
    st.info("⬆️ 위에 있는 드롭다운 메뉴에서 당신의 MBTI를 선택해주세요! 🌈")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #a9a9a9;'>Made with ❤️ by Streamlit & Gemini 🚀</p>", unsafe_allow_html=True)
