class GameStats:
    #跟踪游戏统计信息
    def __init__(self,ai_game):
        #统计初始化信息
        self.game_active=False
        self.settings=ai_game.settings
        self.reset_stats()
        self.high_score=0
    def reset_stats(self):
        #初始化在游戏运行期间可能变化的统计信息
        self.ship_left=self.settings.ship_limit
        self.score=0
        self.level=1
        
        