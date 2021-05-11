class StreamerDAO():
    def __init__(self, db):
        self.db=db
    
    def cadastro(self,streamer):
        sql= "INSERT INTO streamer (id,name,level,stamina,subs,money)" \
            "VALUES(?, ?, ?, ?, ? ,?)" 

        cursor=self.db.cursor()
        cursor.execute(sql, (streamer.id,streamer.name,streamer.level,streamer.stamina,streamer.subs,streamer.money))
        self.db.commit()
        return cursor.lastrowid
    