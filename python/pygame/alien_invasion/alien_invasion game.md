alien_invasion game

  

# introduction                     

```python
import sys
import pygame

def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init() 
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    
    while True:
        """监视键盘和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        """让最近绘制的屏幕可见"""        
        pygame.display.flip()
        

run_game()
```

- `pygame.init()` 初始化背景设置，让pygame能正确地工作
- `pygame.display.set_mode()` 创建一个**名为 sereen 的显示窗口**，该游戏的所有图形元素都将在其中绘制。实参 (1200, 800) 是一个元组，制定了游戏窗口的尺寸：长1200像素，高度800像素



- **对象screen 是一个surface**。该游戏中每个元素(如外星人或飞船) 都是一个surface。 `display.set_mode` 返回的surface表示整个游戏窗口。激活游戏的动画循环后，每经过一次循环都将自动重新绘制该 surface。
- while循环包含一个事件循环 + 管理屏幕更新 的代码。**事件**是**用户执行的操作**，如按键或移动鼠标。
- 为访问pygame检测到的事件，我们使用方法 `pygame.event.get() `
- `pygame.display.flip() ` 命令在每次执行while循环时都绘制一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见。在我们移动游戏元素时，`pygame.display.flip()` 将不断更新屏幕，以显示元素的新位置，并在原来的位置隐藏元素，从而营造平滑移动的效果。
- 用 `sys.exit()` 退出程序



## 设置背景色



alien_invasion.py

```python
--snip--
def run_game():
    --snip--
    pygame.display.set_caption("Alien Invasion")
    
    # 设置背景色
    bg_color = (230, 230, 230)
    
    #开始游戏主循环
    while True:
        --snip--
        secreen.fill(bg_color)
```

screen.fill() : 用背景色填充屏幕



## 创建 settings 类

编写一个 settings 模块，其中包含一个 settings类 ，用于将所有设置存储在一个地方，以免在代码中到处添加设置。

settings.py

```python
class Settings():
    
    def __init__():
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
```



alien_invasion.py

```python
--snip--
from settings import Settings

def run_game():
    # 初始化pygame ，settings和screen对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    while True:
        --snip--
        screen.fill(ai_settings.bg_color)
        pygame.display.flip()
        
        
run_game()
```



## 添加飞机图像

pygame 默认加载位图 ( .bmp)



```
import pygame

class ship():
    
    def __init__(self, screen):
        self.screen = screen
        
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
```

`pygame.image.load() ` 返回一个**表示 ship的surface** ，并将这个surface存储到了 self.image 中。

加载图像后，使用 `get_rect()` 获取相应surface的属性 rect ，pygame的效率之所以如此高，是因为它让你能够像处理矩形 (rect 对象) 一样处理游戏元素，即使它们的形状并非矩形。

处理 rect 对象时，可使用矩形四角和中心的 x 和 y 坐标。通过设置这些值来指定矩形位置。

**要将游戏元素居中**，可设置相应 **rect对象属性 center、 centerx、 centery** 。要让**游戏元素与屏幕边缘对齐**，可使用属性 top 、bottom 、left 、right ；要调整游戏元素的水平或垂直位置，可使用属性 x 和 y ，它们分别是相应**矩形左上角**的 x 和 y 坐标。

方法 blitme() 根据 self.rect 指定的位置将图像绘制到屏幕上。



在屏幕上绘制飞船

alien_invasion.py

```python
--snip--
from settings import Settings
from ship import Ship

def run_game():
    --snip--
    
    #创建 ship
    ship = Ship(screen)
    
    while True:
        --snip--
        screen.fill(ai_settings.bg_color)
        ship.blitme() # 注意顺序，必须先填充背景再绘制ship
        
        
```



# 重构：模块 game_functions 

重构旨在简化既有代码的结构，使其更容易扩展。

创建 game_functions 的新模块，可避免 alien_invasion.py 过长，并使其逻辑更容易理解。



## function : check_events()

将管理事件的代码移动到 check_events 函数中，以简化 run_game() 并隔离事件管理循环。将事件管理与游戏其他方面( 如更新屏幕) 分离

```python
def check_events():
    """相应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
```



## function: update_screen()

```python
def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    pygame.display.flip()
```





game_functions.py

```python
import sys
import pygame

def check_events():
    """相应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
```



alien_invasion.py

```python
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    --snip--
    
    while True:
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)
        
run_game()
```





# 驾驶飞船

学习如何控制屏幕图像的移动



## 响应按键

每当用户按键时，都将在pygame中注册一个事件。事件都是通过方法pygame.event.get() 获得的。

