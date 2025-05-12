import streamlit as st

st.set_page_config(page_title="배그 퀴즈 앱", layout="centered")

st.title("배틀그라운드 퀴즈 앱")

st.write("배그 관련 문제를 풀고 제출을 눌러 정답을 확인해보세요!")

# 객관식 문제
st.subheader("1. 포친키(Pochinki)의 주요 특징은?")
mcq_answer = st.radio(
    "객관식 보기",
    (
        "맵 가장자리에 위치하고 고지대가 많다.",
        "맵 중심에 위치하며, 밀집된 저층 주택들과 미로 같은 골목길이 특징이다.",
        "공장과 컨테이너가 많아 차량 스폰이 집중된다.",
        "눈으로 덮인 설원 맵에 존재하며, 교전이 적다."
    )
)

# 주관식 문제
st.subheader("2. Kar98k에 사용하는 탄약 종류는?")
subjective_answer = st.text_input("주관식 답을 입력하세요 (예: 5.56mm)")

# 결과 확인
if st.button("제출"):
    st.write("---")
    st.subheader("결과")

    if mcq_answer == "맵 중심에 위치하며, 밀집된 저층 주택들과 미로 같은 골목길이 특징이다.":
        st.success("1번 객관식 정답입니다!")
    else:
        st.error("1번 객관식 오답입니다.")

    if subjective_answer.strip().replace(" ", "").lower() in ["7.62", "7.62mm"]:
        st.success("2번 주관식 정답입니다!")
    else:
        st.error("2번 주관식 오답입니다.")