
class Gamer:
    def __init__(self, gamertag):
        self.gamertag = gamertag
        self.kda = -1
        self.win_rate = -1
        self.rank_open = -1
        self.rank_kbm_sd = -1
        self.rank_con_sd = -1

    def set_kda(self, new_kda):
        self.kda = new_kda
    def set_win_rate(self, new_win_rate):
        self.win_rate = new_win_rate
    def set_rank_open(self, new_rank_open):
        self.rank_open = new_rank_open
    def set_rank_kbm_sd(self, new_rank_kbm_sd):
        self.rank_kbm_sd = new_rank_kbm_sd
    def set_rank_con_sd(self, new_rank_con_sd):
        self.rank_con_sd = new_rank_con_sd
    def set_stats(self, new_kda, new_win_rate, new_rank_open, new_rank_kbm_sd, new_rank_con_sd):
        self.kda = new_kda
        self.win_rate = new_win_rate
        self.rank_open = new_rank_open
        self.rank_kbm_sd = new_rank_kbm_sd
        self.rank_con_sd = new_rank_con_sd

    def get_gamertag(self):
        return self.gamertag    
    def get_kda(self):
        return self.kda
    def get_win_rate(self):
        return self.win_rate 
    def get_rank_open(self):
        return self.rank_open
    def get_rank_kbm_sd(self):
        return self.get_rank_kbm_sd 
    def get_rank_con_sd(self):
        return self.get_rank_con_sd 
    def get_stats(self):
        return {'gamertag': self.gamertag, 'kda': self.kda, 'win_rate': self.win_rate, 'rank_open': self.rank_open, 'rank_kbm_sd': self.rank_kbm_sd, 'rank_con_sd': self.rank_con_sd}

    