每次按键都被注册为一个 KEYDOWN 事件。检查到KEYDOWN 事件时， 我们需要检查按下的是否是特定的键。 例如，如果按下的是右箭头键，我们就增大 ship的 rect.centerx 值。

game_function.py

```python
def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx += 1
```

- 读取属性 `event.key` 以检查按下的是否是右箭头 (`pygame.K_RIGHT`)

若现在运行 alien_invasion.py ，则每按右键一次，ship向右移动 1 像素。这并非控制ship的高效方式 。改进控制方式，允许持续移动：



### 持续移动

玩家按住右键不放时，我们希望ship不断地向右移动，直到玩家松开为止。

我们将让游戏检测 pygame.KEYUP 事件 ，以便玩家松开右箭头时我们能够知道。

结合使用 KEYDOWN 和 KEYUP 事件，以及一个名为 moving_right 的标志来实现持续移动。

飞船不动时， 标志 moving_right  = False , 玩家按下右键时 moving_right 置为 True ，玩家松开时 ，该标志重新置为 False 。

飞船的属性都由 Ship 类控制，因此我们将给该类加一个 moving_right 属性 和一个 update() 方法 。update() 方法检查 moving_right 的状态，if 标志为 True ，就调整ship位置 。

ship.py

```python
class Ship():
    
    def __init__(self, screen):
        --snip--
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # 移动标志
        self.moving_right = False
        
    def update(self):
        if self.moving_right:
            self.rect.centerx += 1 
```



game_function.py

```python
def check_events(ship):
    for event in pygame.event.get():
        --snip--
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
```



alien_invasion.py

```python
while True:
    gf.check_events(ship)
    ship.update()
    gf.update_screen(ai_settings, screen, ship)
```



### 左右移动

ship.py

```python
def __init__(self, screen):
    --snip--
    self.moving_right = False
    self.moving_left = False
    
    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
```



game_function.py

```python
def check_event(ship):
    for event in pygame.event.get():
        --snip--
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event,key == pygame.K_LEFT:
                ship.moving_left = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
```

这里之所以可以使用 elif 代码块， 是因为每个事件都只与一个键相关联；如果玩家同时按下了左右箭头键，将检测到两个不同的事件。



## 调整ship的速度

settings.py

```python
class Settings():
    
    def __init__(self):
        
        --snip--
        self.ship_speed_factor = 1.5
```

通过将速度指定为小数，可更细致地控制飞船速度，然而 rect 的centerx 等属性只能存储整数值



ship.py

```python
class Ship():
    
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        --snip--
        
        self.center = float(self.rect.centerx)
        
        def update(self):
            if self.moving_right:
                self.center += self.ai_settings.ship_speed_factor
            if self.moving_left:
                self.center -= self.ai_settings.ship_speed_factor
                
        	#根据 self.center 更新rect对象
            self.rect.centerx = self.center
            
            
        
```



## 限制ship的范围

ship.py

```python
def update(self):
    if self.moving_right and self.rect.right < self.screen_rect.right:
        self.center += self.ai_settings.ship_speed_factor
    if self.moving_left and self.rect.left > 0 :
        self.center -= self.ai_settings.ship_speed_factor
```



# check_events() 重构

```python
def check_keydown_events(event, ship):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
        
def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
        
def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
```



# bullet 类



settings.py

```python
def __init__():
    --snip--
    # 子弹设置
    self.bullet_speed_factor = 1
    self.bullet_width = 3
    self.bullet_height = 15
    self.bullet_color = (60, 60, 60)
```



bullet.py

```python
import pygame
form pygame.sprite import Sprite

class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""
    def __init__(self, ai_settings, screen, ship):
        """在飞船所处的位置创建一个bullet对象"""
        super(Bullet, self).__init__()
        self.screen = screen
        
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bueelt_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
```

- Bullet 类继承了我们从模块 pygame.sprite 中导入的 Sprite 类。通过使用精灵，可将游戏中相关的元素编组，进而同时操作编组中的所有元素。
- `super(Bullet, self).__init__()` 使用了 python 2.7 语法。这种语法也适用于 python3 也可以简写为 `super.__init__()`
- `pygame.Rect()` 从空白开始创建一个矩形。创建该类的实例时，必须提供矩形左上角的 x 和 y 坐标，以及矩形的宽度和高度

bullet.py

```python
def update(self):
    """向上移动子弹"""
    self.y -= self.speed_factor
    self.rect.y = self.y
    
def draw_bullet(self):
    pygame.draw.rect(self.screen, self.color, self.rect)
```



