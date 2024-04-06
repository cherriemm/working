# pygame basic



## class Surface



### method blit()

*draw one image onto another*

```python
blit(source, dest, area=None, special_flags=0) -> Rect
```

Draws a source Surface **onto this Surface.** 

- The draw can be positioned with the dest argument

  - **The dest argument** :   

    a pair of coordinates representing the position of the upper left corner of the blit 

    **OR**  a Rect and the upper left corner of the rectangle will be used as the position for the blit

  - The size of the destination rectangle doesn't effect the blit





## module display()

https://www.pygame.org/docs/ref/display.html?highlight=set_mode#pygame.display.set_mode

*pygame module to control the display window and screen*



### method **set_mode**()

*Initialize a window or screen for display*

```python
set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0) -> Surface
```

This function will create a display Surface. The arguments passed in are requests for a display type. The actual created display will be the best possible match supported by the system.

- size argument: a pair of numbers representing the width and height

  - If no size is passed or is set to (0, 0) AND pygame uses SDL version 1.2.10 or above:

    the created Surface will have the same size as the current screen resolution

  - If only the width or height are set to 0 , the Surface will have the same width or height as the screen resolution

- flags: a collection of additional options

  - you can combine multiple types useing the bitwise or operator( "|")

  ```python
  pygame.FULLSCREEN    create a fullscreen display
  pygame.DOUBLEBUF     only applicable with OPENGL
  pygame.HWSURFACE     (obsolete in pygame 2) hardware accelerated, only in FULLSCREEN
  pygame.OPENGL        create an OpenGL-renderable display
  pygame.RESIZABLE     display window should be sizeable
  pygame.NOFRAME       display window will have no border or controls
  pygame.SCALED        resolution depends on desktop size and scale graphics
  pygame.SHOWN         window is opened in visible mode (default)
  pygame.HIDDEN        window is opened in hidden mode
  ```

  

- depth : the number of bits to use for color

  - It is usually best to not pass the depth argument . It will default to the best and fastest color depth for the system.



### method get_surface()

**Get a reference to the currently set display surface, if no display mode has been set this will return None**

```python
get_surface() -> Surface
```



### method flip()

*Update the full display Surface to the screen*

`flip() -> None`

This will update the contents of the entire display.



### method update()

*update portions of the screen for software displays*

`update(rectangle=None) -> None` , `update(rectangle_list) -> None`

This function is like an optimized version of `pygame.display.flip() `  for software displays. It allows only a portion of the screen to be updated, instead of the entire area.

If no argument is passed it updates the entire Surface area like `pygame.display.flip()`



## module sprite 

`pygame.sprite.Sprite` : Simple base class for visible game objects.















# Applications



##  set background image 



1. **load the image**

   ```python
   background = pygame.image.load("path_to_iamge")
   ```

2. **place the image in a specific coordinate of the screen** 

   Note that this should inside  `while` loop for update

   ```python
   screen.blit(image, (x_coordinate, y_coordinate))
   ```

   

example code

```python
import pygame
import sys

SCREENSIZE = (400, 400)

pygame.init()

screen = pygame.display.set_mode(SCREENSIZE)

# Set the caption for the game window
pygame.display.set_caption("My game window")

# Load the image 
background = pygame.image.load("background.png")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        # Draw the background at the top left corner
        screen.blit(image, (0,0))
        
        # Update the display
        pygame.display.update()
```

















# Stars

```python
import pygame
import sys

SCREENSIZE = (400, 600)


def star_cols(screen, star_width):
    col_num = screen.get_rect().width / star_width
    return int(col_num)




def run_game():
    pygame.init()

    screen = pygame.display.set_mode(SCREENSIZE)

    # Set the caption for the game window
    pygame.display.set_caption("My game window")

    # Load the image
    background = pygame.image.load("background.png")
    star = pygame.image.load("star.png")

    star_width = star.get_rect().width
    star_height = star.get_rect().height

    cols = star_cols(screen, star_width)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Draw the background at the top left corner
            screen.blit(background, (0, 0))

            for col in range(0, cols):
                star_x = star_width + col * star_width
                background.blit(star, (star_x, 10))

            # Update the display
            pygame.display.update()


run_game()
```









