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

    def pesquisar(self, busca):
        sql = "SELECT * FROM streamer WHERE id = ?"
        cursor = self.db.cursor()
        cursor.execute(sql, (busca,))
        self.db.commit()
        return cursor.fetchall()

    def atualiza_stamina(self, id, quant): 
        sql = "UPDATE streamer SET stamina=? WHERE id = ?"
        cursor = self.db.cursor()
        cursor.execute(sql, (quant,id))
        self.db.commit()
        return cursor.fetchall()
        
    def atualiza_dinheiro(self, id, quant): 
        sql = "UPDATE streamer SET money=? WHERE id = ?"
        cursor = self.db.cursor()
        cursor.execute(sql, (quant,id))
        self.db.commit()
        return cursor.fetchall()
    
    def atualiza_subs(self, id, quant): 
        sql = "UPDATE streamer SET subs=? WHERE id = ?"
        cursor = self.db.cursor()
        cursor.execute(sql, (quant,id))
        self.db.commit()
        return cursor.fetchall()
    
    def atualiza_level(self, id, quant): 
        sql = "UPDATE streamer SET level=? WHERE id = ?"
        cursor = self.db.cursor()
        cursor.execute(sql, (quant,id))
        self.db.commit()
        return cursor.fetchall()
    
    