## 将子弹存储到编组中

在 alien_invasion.py 中创建一个编组 (group), 用于存储所有有效的子弹，以便能够管理发射出去的所有子弹。这个编组是`pygame.sprite.Group` 类的一个实例。

alien_invasion.py

```python
import pygame
from pygame.sprite import Group

def run_game():
    --snip--
    
    # 创建一个用于存储子弹的编组
    bullets = Group()
    
    while True:
        gf.check_events(ai_settings, screen, ship, bullets) # 需要在玩家按空格时处理 bullets
        ship.update() # 更新要绘制到屏幕上的bullets
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
        
run_game()
```

- 当你对 编组调用update() 时，编组将自动对其中的每个精灵调用 update() ,因此`bullets.update()` 将为编组bullets 中的每颗子弹调用 `bullet.update()`



## fire

game_functions.py

```python
--snip--
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    --snip--
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹，并将其加入到编组 bullets中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        --snip--
        

def update_screen(ai_settings, screen, ship, bullets):
    --snip--
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    --snip
    
```

- 方法 `bullets.sprites()` 返回一个列表，其中包含编组 bullets中的所有精灵。



## 删除已消失的子弹

当前子弹抵达屏幕顶端后消失，仅仅是因为pygame无法再屏幕外面绘制它们。这些子弹实际上依然存在，它们将继续消耗内存，因此需要删除这些已消失的子弹

检测条件: 表示子弹的rect的bottom属性为 0

alien_invasion.py

```python
while True:
    gf.check_events(ai_settings, screen, ship, bullets)
    ship.update()
    bulelts.update()
    
    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
  
    
    gf.update_screen(ai_settings, screen, ship, bullets)
```

在for循环中，不应从列表或编组中删除条目( for循环按索引递增，删除元素后，其后面的元素前移，而索引又递增一，导致某些元素可能会漏掉) ， 因此必须遍历编组的副本。



## 限制子弹数量

settings.py

```python
self.bullets_allowed = 3
```



game_functions.py

```python
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    --snip--
    elif event.key == pygame.K_SPACE:
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
```



## update_bullets()

可将子弹管理代码移到模块 game_functions 中，以让主程序文件 alien_invasion.py 尽可能简单。

让主循环包含尽可能少的代码，这样只要看见函数名就能迅速知道游戏中发生的情况。主循环检查玩家的输入，然后更新飞船位置和所有未消失的子弹的位置。再使用更新后的位置绘制新屏幕

game_functions.py

```python
def update_bullets(bullets):
    """更新子弹位置，并删除已消失子弹"""
    
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0 :
            bullets.remove(bulelt)
```





# 外星人

开发较大的项目时，进入每个开发阶段前回顾一下开发计划，搞清楚接下来要编写代码来完成哪些任务。

在给项目添加新功能前，还应审核既有代码。每进入一个新阶段，最好对混乱或低效的代码进行清理重构



## 结束游戏快捷键

game_functions.py

```python
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    --snip--
    elif event.key == pygame.K_q:
        sys.exit()
```



## alien 类

alien.py

```python
import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """表示单个外星人的类"""
    
    def __init__(self, ai_settings, screen):
        """初始化外星人并设置其起始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # 加载外星人图像， 并设置其rect属性
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # 每个alien最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # 存储alien的准确位置
        self.x = float(self.rect.x)
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
```



### 创建 alien 实例

alien_invasion.py

```python

def run_game():
    --snip--
    
    alien = Alien(ai_settings, screen)
    
    while True:
        --snip--
        gf.update_screen(ai_settings, screen, ship, alien, bullets)
```



### 创建一群alien

alien_invasion.py

```python
def run_game():
    --snip--
    
    bullets = Group()
    aliens = Group() # 创建一个空编组
    
    gf.create_fleet(ai_settings, screen, aliens)
```



game_functions.py

```python
def udpate_screen(ai_settings, screen, ship, aliens, bullets):
    --snip--
    aliens.draw(screen)
    # pygame 自动绘制编组的每个元素，绘制位置由元素属性rect决定 。
```

```python
from alien import Alien

def create_fleet(ai_settings, screen, aliens):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width ) )
    
    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
```



### 重构 `create_fleet`

gf.py

```python
def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width ) )
    return number_aliens_x

"""创建一个alien并将其放在当前行"""
def create_alien(ai_settings, screen, aliens, alien_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width*alien_number
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(ai_settings, screen, aliens):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    
    # 创建整行alien
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number)
        
```



### 添加更多行