# 字符雨



## 用到的函数



### chr()

chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回值是当前整数对应的 ASCII 字符。



### random





### pygame.font.**SysFont**()

*create a Font object from the system fonts*

SysFont(name, size, bold=False, italic=False) -> Font



### pygame.Surface 类

- **A pygame Surface is used to represent any image**
- Call pygame.Surface() to create a new image object
- 像素格式可以通过传递位深度或现有的 Surface
- pygame支持三种类型的透明度：
  - colorkeys
  - surface alphas
  - pixel alphas
  - Surface alphas can be mixed with colorkeys, but an image with per pixel alphas cannot use the other modes.


```python
Surface((width, height), flags=0, depth=0, masks=None) -> Surface

Surface((width, height), flags=0, Surface) -> Surface
```



Surface 将被清除为全黑。唯一需要的参数是大小。如果没有其他参数，Surface 将以最匹配的格式创建。



#### **convert**()方法

更改图像的像素格式

```python
convert(Surface=None) -> Surface
convert(depth, flags=0) -> Surface
convert(masks, flags=0) -> Surface
```







```
n:=len(cols)
```





```python
import pygame
import random
# 参数
SCREENSIZE=(600,600)
BLACK=(0,0,0,13)
# 初始化
pygame.init()
font = pygame.font.SysFont('宋体', 20)
screen = pygame.display.set_mode(SCREENSIZE)

surface = pygame.Surface(SCREENSIZE, flags=pygame.SRCALPHA)
pygame.Surface.convert(surface)
surface.fill(BLACK)

# 内容
lib=[chr(i) for i in range(48,48+10)] + [chr(i) for i in range(97,97+26)]   # [0-9 a-z]
texts = [font.render(l, True, (0, 255, 0)) for l in lib]
cols = list(range(40))  # 字体15, 窗口600
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.time.delay(1000)
    screen.blit(surface, (0, 0))
    pygame.time.delay(1000)
    for i in range(n:=len(cols)):
        text = random.choice(texts)
        # 随机闪烁
        x,y=random.randint(0,n-1),random.randint(0,n-1)
        screen.blit(text,(x*15,cols[y]*15))
    pygame.display.flip()

```



要在Pygame中实现闪烁效果，你可以通过调整Surface的透明度或者在不同的时间间隔内交替显示和隐藏Surface来实现。以下是两种方法的示例：

1. **调整透明度：**

```
import pygame
import sys

pygame.init()

# 设置窗口大小和标题
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('闪烁效果')

# 创建Surface
surface = pygame.Surface((width, height))
surface.fill((255, 255, 255))  # 设置Surface的背景颜色为白色

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 清屏
    screen.fill((0, 0, 0))

    # 调整透明度
    alpha = (pygame.time.get_ticks() % 1000) / 1000.0  # 控制透明度的变化，可以根据需求调整
    surface.set_alpha(int(alpha * 255))

    # 将Surface绘制到屏幕上
    screen.blit(surface, (0, 0))

    pygame.display.flip()
    clock.tick(60)
```

1. **交替显示和隐藏：**

```
import pygame
import sys

pygame.init()

# 设置窗口大小和标题
width, height = 400, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('闪烁效果')

# 创建Surface
surface = pygame.Surface((width, height))
surface.fill((255, 255, 255))  # 设置Surface的背景颜色为白色

clock = pygame.time.Clock()

visible = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 清屏
    screen.fill((0, 0, 0))

    # 控制显示和隐藏
    if pygame.time.get_ticks() % 1000 < 500:  # 控制时间间隔，可以根据需求调整
        screen.blit(surface, (0, 0))

    pygame.display.flip()
    clock.tick(60)
```

这两种方法都可以实现简单的闪烁效果，具体取决于你的需求和喜好。希望对你有帮助！





想要实现star随机位置产生，亮度先变亮再变暗，最后删除。