from main import db

class Dry(db.Model):
    iddry = db.Column(db.Integer, primary_key=True)
    drycol = db.Column(db.String(45))

    def to_dict(self):
        return {
            "iddry": self.iddry,
            "drycol": self.drycol
        }
    