```python
available_space_y = ai_settings.screen_height - 3*alien_height - ship_height
# 减去第一行外星人的上边距，alien与ship距离
number_rows = available_space_y / (2*alien_height)
```



game_functions.py

```python
def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_height_y = ai_settings.screen_height - 3 * alien_height -ship_heiht
    number_rows = int(availabel_height_y /(2*alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    --snip--
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    
    
def create_fleet(ai_settings, screen, ship, aliens):
    --snip--
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
    
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, 
                         row_number)
```



### 让 alien 移动

gf.py

```python
def change_fleet_direction(aliens, settings):
    for alien in aliens.sprites():
        alien.rect.y += settings.alien_drop_speed
    settings.fleet_direction *= -1


def check_fleet_edges(aliens, settings):
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(aliens, settings)
            break


def update_aliens(aliens, settings):
    check_fleet_edges(aliens, settings)
    aliens.update()
```



alien.py

```python
    def update(self):
        self.x += self.settings.alien_speed_factor * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
```





## 射杀外星人



### 检测子弹与外星人的碰撞



方法 `sprite.groupcollide() ` 将每颗子弹的 rect 同每个 alien 的 rect 比较，并返回一个字典，其中包含发生了碰撞的 bullet 和 alien 。

在该字典中，每个键 都是一颗子弹 ，而对应的值是被击中的外星人





**更新 bullet 位置后立即检测碰撞**

game_functions.py

```python
def update_bullets(aliens, bullets):
    --snip--
    
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
# 此行遍历 bullets中的每颗子弹，再遍历编组 aliens中的每个外星人。
# 每当有 bullet 和 alien 的 rect重叠时 ，groupcollide() 就在它返回的字典中添加一个键值对 。

# 两个参数 True 告诉pygame删除发生碰撞的子弹和外星人 。
# 要模拟能够穿行到屏幕顶端的高能子弹 —— 消灭它击中的每个外星人，可将第一个布尔实参设置为 False ，并让第二个 实参为True ，这样被击中的外星人将消失，但所有子弹始终有效，直到抵达屏幕顶端后消失 。
```





## 测试

只通过运行游戏就可以测试其很多功能，但有些功能在正常情况下测试起来比较繁琐 。例如 ，要测试代码能否正确地处理外星人编组为空的情形，需要花很长时间将屏幕上的外星人击落 。



测试有些功能时 ，可以修改游戏的某些设置，以便专注于游戏的特定方面。 例如 ，缩小屏幕以减少需要击落的外星人数量 。



### 生成新的 aliens 群

要在外星人群被消灭后又显示一群外星人 ，首先需要检查编组 aliens 是否为空 。在 update_bullets() 中执行这种这种检查，因为 aliens 都是在此处被消灭的



gf.py

```python
def update_bullets(settings, screen, ship, aliens, bullets):
    --snip--
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(settings, screen, ship, aliens)
```





## 结束游戏



### 检测外星人和飞船碰撞



gf.py

```python
if pygame.sprite.spritecollideany(ship, aliens):
    print("Ship hit!!!")
```

方法 `spritecollideany() ` 接收两个实参 ：一个精灵和一个编组 。

它检查编组是否有成员与精灵发生了碰撞 ，并在找到与精灵发生了碰撞的成员后就停止遍历编组 。

此处，它遍历编组 aliens ，并返回它找到的第一个与飞船发生了碰撞的 alien 

- 有 alien 撞到ship 时 ，需要执行的任务很多 ：需要删除余下的所有 alien 和 bullet ，让ship 重新居中， 以及创建一群新的外星人 。
- 编写上述代码前 ，需要确定检测 alien 和ship 碰撞的方法是否可行 ，为确定这一点 ，最简单的方法是编写一条 print 语句 。会在终端窗口输出。





### 响应外星人和飞船碰撞

确定 alien 与 ship 发生碰撞时需要做什么 ？

我们不销毁 ship 实例并创建一个 新ship实例，而是通过跟踪游戏的统计信息来记录飞船被撞了多少次 。



创建一个用于跟踪游戏统计信息的新类 —— GameStatus , 并保存为 文件 

game_status.py

```python
class GameStatus():
    """跟踪游戏的统计信息"""
    
    def __init__(self, settings):
        """初始化统计信息"""
        self.settings = settings
        self.reset_status()
        
    def reset_status(self):
        """初始化游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit
```

- 游戏运行期间，我们只创建一个 GameStatus 实例，但每当玩家开始新游戏时 ，需要重置一些统计信息 。为此，我们在方法 reset_status 中初始化大部分统计信息 。
