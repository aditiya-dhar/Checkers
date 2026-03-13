"""
SecondMenu.py
The SecondMenu file and class powers the second menu of the game, which allows the user to choose between playing against another player or against the computer.
The class also creates an object of the game class to create the game the users plays.
"""
import pygame
from checkers.core.player import Player
from checkers.core.player import user_scores
from checkers.utils.score_manager import ScoreManager
from checkers.core.constants import RED, SQUARE_SIZE, WHITE
from checkers.core.game import Game
from checkers.core.engine import minimax
from checkers.ui.music import BackgroundMusic
from checkers.utils.shared import background_music


Width, Height = 1000, 700
background_image = pygame.image.load("./assets/images/checkers.jpg")
background_image = pygame.transform.scale(background_image, (Width, Height))
screen = pygame.display.set_mode([Width, Height])
pygame.init()

player1_name = Player("Player 1", 0)
player2_name = Player("Player 2", 0)
score_manager = ScoreManager("./data/user_data.json")
cursor_color = (100, 100, 100) # darker grey
color = (128, 128, 128) # grey

def get_row_col_from_mouse(pos):
    """
    This function gets the row and column of the mouse position. This is necessary for selecting pieces in the class.
    """
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def show_game_over_screen(winner_color, player1, player2, is_vs_computer=False):
    """
    Displays a post-game screen showing the result of the match.
    Shows 'You Won!' in gold or 'Better Luck Next Time!' in red depending on whether player 1 (RED) won.
    Returns when the user clicks 'Back to Menu'.
    """
    go_screen = pygame.display.set_mode([Width, Height])
    clock     = pygame.time.Clock()

    # determine outcome first so font size can depend on it
    player1_won = (winner_color == RED)

    # fonts
    headline_font = pygame.font.Font(None, 110 if player1_won else 72)
    name_font     = pygame.font.Font(None, 48)
    detail_font   = pygame.font.Font(None, 34)
    btn_font      = pygame.font.Font(None, 32)

    # palette
    GOLD       = (220, 180,  40)
    LIGHT_GOLD = (255, 225, 100)
    CRIMSON    = (190,  30,  30)
    LIGHT_RED  = (230,  80,  80)
    SILVER     = (180, 180, 180)
    WHITE_COL  = (255, 255, 255)
    BTN_COLOR  = ( 55,  55,  55)
    BTN_HOVER  = ( 85,  85,  85)
    PANEL_COL  = ( 18,  18,  18)

    winner_name   = player1 if player1_won else ("Computer" if is_vs_computer else player2)
    p2_display    = "Computer" if is_vs_computer else player2
    headline      = "You Won!"               if player1_won else "Better Luck Next Time!"
    headline_col  = GOLD                     if player1_won else CRIMSON
    headline_glow = LIGHT_GOLD               if player1_won else LIGHT_RED
    winner_line   = f"{winner_name} takes the win"
    points_txt    = "+50 pts"                if player1_won else "-50 pts"
    points_col    = GOLD                     if player1_won else CRIMSON

    # back button
    btn_surf = btn_font.render("Back to Menu", True, WHITE_COL)
    btn_rect = btn_surf.get_rect(center=(Width // 2, Height - 65))
    btn_bg   = pygame.Rect(btn_rect.x - 22, btn_rect.y - 10,
                           btn_rect.width + 44, btn_rect.height + 20)

    bg_img = pygame.image.load("./assets/images/checkers.jpg")
    bg_img = pygame.transform.scale(bg_img, (Width, Height))

    while True:
        clock.tick(60)
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if btn_bg.collidepoint(event.pos):
                    return

        # background + dark overlay
        go_screen.blit(bg_img, (0, 0))
        overlay = pygame.Surface((Width, Height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 175))
        go_screen.blit(overlay, (0, 0))

        # center panel
        panel_w, panel_h = 580, 320
        panel = pygame.Surface((panel_w, panel_h), pygame.SRCALPHA)
        panel.fill((*PANEL_COL, 220))
        panel_rect = panel.get_rect(center=(Width // 2, Height // 2 - 15))
        go_screen.blit(panel, panel_rect)
        # colored top bar
        pygame.draw.rect(go_screen, headline_col,
                         pygame.Rect(panel_rect.x, panel_rect.y, panel_w, 5))
        # subtle border
        pygame.draw.rect(go_screen, (50, 50, 50), panel_rect, width=1, border_radius=2)

        # glow layer behind headline
        glow = headline_font.render(headline, True, headline_glow)
        glow.set_alpha(40)
        go_screen.blit(glow, glow.get_rect(center=(Width // 2 + 2, Height // 2 - 118)))

        # headline
        hdr = headline_font.render(headline, True, headline_col)
        go_screen.blit(hdr, hdr.get_rect(center=(Width // 2, Height // 2 - 120)))

        # divider
        pygame.draw.line(go_screen, (60, 60, 60),
                         (panel_rect.x + 30, Height // 2 - 68),
                         (panel_rect.right - 30, Height // 2 - 68), 1)

        # winner name
        w_surf = name_font.render(winner_line, True, WHITE_COL)
        go_screen.blit(w_surf, w_surf.get_rect(center=(Width // 2, Height // 2 - 22)))

        # score change
        pts_surf = detail_font.render(points_txt, True, points_col)
        go_screen.blit(pts_surf, pts_surf.get_rect(center=(Width // 2, Height // 2 + 28)))

        # matchup label
        matchup = detail_font.render(
            f"{player1}  (RED)   vs   {p2_display}  (WHITE)", True, SILVER)
        go_screen.blit(matchup, matchup.get_rect(center=(Width // 2, Height // 2 + 75)))

        # back button
        btn_col = BTN_HOVER if btn_bg.collidepoint(mouse) else BTN_COLOR
        pygame.draw.rect(go_screen, btn_col, btn_bg, border_radius=6)
        go_screen.blit(btn_surf, btn_rect)

        pygame.display.flip()

class SecondMenu:
    """
    The SecondMenu class consists of a String color, which represents the color of the board chosen by the user.
    The class also has three functions, start_game_menu, start_game_vs_player, and start_game_vs_computer.
    """
    
    def __init__(self, track):
        self.selected_music_track = track
        self.background_music = BackgroundMusic([track])
    
    color = RED

    def start_game_menu(self):
        """
        The start game menu function displays the second menu of the game, which allows the user to choose between playing against another player or against the computer.
        """
        global player1_name, player2_name
        start_game_screen = pygame.display.set_mode([Width, Height])

        message = "Select Game Mode"
        credits1 = "Developed by Wander Cerda-Torres, Barry Lin,"
        credits2 = "Nathan McCourt, Jonathan Stanczak, and Geonhee Yu"
        credits_font = pygame.font.Font(None, 25)

        credits_text1 = credits_font.render(credits1, True, (255, 255, 255))
        credits_rect1 = credits_text1.get_rect(center=(Width // 2, 650))
        credits_text2 = credits_font.render(credits2, True, (255, 255, 255))
        credits_rect2 = credits_text2.get_rect(center=(Width // 2, 670))

        background_image = pygame.image.load("./assets/images/checkers.jpg")
        background_image = pygame.transform.scale(background_image, (Width, Height))

        title_font = pygame.font.Font(None, 64)
        title_text = title_font.render(message, True, (255, 255, 255))
        title_rect = title_text.get_rect(center=(Width // 2, 38))

        start_game_screen.blit(background_image, (0, 0))
        start_game_screen.blit(title_text, title_rect)
        start_game_screen.blit(credits_text1, credits_rect1)
        start_game_screen.blit(credits_text2, credits_rect2)

        button_height = 50
        spacing = 10
        color = (128, 128, 128)

        # PvP Button
        position = (Width // 2 - 150, Height // 3 - 25)
        size = (300, 50)
        button_font = pygame.font.Font(None, 32)
        button_text1 = button_font.render("Start Game VS Player", True, (255, 255, 255))
        button_text_rect1 = button_text1.get_rect(center=(Width // 2, Height // 3))
        pygame.draw.rect(start_game_screen, color, pygame.Rect(position, size))
        start_game_screen.blit(button_text1, button_text_rect1)
        button_rect = pygame.Rect(position, size)

        # PvC Button
        position = (Width // 2 - 150, Height // 3 + button_height + spacing)
        size = (300, button_height)
        button_text2 = button_font.render("Start Game VS Computer", True, (255, 255, 255))
        button_text_rect2 = button_text2.get_rect(
            center=(Width // 2, Height // 3 + button_height + spacing + button_height // 2))
        pygame.draw.rect(start_game_screen, color, pygame.Rect(position, size))
        start_game_screen.blit(button_text2, button_text_rect2)
        button_rect_2 = pygame.Rect(position, size)

        # Back Button
        position = (Width // 2 - 150, Height // 3 + 135)
        size = (300, 50)
        button_text3 = button_font.render("Back to Main Menu", True, (255, 255, 255))
        button_text_rect3 = button_text3.get_rect(center=(Width // 2, Height // 3 + 160))
        pygame.draw.rect(start_game_screen, color, pygame.Rect(position, size))
        start_game_screen.blit(button_text3, button_text_rect3)
        button_rect_3 = pygame.Rect(position, size)

        pygame.display.flip()

        while True:
            mouse = pygame.mouse.get_pos()
            if button_rect_3.collidepoint(mouse):
                pygame.draw.rect(start_game_screen, cursor_color, button_rect_3)
                start_game_screen.blit(button_text3, button_text_rect3)
                pygame.display.update()
            elif button_rect_2.collidepoint(mouse):
                pygame.draw.rect(start_game_screen, cursor_color, button_rect_2)
                start_game_screen.blit(button_text2, button_text_rect2)
                pygame.display.update()
            elif button_rect.collidepoint(mouse):
                pygame.draw.rect(start_game_screen, cursor_color, button_rect)
                start_game_screen.blit(button_text1, button_text_rect1)
                pygame.display.update()
            else:
                pygame.display.update()
                pygame.draw.rect(start_game_screen, color, button_rect_3)
                start_game_screen.blit(button_text3, button_text_rect3)
                pygame.draw.rect(start_game_screen, color, button_rect_2)
                start_game_screen.blit(button_text2, button_text_rect2)
                pygame.draw.rect(start_game_screen, color, button_rect)
                start_game_screen.blit(button_text1, button_text_rect1)
                pygame.display.update()

            for event in pygame.event.get():
                score_manager.load_scores()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect_3.collidepoint(event.pos):
                        return
                    elif button_rect.collidepoint(event.pos):
                        player1_name.get_player_name(1)
                        score_manager.add_user(player1_name.username)
                        player2_name.get_player_name(2)
                        score_manager.add_user(player2_name.username)
                        self.start_game_vs_player(start_game_screen)
                        score_manager.save_scores()
                        return
                    elif button_rect_2.collidepoint(event.pos):
                        player1_name.get_player_name(0)
                        score_manager.add_user(player1_name.username)
                        self.start_game_vs_computer(start_game_screen)
                        score_manager.save_scores()
                        return
                    elif event.type == self.background_music.SONG_END:
                        self.background_music.handle_event(event)

    def start_game_vs_player(self, screen):
        """
        The start game vs player function starts the game against another player by creating an object of the game class and passing the screen, color, and player names.
        """
        run = True
        clock = pygame.time.Clock()
        game = Game(screen, self.color, player1_name.username, player2_name.username)
        global score_manager, user_scores

        button_font = pygame.font.Font(None, 32)
        exit_text = button_font.render("Exit Game", True, (255, 255, 255))
        exit_button_rect = exit_text.get_rect(center=(Width // 2 + 350, Height - 100))
        pygame.draw.rect(screen, (128, 128, 128), exit_button_rect)
        screen.blit(exit_text, exit_button_rect)
        pygame.display.flip()

        while run:
            clock.tick(60)
            if game.winner() != None:
                run = False
                winner = game.winner()
                if winner == RED:
                    player1_name.update_win()
                    score_manager.update_scores(player1_name)
                    player2_name.update_loss()
                    score_manager.update_scores(player2_name)
                elif winner == WHITE:
                    player2_name.update_win()
                    score_manager.update_scores(player2_name)
                    player1_name.update_loss()
                    score_manager.update_scores(player1_name)
                show_game_over_screen(winner, player1_name.username, player2_name.username, is_vs_computer=False)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)
                if event.type == background_music.SONG_END:
                    background_music.handle_event(event)

            game.update()

    def start_game_vs_computer(self, screen):
        """
        The start game vs computer function starts the game against the computer by creating an object of the game class and passing the screen, color, and player name.
        """
        run = True
        clock = pygame.time.Clock()
        game = Game(screen, self.color, player1_name.username, "Computer")
        global score_manager, user_scores

        button_font = pygame.font.Font(None, 32)
        exit_text = button_font.render("Exit Game", True, (255, 255, 255))
        exit_button_rect = exit_text.get_rect(center=(Width // 2 + 350, Height - 100))
        pygame.draw.rect(screen, (128, 128, 128), exit_button_rect)
        screen.blit(exit_text, exit_button_rect)
        pygame.display.flip()

        while run:
            clock.tick(60)
            if game.turn == WHITE:
                value, new_board = minimax(game.get_board(), 4, WHITE, game)
                game.ai_move(new_board)

            if game.winner() != None:
                run = False
                winner = game.winner()
                if winner == RED:
                    player1_name.update_win()
                    score_manager.update_scores(player1_name)
                else:
                    player1_name.update_loss()
                    score_manager.update_scores(player1_name)
                show_game_over_screen(winner, player1_name.username, "Computer", is_vs_computer=True)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)
                if event.type == background_music.SONG_END:
                    background_music.handle_event(event)

            game.update()