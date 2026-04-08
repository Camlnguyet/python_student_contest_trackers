# Analyze data and draw chart
import pandas as pd
import plotly.express as px 
from database import get_connection

def get_score_df():
    connection = get_connection()
    df = pd.read_sql_query("""
        SELECT
            s.name as student,
            c.name as contest,
            c.date as date,
            sc.score
        FROM scores sc
        JOIN students s ON sc.student_id = s.id
        JOIN contests c ON sc.contest_id = c.id
        ORDER BY c.date
                           """, connection)
    connection.close()
    return df

def get_summary_df():
    df = get_score_df()
    if df.empty:
        return pd.DataFrame()
    
    summary = df.groupby("student")["score"].agg(
        average="mean",
        highest="max",
        lowest="min",
        total_contests="count"
    ).reset_index()
    
    summary["rank"] = summary["average"].rank(
        ascending=False, method="min"
    ).astype(int)
    
    summary = summary.sort_values("rank")
    summary["average"] = summary["average"].round(2)
    return summary

def plot_line_chart():
    df = get_score_df()
    if df.empty:
        return None
    fig = px.line(
        df,
        x="contest",
        y="score",
        color="student",
        markers=True,
        title="Tiến độ học sinh qua các cuộc thi",
        labels={"contest": "Cuộc thi", "score": "Điểm", "student": "Học sinh"}
    )
    fig.update_layout(
        plot_bgcolor="white",
        hovermode="x unified"
    )
    return fig

def plot_bar_chart():
    summary = get_summary_df()
    if summary.empty:
        return None
    
    fig = px.bar(
        summary,
        x="student",
        y="average",
        color="student",
        title="So sánh điểm trung bình",
        labels={"student": "Học sinh", "average": "Điểm TB"},
        text="average"
    )
    fig.update_traces(textposition="outside")
    fig.update_layout(
        plot_bgcolor="white",
        showlegend=False
    )
    return fig