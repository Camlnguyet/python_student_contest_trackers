# test analytics
from analytics import get_score_df, get_summary_df

df = get_score_df()
print("=== RAW DATA ===")
print(df)

summary = get_summary_df()
print("\n=== SUMMARY ===")
print(summary)