#import sys
import pygame
import game_functions as gf
from setting import Setting
from ship import Ship
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats

def run_game():     
# 初始化游戏并创建一个屏幕对象    
	pygame.init()
	ai_setting = Setting()
	screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
	pygame.display.set_caption("Alien Invasion")  
	# 创建一个用于存储游戏统计信息的实例
	stats = GameStats(ai_setting)
	ship = Ship(screen,ai_setting)
	#创建一个子弹的编组
	bullets = Group()
	aliens = Group()

	# 创建外星人群
	gf.create_fleet(ai_setting, screen,ship, aliens) 
	#alien = Alien(ai_setting, screen) 

	# 开始游戏的主循环
	while True:
	# 监视键盘和鼠标事件         
		gf.check_events(ai_setting,screen,ship,bullets)
		#绘制屏幕前先更新坐标值
		if stats.game_active: 
			ship.update()

			bullets.update()

			gf.update_bullets(ai_setting, screen, ship, aliens, bullets)
			gf.update_aliens(ai_setting, stats, screen, ship, aliens, bullets)

		# 让最近绘制的屏幕可见
		gf.update_screen(ai_setting, screen, ship, aliens, bullets) 

run_game()  