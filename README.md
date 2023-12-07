# AndroidAppnalysis
Analyzing Android App market by category, and identifying apps with strongest review sentiment scores.

Project objectives
  1: Read csv files and perform basic cleaning and validation on the apps DataFrame
  2: Collect aggregate statistics of apps, grouped by Category
  3: Find the top 10 free FINANCE apps, rated by highest average Sentiment Scores

Dataset used was uploaded in 2018 on Kaggle at 
https://www.kaggle.com/datasets/lava18/google-play-store-apps
and renamed as such

googleplaystore.csv ->
datasets/apps.csv
This file contains all the details of the apps on Google Play. There are 9 features that describe a given app.

    App: Name of the app
    Category: Category of the app. Some examples are: ART_AND_DESIGN, FINANCE, COMICS, BEAUTY etc.
    Rating: The current average rating (out of 5) of the app on Google Play
    Reviews: Number of user reviews given on the app
    Size: Size of the app in MB (megabytes)
    Installs: Number of times the app was downloaded from Google Play
    Type: Whether the app is paid or free
    Price: Price of the app in US$
    Last Updated: Date on which the app was last updated on Google Play

googleplaystore_user_reviews ->
datasets/user_reviews.csv
This file contains a random sample of 100 most helpful first user reviews for each app. The text in each review has been pre-processed and passed through a sentiment analyzer.

    App: Name of the app on which the user review was provided. Matches the App column of the apps.csv file
    Review: The pre-processed user review text
    Sentiment Category: Sentiment category of the user review - Positive, Negative or Neutral
    Sentiment Score: Sentiment score of the user review. It lies between [-1,1]. A higher score denotes a more positive sentiment.

