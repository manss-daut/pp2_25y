import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    drawing = False
    start_pos = None

    mode = 'blue'       #tekushchiy tsvet
    tool = 'pen'        #tekushchiy instrument

    points = []         #spisok tochek dlya risovaniya kistyu/lastikom

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held: return
                if event.key == pygame.K_F4 and alt_held: return
                if event.key == pygame.K_ESCAPE: return

                #vybor po knopke
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_q:
                    mode = 'quas'    #kvas
                elif event.key == pygame.K_w:
                    mode = 'wex'     #keks
                elif event.key == pygame.K_e:
                    mode = 'exort'   #eskort

                #mu shmotki(instruments)
                if event.key == pygame.K_1:
                    tool = 'pen'
                elif event.key == pygame.K_2:
                    tool = 'rect'
                elif event.key == pygame.K_3:
                    tool = 'circle'
                elif event.key == pygame.K_d:
                    tool = 'eraser'

            #nazhal myshky
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawing = True
                    start_pos = event.pos
                    if tool in ('pen', 'eraser'):
                        points += [event.pos]
                elif event.button == 3:
                    radius = max(1, radius - 1)  #pravaya knopka umenshaet radius

            # dlya kvadrata i kruga
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if tool == 'rect':
                        end_pos = event.pos
                        color = get_color(mode)
                        pygame.draw.rect(screen, color, pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])), 0)
                    elif tool == 'circle':
                        end_pos = event.pos
                        color = get_color(mode)
                        radius_c = int(((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2)**0.5 / 2)
                        center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                        pygame.draw.circle(screen, color, center, radius_c, 0)

                    drawing = False
                    points = []

            #esli myshka
            elif event.type == pygame.MOUSEMOTION:
                if drawing and tool in ('pen', 'eraser'):
                    position = event.pos
                    points += [position]
                    points = points[-256:]

        #rsiem ili stiraem
        if tool in ('pen', 'eraser'):
            i = 0
            while i < len(points) - 1:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode if tool == 'pen' else 'eraser')
                i += 1

        pygame.display.flip()
        clock.tick(60)

#postepennoe belenie dlya risovaniya
def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'eraser':
        color = (0, 0, 0)
    elif color_mode == 'quas':
        color = (100, 150, 255)
    elif color_mode == 'wex':
        color = (180, 100, 255)
    elif color_mode == 'exort':
        color = (255, 140, 0)
    else:
        color = (255, 255, 255)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    if iterations == 0:
        iterations = 1
    #ot start k end
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        #risuem
        pygame.draw.circle(screen, color, (x, y), width)

#tsvet po mode
def get_color(mode):
    if mode == 'blue':
        return (0, 0, 255)
    elif mode == 'red':
        return (255, 0, 0)
    elif mode == 'green':
        return (0, 255, 0)
    elif mode == 'quas':
        return (100, 150, 255)
    elif mode == 'wex':
        return (180, 100, 255)
    elif mode == 'exort':
        return (255, 140, 0)
    return (255, 255, 255)

main()