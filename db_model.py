# schema for SQL database
from data import app, db 


class HNuser(db.Model):
    """ SQL database class """
    username = db.Column(db.String(100), primary_key=True)
    post_id = db.Column(db.Integer)
    salty_rank = db.Column(db.Float, nullable=False)
    salty_comments = db.Column(db.Integer, nullable=False)
    # comments_total = db.Column(db.Integer, nullable=False)

    def __repr__(self)
        return f"User {self.username} -- Salty Ranking: {self.salty_rank}"
    
    def salty_hackers(self):
        """return user information in Json format """
        return {
            "username" : self.username,
            "date" : self.date,
            "salty_rank" : self.salty_rank,
            "salty_comments" : self.salty_comments,
        }

class Comments(db.Model):
    comment_id = db.Column(db.BigInteger, primary_key=True)
    username = db.Column(db.String(100), db.ForeignKey('user.username'))
    text = db.Column(db.String(3000))
    date = db.Column(db.BigInteger)

    def __repr__(self):
        return f"User {self.username} -- Comment: {self.text}"

    def salty_comments(self):
        """ returns comments in JSON format """
        return {
            "comment_id" : self.comment_id,
            "username" : self.username,
            "text" : self.text,
            "date" : self.date
            ""
        }
