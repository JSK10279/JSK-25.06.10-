import streamlit as st

# --- 페이지 설정 (화려한 테마와 넓은 레이아웃) ---
st.set_page_config(
    page_title="✨ AI 공부 플래너 & 맞춤형 조언 마법사 🧙‍♀️",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 스타일링 (CSS) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');
    body {
        font-family: 'Noto Sans KR', sans-serif;
        background-color: #e0f7fa; /* 부드러운 하늘색 배경 */
    }
    .main {
        background-color: #ffffff; /* 컨텐츠 영역 흰색 배경 */
        padding: 40px;
        border-radius: 25px;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15); /* 깊은 그림자 */
    }
    .stSelectbox > div > div {
        background-color: #ffe0b2; /* 셀렉트 박스 배경색 (오렌지 계열) */
        border-radius: 15px;
        border: 2px solid #ffcc80;
        padding: 12px;
        font-size: 1.1em;
    }
    .stButton > button {
        background-color: #8e24aa; /* 버튼 색상 (진한 보라) */
        color: white;
        font-weight: bold;
        border-radius: 15px;
        padding: 12px 25px;
        border: none;
        box-shadow: 0 5px 15px rgba(142, 36, 170, 0.4);
        transition: all 0.3s ease;
        font-size: 1.1em;
    }
    .stButton > button:hover {
        background-color: #4a148c; /* 호버 시 더 진한 보라 */
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(142, 36, 170, 0.6);
    }
    .stMarkdown h1 {
        color: #f50057; /* 핫핑크 제목 */
        text-align: center;
        font-size: 4.0em;
        text-shadow: 3px 3px 8px rgba(0,0,0,0.15);
        margin-bottom: 40px;
        font-weight: 700;
    }
    .stMarkdown h2 {
        color: #ff9800; /* 오렌지 소제목 */
        border-bottom: 4px solid #ffeb3b;
        padding-bottom: 15px;
        margin-top: 50px;
        font-size: 2.5em;
        text-align: center;
    }
    .stMarkdown h3 {
        color: #2196f3; /* 파란색 부제목 */
        font-size: 1.8em;
        margin-top: 30px;
        border-left: 5px solid #2196f3;
        padding-left: 10px;
    }
    .advice-box {
        background-color: #fffde7; /* 연한 노란색 배경 */
        padding: 25px;
        border-radius: 15px;
        margin-top: 25px;
        border: 2px dashed #ffd54f; /* 점선 테두리 */
        font-size: 1.1em;
        line-height: 1.8;
    }
    .advice-box p {
        margin-bottom: 10px;
        color: #424242;
    }
    .general-advice-box {
        background-color: #e8f5e9; /* 연한 초록색 배경 */
        padding: 25px;
        border-radius: 15px;
        margin-top: 25px;
        border: 2px dashed #81c784;
        font-size: 1.1em;
        line-height: 1.8;
    }
    .emoji-large {
        font-size: 2.0em;
        margin-right: 15px;
    }
    .emoji-medium {
        font-size: 1.5em;
        margin-right: 10px;
    }
</style
