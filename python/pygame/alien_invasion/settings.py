class Settings():
    def __init__(self):
        # 屏幕基本设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship基本设置
        self.ship_speed_factor = 1.5

        # bullet设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # 外星人设置
        self.alien_speed_factor = 1
        self.alien_drop_speed = 5
        # fleet_direction 为1 表示向右移动，为 -1 表示向左移
        self.fleet_direction = 1