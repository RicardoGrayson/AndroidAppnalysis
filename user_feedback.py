##read user_reviews.csv file
user_feedback = pd.read_csv('datasets/user_reviews.csv')

##perform preliminary EDA
#print(user_feedback.info())
#print(user_feedback.isna().value_counts())
#print(user_feedback.head())

##filter apps DataFrames by Category and Type
finance_apps = apps[apps['Category']=='FINANCE']
free_finance_apps =finance_apps[finance_apps['Type']=='Free']

##perform merge of user_feedback and filtered apps dataset
user_feedback_merged = pd.merge(user_feedback,free_finance_apps,on = 'App')

##group merged DataFrame by App name and calculate average Sentiment Score
user_feedback_merged_grouped = user_feedback_merged.groupby('App').agg({'Sentiment Score':'mean'})
#print(user_feedback_merged_grouped)

##sort filtered apps by Sentiment Score, descending
top_10_user_feedback=pd.DataFrame(user_feedback_merged_grouped.sort_values('Sentiment Score', ascending=False))
top_10_user_feedback = top_10_user_feedback.reset_index()
display(top_10_user_feedback[:10])
