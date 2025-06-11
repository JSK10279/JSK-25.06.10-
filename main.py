import streamlit as st

# --- 페이지 설정 (화려한 테마와 넓은 레이아웃) ---
st.set_page_config(
    page_title="✨ AI 공부 플래너 & 맞춤형 조언 마법사 🧙‍♀️",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 스타일링 (CSS) ---
# >>>>>> 매우 중요! 이 부분의 시작과 끝 따옴표를 꼭 확인해주세요! <<<<<<
# CSS 코드를 여러 줄로 나누어 오류 가능성을 줄입니다.
css_styles = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');
    
    body {
        font-family: 'Noto Sans KR', sans-serif;
        background-color: #e0f7fa; /* 부드러운 하늘색 배경 */
        margin: 0;
        padding: 0;
    }
    .main {
        background-color: #ffffff; /* 컨텐츠 영역 흰색 배경 */
        padding: 40px;
        border-radius: 25px;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15); /* 깊은 그림자 */
        max-width: 1200px; /* 최대 너비 설정 */
        margin: 30px auto; /* 중앙 정렬 및 상하 여백 */
    }
    .stSelectbox > div > div {
        background-color: #ffe0b2; /* 셀렉트 박스 배경색 (오렌지 계열) */
        border-radius: 15px;
        border: 2px solid #ffcc80;
        padding: 12px;
        font-size: 1.1em;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
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
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #4a148c; /* 호버 시 더 진한 보라 */
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(142, 36, 170, 0.6);
    }
    .stMarkdown h1 {
        color: #f50057; /* 핫핑크 제목 */
        text-align: center;
        font-
