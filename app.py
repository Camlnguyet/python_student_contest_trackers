# Streamlit UI
import streamlit as st
import pandas as pd
from analytics import get_score_df, get_summary_df, plot_line_chart, plot_bar_chart
from database import get_connection, init_db
from models import Student, Contest, Score

init_db()

st.set_page_config(
    page_title="Student Contest Tracker",
    page_icon="🏆",
    layout="wide"
)

st.title("🏆 Student Contest Tracker")
st.caption("Quản lý & phân tích kết quả thi thuật toán")

with st.sidebar:
    st.header("➕ Thêm dữ liệu")

    with st.expander("Thêm học sinh"):
        name = st.text_input("Tên học sinh")
        grade = st.text_input("Khối lớp (VD: 8, 9)")
        if st.button("Thêm học sinh"):
            if name:
                conn = get_connection()
                conn.execute(
                    "INSERT INTO students (name, grade) VALUES (?, ?)",
                    (name, grade)
                )
                conn.commit()
                conn.close()
                st.success(f"Đã thêm: {name}")
            else:
                st.warning("Vui lòng nhập tên!")

    with st.expander("Thêm cuộc thi"):
        contest_name = st.text_input("Tên cuộc thi")
        contest_date = st.date_input("Ngày thi")
        if st.button("Thêm cuộc thi"):
            if contest_name:
                conn = get_connection()
                conn.execute(
                    "INSERT INTO contests (name, date) VALUES (?, ?)",
                    (contest_name, str(contest_date))
                )
                conn.commit()
                conn.close()
                st.success(f"Đã thêm: {contest_name}")

    with st.expander("Nhập điểm"):
        conn = get_connection()
        students = pd.read_sql_query("SELECT * FROM students", conn)
        contests = pd.read_sql_query("SELECT * FROM contests", conn)
        conn.close()

        if not students.empty and not contests.empty:
            selected_student = st.selectbox(
                "Học sinh",
                students["id"].tolist(),
                format_func=lambda x: students[students["id"]==x]["name"].values[0]
            )
            selected_contest = st.selectbox(
                "Cuộc thi",
                contests["id"].tolist(),
                format_func=lambda x: contests[contests["id"]==x]["name"].values[0]
            )
            score_val = st.number_input("Điểm", min_value=0.0, max_value=100.0, step=0.5)
            if st.button("Lưu điểm"):
                conn = get_connection()
                conn.execute(
                    "INSERT INTO scores (student_id, contest_id, score) VALUES (?, ?, ?)",
                    (selected_student, selected_contest, score_val)
                )
                conn.commit()
                conn.close()
                st.success("Đã lưu điểm!")
        else:
            st.info("Cần có học sinh và cuộc thi trước.")

tab1, tab2, tab3 = st.tabs(["📊 Bảng xếp hạng", "📈 Biểu đồ", "📋 Dữ liệu thô"])

with tab1:
    st.subheader("Xếp hạng học sinh")
    summary = get_summary_df()
    if not summary.empty:
        st.dataframe(summary, use_container_width=True, hide_index=True)
    else:
        st.info("Chưa có dữ liệu.")

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        fig_line = plot_line_chart()
        if fig_line:
            st.plotly_chart(fig_line, use_container_width=True)
    with col2:
        fig_bar = plot_bar_chart()
        if fig_bar:
            st.plotly_chart(fig_bar, use_container_width=True)

with tab3:
    df = get_score_df()
    if not df.empty:

        excel_data = df.to_excel("/tmp/report.xlsx", index=False)
        with open("/tmp/report.xlsx", "rb") as f:
            st.download_button(
                label="📥 Tải báo cáo Excel",
                data=f,
                file_name="contest_report.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        st.dataframe(df, use_container_width=True, hide_index=True)
    else:
        st.info("Chưa có dữ liệu.")