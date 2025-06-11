import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(
    page_title="✨ 엘든 링 플레이어 스타일 조언 마법사 ⚔️🏹",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 스타일링 (CSS) ---
css_styles = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&family=Cinzel:wght@400;700&display=swap');
    
    body {
        font-family: 'Noto Sans KR', sans-serif;
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%); /* 다크 판타지 배경 */
        color: #ecf0f1; /* 밝은 텍스트 색상 */
        margin: 0;
        padding: 0;
    }
    .main {
        background-color: #1a1a1a; /* 어두운 컨텐츠 영역 */
        padding: 50px;
        border-radius: 20px;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.4); /* 깊고 어두운 그림자 */
        max-width: 1000px; /* 최대 너비 */
        margin: 40px auto;
        border: 2px solid #5a5a5a; /* 은은한 테두리 */
    }
    .stSelectbox > div > div {
        background-color: #333333; /* 셀렉트 박스 배경 */
        border-radius: 12px;
        border: 1px solid #7f8c8d;
        padding: 10px;
        font-size: 1.1em;
        color: #ecf0f1;
    }
    .stSelectbox > div > div:hover {
        border-color: #3498db;
    }
    .stButton > button {
        background-color: #e74c3c; /* 버튼 색상 (강렬한 붉은색) */
        color: white;
        font-weight: bold;
        border-radius: 12px;
        padding: 12px 25px;
        border: none;
        box-
