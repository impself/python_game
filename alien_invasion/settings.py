class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed=1.5
        self.ship_limit=3
        #子弹设置
        self.bullet_speed=1.5
        self.bullet_width=1000
        self.bullet_height=15
        self.bullet_color=(60,60,60)
        self.bullet_allowed=3
        self.alien_speed=0.5
        self.fleet_drop_speed=6
        #fleet direction为1表示向右移，为-1表示向左移
        self.fleet_direction=1
        self.speedup_scale=1.1
        self.score_scale=1.5
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        #初始化随游戏进行而变化的设置
        self.ship_speed=1.0
        self.bullet_speed=3.0
        self.alien_speed=1.0
        self.fleet_direction=1
        self.alien_points=50
        #1表示向右，-1表示向左
    def increase_speed(self):
        #提高速度设置和分数设置
        self.ship_speed*=self.speedup_scale
        self.bullet_speed*=self.speedup_scale
        self.bullet_speed*=self.speedup_scale
        self.alien_points=int(self.alien_points*self.score_scale)
        
    