import pygame
from Settings import Settings

class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #游戏刚启动时处于活动状态
        self.game_active = False

        #在任何情况下都不重置最高得分
        self.top_score = 0
        self.top_score_file = "D:/QQrecv/python/alien_invasion/top_score_file.txt"
        self.load_top_score()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def store_top_score(self):
        """关闭游戏前，保存最高得分"""
        with open(self.top_score_file, 'w+') as file_obj:
            file_obj.write(str(self.top_score))


    def load_top_score(self):
        """初始化的时候，加载最新的文件"""
   #     top_score = 0
        try:
            with open(self.top_score_file, 'rb') as file_obj:
                self.top_score = int(file_obj.read())
        except FileNotFoundError:
            self.top_score = 0
            print("first time play alien invasion game!")

