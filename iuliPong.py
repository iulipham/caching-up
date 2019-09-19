import pygame, sys, time, random
from pygame.locals import *

# Set up pygame.
pygame.init()

# Set up the window.
WINDOWHEIGHT = 700
WINDOWWIDTH = 1100
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Pong')

# Set up the colors.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up direction variables.
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'
DIRECTIONS = [DOWNLEFT, DOWNRIGHT, UPLEFT, UPRIGHT]

BALLMOVESPEED = 5

# Set up the fonts.
basicFont = pygame.font.SysFont(None, 48)

# Draw the background onto the surface.
# windowSurface.fill(BLACK)

# Draw the ball.
RADIUS = 20
ballRect = pygame.draw.circle(windowSurface, WHITE, ((WINDOWWIDTH//2) + RADIUS, (WINDOWHEIGHT//2)), RADIUS)
ball = {'rect': ballRect, 'color': WHITE, 'dir': DOWNLEFT}

# Set up constants for paddles.
SIDEPADDLEHEIGHT = 150
SIDEPADDLEWIDTH = 15
PADDLEMOVESPEED1 = 5
PADDLEMOVESPEED2 = PADDLEMOVESPEED1
P1COLOR = BLUE
P2COLOR = GREEN
TOPPADDLEHEIGHT = SIDEPADDLEWIDTH
TOPPADDLEWIDTH = SIDEPADDLEHEIGHT

# Draw the top and bottom P1paddles.
P1topPaddleX = (WINDOWWIDTH/4)-(TOPPADDLEHEIGHT/2)
P1topPaddleY = 0
paddleRect1T = pygame.Rect(P1topPaddleX, P1topPaddleY, TOPPADDLEWIDTH, TOPPADDLEHEIGHT)
pygame.draw.rect(windowSurface, P1COLOR, paddleRect1T)

P1botPaddleX = P1topPaddleX
P1botPaddleY = WINDOWHEIGHT - TOPPADDLEHEIGHT
paddleRect1B = pygame.Rect(P1botPaddleX, P1botPaddleY, TOPPADDLEWIDTH, TOPPADDLEHEIGHT)
pygame.draw.rect(windowSurface, P1COLOR, paddleRect1B)

# Draw the top and bottom P2paddles.
P2topPaddleX = 3*(WINDOWWIDTH/4)-(TOPPADDLEHEIGHT/2)
P2topPaddleY = 0
paddleRect2T = pygame.Rect(P2topPaddleX, P2topPaddleY, TOPPADDLEWIDTH, TOPPADDLEHEIGHT)
pygame.draw.rect(windowSurface, P2COLOR, paddleRect2T)

P2botPaddleX = P2topPaddleX
P2botPaddleY = WINDOWHEIGHT - TOPPADDLEHEIGHT
paddleRect2B = pygame.Rect(P2botPaddleX, P2botPaddleY, TOPPADDLEWIDTH, TOPPADDLEHEIGHT)
pygame.draw.rect(windowSurface, P2COLOR, paddleRect2B)

# Draw the side paddles.
P1sidePaddleX = 0
P1sidePaddleY = (WINDOWHEIGHT/2)-(SIDEPADDLEHEIGHT/2)
paddleRect1 = pygame.Rect(P1sidePaddleX, P1sidePaddleY, SIDEPADDLEWIDTH, SIDEPADDLEHEIGHT)
pygame.draw.rect(windowSurface, P1COLOR, paddleRect1)

P2sidePaddleX = WINDOWWIDTH-SIDEPADDLEWIDTH
P2sidePaddleY = (WINDOWHEIGHT/2)-(SIDEPADDLEHEIGHT/2)
paddleRect2 = pygame.Rect(P2sidePaddleX, P2sidePaddleY, SIDEPADDLEWIDTH, SIDEPADDLEHEIGHT)
pygame.draw.rect(windowSurface, P2COLOR, paddleRect2)

P1GAMESCORE = 0
P2GAMESCORE = 0
P1MATCHSCORE = 0
P2MATCHSCORE = 0

playAgain = '0'

# Draw the window onto the screen.
pygame.display.update()

# Run the game loop.
while True:
    MOVEDOWN = False
    MOVEUP = False
    MOVELEFT = False
    MOVERIGHT = False
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    windowSurface.fill(BLACK)

    # Move the ball.
    if ball['dir'] == DOWNLEFT:
        ball['rect'].left -= BALLMOVESPEED
        ball['rect'].top += BALLMOVESPEED
    if ball['dir'] == DOWNRIGHT:
        ball['rect'].left += BALLMOVESPEED
        ball['rect'].top += BALLMOVESPEED
    if ball['dir'] == UPLEFT:
        ball['rect'].left -= BALLMOVESPEED
        ball['rect'].top -= BALLMOVESPEED
    if ball['dir'] == UPRIGHT:
        ball['rect'].left += BALLMOVESPEED
        ball['rect'].top -= BALLMOVESPEED

    # Check whether the box has missed the paddles and gone out of the top or bottom sides.
    if ball['rect'].bottom < 0:
        # The box has moved past the top.
        if ball['rect'].right < WINDOWWIDTH/2:
            P1GAMESCORE += 1
        else:
            P2GAMESCORE += 1
        # Respawn ball at random velocity (speed and angle).
        ballRect = pygame.draw.circle(windowSurface, WHITE, ((WINDOWWIDTH // 2) + RADIUS, (WINDOWHEIGHT // 2)), RADIUS)
        ball = {'rect': ballRect, 'color': WHITE, 'dir': DIRECTIONS[random.randint(0, (len(DIRECTIONS) - 1))]}
        BALLMOVESPEED = random.randint(4,15)

    if ball['rect'].top > WINDOWHEIGHT:
        # The box has moved past the bottom.
        if ball['rect'].right < WINDOWWIDTH/2:
            P1GAMESCORE += 1
        else:
            P2GAMESCORE += 1
        # Respawn ball at random velocity (speed and angle).
        ballRect = pygame.draw.circle(windowSurface, WHITE, ((WINDOWWIDTH // 2) + RADIUS, (WINDOWHEIGHT // 2)), RADIUS)
        ball = {'rect': ballRect, 'color': WHITE, 'dir': DIRECTIONS[random.randint(0, (len(DIRECTIONS) - 1))]}
        BALLMOVESPEED = random.randint(4, 15)

    # Check if ball has missed paddles and gone off the sides.
    if ball['rect'].right < 0:
        # The ball has moved past the left side.
        P1GAMESCORE += 1
        # Respawn ball at random velocity (speed and angle).
        ballRect = pygame.draw.circle(windowSurface, WHITE, ((WINDOWWIDTH // 2) + RADIUS, (WINDOWHEIGHT // 2)), RADIUS)
        ball = {'rect': ballRect, 'color': WHITE, 'dir': DIRECTIONS[random.randint(0, (len(DIRECTIONS) - 1))]}
        BALLMOVESPEED = random.randint(4,15)
    elif ball['rect'].left > WINDOWWIDTH:
        # The ball has moved past the right side.
        P2GAMESCORE += 1
        # Respawn ball at random velocity (speed and angle).
        ballRect = pygame.draw.circle(windowSurface, WHITE, ((WINDOWWIDTH // 2) + RADIUS, (WINDOWHEIGHT // 2)), RADIUS)
        ball = {'rect': ballRect, 'color': WHITE, 'dir': DIRECTIONS[random.randint(0, (len(DIRECTIONS) - 1))]}
        BALLMOVESPEED = random.randint(4,15)
    else:
        # Update circle to screen after moving.
        pygame.draw.circle(windowSurface, ball['color'], (ball['rect'].left, ball['rect'].top), RADIUS, 0)

    # Up and down arrow move P1 paddle.
    if event.type == KEYDOWN:
        if event.key == K_DOWN:
            MOVEDOWN = True
            MOVEUP = False
        if event.key == K_UP:
            MOVEDOWN = False
            MOVEUP = True
        if event.key == K_LEFT:
            MOVELEFT = True
            MOVERIGHT = False
        if event.key == K_RIGHT:
            MOVELEFT = False
            MOVERIGHT = True
    if event.type == KEYUP:
        if event.key == K_DOWN:
            MOVEDOWN = False
        if event.key == K_UP:
            MOVEUP = False
        if event.key == K_LEFT:
            MOVELEFT = False
        if event.key == K_RIGHT:
            MOVERIGHT = False

    # Move the P1 side paddle.
    if MOVEDOWN and paddleRect1.bottom + PADDLEMOVESPEED1 < WINDOWHEIGHT:
        paddleRect1.top += PADDLEMOVESPEED1
        P1sidePaddleY += PADDLEMOVESPEED1
    if MOVEUP and paddleRect1.top > PADDLEMOVESPEED1:
        paddleRect1.top -= PADDLEMOVESPEED1
        P1sidePaddleY -= PADDLEMOVESPEED1

    # Move the P1 top paddle.
    if MOVERIGHT and paddleRect1T.right + PADDLEMOVESPEED1 < (WINDOWWIDTH/2):
        paddleRect1T.right += PADDLEMOVESPEED1
        P1topPaddleX += PADDLEMOVESPEED1
    if MOVELEFT and paddleRect1T.left > PADDLEMOVESPEED1:
        paddleRect1T.left -= PADDLEMOVESPEED1
        P1topPaddleX -= PADDLEMOVESPEED1

    # Move the P1 bottom paddle.
    if MOVERIGHT and paddleRect1B.right + PADDLEMOVESPEED1 < (WINDOWWIDTH/2):
        paddleRect1B.right += PADDLEMOVESPEED1
        P1botPaddleX += PADDLEMOVESPEED1
    if MOVELEFT and paddleRect1B.left > PADDLEMOVESPEED1:
        paddleRect1B.left -= PADDLEMOVESPEED1
        P1botPaddleX -= PADDLEMOVESPEED1

    # Check if ball has hit P1 side paddle from the bottom.
    if (paddleRect1.top <= ballRect.bottom) & ballRect.collidepoint((paddleRect1.right + 15, paddleRect1.bottom + 15)):
        if ball['dir'] == UPLEFT:
            ball['dir'] = DOWNRIGHT
    # Check if ball has hit P1 side paddle from the top.
    elif (paddleRect1.top <= ballRect.bottom - 15) & ballRect.collidepoint(paddleRect1.topright):
        if ball['dir'] == DOWNLEFT:
            ball['dir'] = UPRIGHT
    # Check if ball has hit P1 side paddle from the front.
    elif (paddleRect1.right - 5 >= ballRect.left - RADIUS) \
            & ((ballRect.bottom > paddleRect1.top) & (ballRect.top < paddleRect1.bottom)):
        if ball['dir'] == DOWNLEFT:
            ball['dir'] = DOWNRIGHT
        elif ball['dir'] == DOWNRIGHT:
            ball['dir'] = DOWNLEFT
        elif ball['dir'] == UPLEFT:
            ball['dir'] = UPRIGHT
        else:
            ball['dir'] = UPLEFT

    # Check if ball has hit P1 top paddle from the left.
    if (paddleRect1T.left <= ballRect.right) & ballRect.collidepoint(
            (paddleRect1T.left - 15, paddleRect1T.bottom + RADIUS)):
        if ball['dir'] == UPRIGHT:
            ball['dir'] = DOWNLEFT
    # Check if ball has hit P1 top paddle from the right.
    elif (paddleRect1T.right >= ballRect.left) & ballRect.collidepoint(paddleRect1T.bottomright):
        if ball['dir'] == UPLEFT:
            ball['dir'] = DOWNRIGHT
    # Check if ball has hit P1 top paddle from the bottom.
    elif (paddleRect1T.bottom + TOPPADDLEHEIGHT >= ballRect.top) \
            & ((ballRect.right > paddleRect1T.left) & (ballRect.left < paddleRect1T.right)):
        if ball['dir'] == UPLEFT:
            ball['dir'] = DOWNLEFT
        elif ball['dir'] == UPRIGHT:
            ball['dir'] = DOWNRIGHT

    # Check if ball has hit P1 bottom paddle from the left.
    if (paddleRect1B.left <= ballRect.right) & ballRect.collidepoint(
            (paddleRect1B.left, paddleRect1B.top)):
        if ball['dir'] == DOWNRIGHT:
            ball['dir'] = UPLEFT
    # Check if ball has hit P1 bottom paddle from the right.
    elif (paddleRect1B.right >= ballRect.left) & ballRect.collidepoint(paddleRect1B.top - 30, paddleRect1B.right):
        if ball['dir'] == DOWNLEFT:
            ball['dir'] = UPRIGHT
    # Check if ball has hit P1 bottom paddle from the top.
    elif (paddleRect1B.top - 10 <= ballRect.bottom - 22) \
            & ((ballRect.right > paddleRect1B.left) & (ballRect.left < paddleRect1B.right)):
        if ball['dir'] == DOWNLEFT:
            ball['dir'] = UPLEFT
        elif ball['dir'] == DOWNRIGHT:
            ball['dir'] = UPRIGHT

    # Move the P2 side paddle.
    # Move down.
    if (paddleRect2.bottom + PADDLEMOVESPEED2 < WINDOWHEIGHT) & (ball['dir'] == DOWNRIGHT):
        paddleRect2.top += PADDLEMOVESPEED2
        P2sidePaddleY += PADDLEMOVESPEED2
    # Move up.
    if (paddleRect2.top > PADDLEMOVESPEED2) & (ball['dir'] == UPRIGHT):
        paddleRect2.top -= PADDLEMOVESPEED2
        P2sidePaddleY -= PADDLEMOVESPEED2

    # Move the P2 top paddle.
    # Move left.
    if (paddleRect2T.right + PADDLEMOVESPEED2 < WINDOWWIDTH) \
            & ((ball['dir'] == UPRIGHT) | (ball['dir'] == DOWNRIGHT)) \
            & (ball['rect'].left > WINDOWWIDTH/2) & (ball['rect'].right < paddleRect2T.left):
        paddleRect2T.right -= PADDLEMOVESPEED2
        P2topPaddleX -= PADDLEMOVESPEED2
        paddleRect2B.right -= PADDLEMOVESPEED2
        P2botPaddleX -= PADDLEMOVESPEED2
    # Move right.
    if (paddleRect2T.right + PADDLEMOVESPEED2 < WINDOWWIDTH) \
            & ((ball['dir'] == UPRIGHT) | (ball['dir'] == DOWNRIGHT)) \
            & (ball['rect'].left > WINDOWWIDTH/2) & (ball['rect'].left > paddleRect2T.right):
        paddleRect2T.left += PADDLEMOVESPEED2
        P2topPaddleX += PADDLEMOVESPEED2
        paddleRect2B.right += PADDLEMOVESPEED2
        P2botPaddleX += PADDLEMOVESPEED2

    # Detect paddle collision for paddleP2.
    # Check if ball has hit side paddleP2 from the bottom.
    if (paddleRect2.top <= ballRect.bottom) & ballRect.collidepoint((paddleRect2.left, paddleRect2.bottom + 15)):
        if ball['dir'] == UPRIGHT:
            ball['dir'] = DOWNLEFT
    # Check if ball has hit a side paddleP2 from the top.
    elif (paddleRect2.top <= ballRect.bottom) & ballRect.collidepoint(paddleRect2.left + RADIUS, paddleRect2.top):
        if ball['dir'] == DOWNRIGHT:
            ball['dir'] = UPLEFT
    # Check if ball has hit a side paddleP2 from the front.
    elif (paddleRect2.left <= ballRect.right - 25) \
            & ((ballRect.bottom > paddleRect2.top) & (ballRect.top < paddleRect2.bottom)):
        if ball['dir'] == DOWNLEFT:
            ball['dir'] = DOWNRIGHT
        elif ball['dir'] == DOWNRIGHT:
            ball['dir'] = DOWNLEFT
        elif ball['dir'] == UPLEFT:
            ball['dir'] = UPRIGHT
        else:
            ball['dir'] = UPLEFT

    # Check if ball has hit P2 top paddle from the left.
    if (paddleRect2T.left <= ballRect.right) & ballRect.collidepoint(
            (paddleRect2T.left - 15, paddleRect2T.bottom + RADIUS)):
        if ball['dir'] == DOWNRIGHT:
            ball['dir'] = UPLEFT
    # Check if ball has hit P2 top paddle from the right.
    elif (paddleRect2T.right >= ballRect.left) \
            & ballRect.collidepoint((paddleRect2T.right + 15, paddleRect2T.bottom + RADIUS)):
        if ball['dir'] == DOWNLEFT:
            ball['dir'] = UPRIGHT
    # Check if ball has hit P2 top paddle from the bottom.
    elif (paddleRect2T.bottom + TOPPADDLEHEIGHT >= ballRect.top) \
            & ((ballRect.right > paddleRect2T.left) & (ballRect.left < paddleRect2T.right)):
        if ball['dir'] == UPLEFT:
            ball['dir'] = DOWNLEFT
        elif ball['dir'] == UPRIGHT:
            ball['dir'] = DOWNRIGHT

    # Check if ball has hit P2 bottom paddle from the left.
    if (paddleRect2B.left <= ballRect.right) & ballRect.collidepoint(
            (paddleRect2B.left - 15, paddleRect2B.top)):
        if ball['dir'] == DOWNRIGHT:
            ball['dir'] = UPLEFT
    # Check if ball has hit P1 bottom paddle from the right.
    elif (paddleRect2B.right >= ballRect.left) & ballRect.collidepoint(paddleRect2B.top - 30, paddleRect2B.right):
        if ball['dir'] == DOWNLEFT:
            ball['dir'] = UPRIGHT
    # Check if ball has hit P1 bottom paddle from the top.
    elif (paddleRect2B.top - 10 <= ballRect.bottom - 22) \
            & ((ballRect.right > paddleRect2B.left) & (ballRect.left < paddleRect2B.right)):
        if ball['dir'] == DOWNLEFT:
            ball['dir'] = UPLEFT
        elif ball['dir'] == DOWNRIGHT:
            ball['dir'] = UPRIGHT

    # Update the score. Respawn ball at random velocity (speed and angle).
    # Set up the text for Game Score.
    scoreString = "Game P1: {}/11    P2: {}/11".format(P1GAMESCORE, P2GAMESCORE)
    gameScoreText = basicFont.render(scoreString, True, WHITE)
    gameScoreTextRect = gameScoreText.get_rect()
    gameScoreTextRect.center = ((WINDOWWIDTH/2), 100)
    windowSurface.blit(gameScoreText, gameScoreTextRect)
    pygame.display.update(gameScoreTextRect)

    # Check if the game has been won.
    if (P1GAMESCORE >= 11) & (P1GAMESCORE - 2 >= P2GAMESCORE):
        P1MATCHSCORE += 1
        # Set up the text for Game Winner.
        winnerString = "P1 Won the Game! Play Again?"
        winnerText = basicFont.render(winnerString, True, WHITE)
        winnerTextRect = winnerText.get_rect()
        winnerTextRect.center = ((WINDOWWIDTH / 2), 150)
        windowSurface.blit(winnerText, winnerTextRect)
        pygame.display.update(winnerTextRect)
        playAgain = input('Player 1 Won. Play again? (Y or N)').lower()
    if (P2GAMESCORE >= 11) & (P2GAMESCORE - 2 >= P1GAMESCORE):
        P2MATCHSCORE += 1
        # Set up the text for Game Winner.
        winnerString = "P2 Won the Game! Play Again?"
        winnerText = basicFont.render(winnerString, True, WHITE)
        winnerTextRect = winnerText.get_rect()
        winnerTextRect.center = ((WINDOWWIDTH / 2), 150)
        windowSurface.blit(winnerText, winnerTextRect)
        pygame.display.update(winnerTextRect)
        playAgain = input('Player 2 Won. Play again? (Y or N)').lower()

    # Set up the text for Match Score.
    scoreString = "Match P1: {}/5    P2: {}/5".format(P1MATCHSCORE, P2MATCHSCORE)
    matchScoreText = basicFont.render(scoreString, True, WHITE)
    matchTextRect = matchScoreText.get_rect()
    matchTextRect.center = ((WINDOWWIDTH/2), 50)
    windowSurface.blit(matchScoreText, matchTextRect)

    # Check if match has been won.
    if (P1MATCHSCORE >= 3):
        print('Player 1 has won the match.')

    if (P2MATCHSCORE >= 3):
        print('Player 2 has won the match.')

    # Update paddles to screen after moving.
    pygame.draw.rect(windowSurface, P1COLOR, paddleRect1)
    pygame.draw.rect(windowSurface, P2COLOR, paddleRect2)
    pygame.draw.rect(windowSurface, P1COLOR, paddleRect1T)
    pygame.draw.rect(windowSurface, P1COLOR, paddleRect1B)
    pygame.draw.rect(windowSurface, P2COLOR, paddleRect2T)
    pygame.draw.rect(windowSurface, P2COLOR, paddleRect2B)

    pygame.display.update()

    while P1GAMESCORE == 11 | P2GAMESCORE == 11:
        if playAgain == 'y':
            # Respawn ball at random velocity.
            ballRect = pygame.draw.circle(windowSurface, WHITE, ((WINDOWWIDTH // 2) + RADIUS, (WINDOWHEIGHT // 2)), RADIUS)
            ball = {'rect': ballRect, 'color': WHITE, 'dir': DOWNLEFT}
            BALLMOVESPEED = 20
            P1GAMESCORE = 0
            P2GAMESCORE = 0
        if playAgain == 'n':
            pygame.quit()
            sys.exit()

    time.sleep(0.02)
