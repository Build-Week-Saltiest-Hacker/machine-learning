# machine-learning
How the ML component of our project works for those who need to reference in when they are doing interviews or later in time:

Our data science team connect to the HackerNews API and performed some exploratory data analysis. After examining the indented goals of the Salty Troll App, our team opted to use a Sentiment Analysis user VADER, an open-source python library specifically designed for social media texts. 

At a high level, the Vader Sentiment Analysis examines a comment/text and provides 4 scores:
A Positivity Score (how positive the text is)
A Negativity Score (how negative the text is)
Neutral Score (how neutral the text is) 
A Final “Compound/Vader” Score on a scale of 1 to -1 which is an overall representation of the sentiment of a comment. 

We used the Vader Score because the algorithm:
Doesn’t require any training data
Handles transitions: (it notices when people use words like “but” to detect a change in sentiment)
It is fast
Measure sentiment intensity (Notices when people say GREAT versus great. Takes into account !!! and weights other punctuation) 
Handles emojis, slang, emoticons
And finally is able to examine preceding text (The food here really isn’t that great). This will identify as negative rather than positive because of the work great. 

If you have any deeper questions let me know! 
