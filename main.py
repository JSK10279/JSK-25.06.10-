import streamlit as st
import random

def main():
    st.title("오늘의 식사 메뉴 추천 🍽️")

    # 메뉴 리스트 정의
    menu_options = [
        "김치찌개",
        "된장찌개",
        "비빔밥",
        "제육볶음",
        "불고기",
        "돈까스",
        "파스타",
        "피자",
        "햄버거",
        "초밥",
        "회덮밥",
        "칼국수",
        "냉면",
        "닭갈비",
        "삼겹살",
        "순대국",
        "뼈해장국",
        "부대찌개",
        "떡볶이",
        "치킨",
        "카레",
        "오므라이스",
        "짜장면",
        "짬뽕",
        "볶음밥"
    ]

    st.write("아래 버튼을 누르면 오늘의 식사 메뉴가 무작위로 선택됩니다!")

    if st.button("메뉴 추천 받기"):
        # 메뉴 리스트에서 무작위로 하나 선택
        selected_menu = random.choice(menu_options)

        st.subheader("오늘의 추천 메뉴는 바로...")
        st.success(f"✨ **{selected_menu}** ✨ 입니다!")
        st.balloons() # 메뉴 추천 시 풍선 효과

    st.markdown("---")
    st.write("다른 메뉴를 원하시면 '메뉴 추천 받기' 버튼을 다시 눌러주세요.")
    st.write("맛있는 식사 되세요! 😊")

if __name__ == "__main__":
    main()
