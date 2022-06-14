def  mutliply_df_by_10(df):
    for col in df.columns:
        df[col] = df[col] * 10
    return df

# comment