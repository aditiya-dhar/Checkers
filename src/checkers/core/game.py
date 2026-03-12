"""
Game.py
The game file holds the game logic and game class.
"""
import pygame
from checkers.ui.music import BackgroundMusic
from checkers.core.constants import RED, WHITE, YELLOW, SQUARE_SIZE, GREY
from checkers.core.board import Main_Board

class Game: 
    """
    The Game class is responsible for managing the game logic, and contains functions to initialize the game, check the turn timeout, display the turn,
    display the piece count, display the player names, update the board, check for a winner, select a piece, move a piece, show available moves, change the turn,
    get the board, and move an AI piece.
    """
    def __init__(self, win, color, player1, player2):
        """
        The init function initializes the Game class with a window, color, player1, and player2, and sets the turn start time and turn timeout. The text color is set to white,
        and the urgent text color is set to red. The screen is set to the window size, and the player names are set to player1 and player2.
        """
        self.turn_start_time = pygame.time.get_ticks()
        self.turn_timeout = 5200  # 5.2 seconds per turn
        self.win = win
        self.color = color
        self.selected = None
        self.board = Main_Board(self.color)
        self.turn = RED
        self.valid_moves = {}
        self.font = pygame.font.Font(None, 36)  # Font for rendering text
        self.text_color = WHITE  # Text color
        self.text_urgent_color = RED  # Text color when time is running out
        self.screen = pygame.display.set_mode((1000, 700))
        self.player1 = player1
        self.player2 = player2
        self.music_button_pressed = False # for music toggle
        self.music_icon = pygame.transform.scale(pygame.image.load('./assets/images/music_icon.png'), (40, 40)) # music icon asset
        
    def check_turn_timeout(self):
        """
        Checks the turn timeout and displays the move timer on the screen.
        If the time is running out, the text color is set to red.
        """

        # position of timer display
        x = 765
        y = 290

        # get remaining time
        elapsed_time = pygame.time.get_ticks() - self.turn_start_time
        remaining_time = max(0, self.turn_timeout - elapsed_time)
        remaining_seconds = remaining_time // 1000 

        # text formatting for timer label and actual time
        label_text = "Timer: "
        label_surface = self.font.render(label_text, True, self.text_color)

        # logic to change color of timer when time is running out
        if remaining_time <= 3000:
            circle_color = RED
        else:
            circle_color = (0, 0, 255)

        # ----- MAKE TIMER CIRCLE ----- #
        # set circl positions for timer
        label_width = label_surface.get_width()
        radius = 30
        cc_x = x + label_width + radius + 5
        cc_y = y + label_surface.get_height() // 2

        # draw circle with time remaining
        self.draw_timer_circle(remaining_seconds, circle_color, cc_x, cc_y)
        # ----------------------------- #

        # Render here
        self.screen.blit(label_surface, (x, y))

        # change turn when time has run out
        if elapsed_time > self.turn_timeout:
            self.change_turn()

    def display_turn(self):
        """
        The display turn function displays the current turn on the screen.
        """
        # position of turn display
        x = 730
        y = 350

        # formats the text and colors
        if self.turn == RED:
            text = f"Current Turn: RED"
            rect_color = RED
            font_color = WHITE
        else:
            text = f"Current Turn: WHITE"
            rect_color = WHITE
            font_color = (0,0,0)
            x = 715
        text_surface = self.font.render(text, True, font_color)

        # draw a background box so the current turn stands out
        self.draw_rect(text_surface, rect_color, x, y)

        # render here
        self.screen.blit(text_surface, (x, y))

    def display_music_toggle(self):
        """
        The display music toggle function displays the music toggle on the screen.
        """
        # check if music playing
        music_playing = pygame.mixer.music.get_busy()

        # position of button
        x = 945
        y = 630

        # position of icon
        x2 = x - 20
        y2 = y - 10

        # position of mouse
        mx, my = pygame.mouse.get_pos()   
        click = pygame.mouse.get_pressed()[0]

        # on hover: toggle formatting of button, on click: toggle music
        if ((mx - x) ** 2 + (my - y) ** 2 <= 40 ** 2):
            pygame.draw.circle(self.screen, GREY, (x, y), 40)

            if click and not self.music_button_pressed:
                self.music_button_pressed = True

                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    music_playing = False
                else:
                    pygame.mixer.music.unpause()
                    music_playing = True
        else:
            pygame.draw.circle(self.screen, WHITE, (x, y), 40)

        if not click:
            self.music_button_pressed = False

        # render icon
        self.screen.blit(self.music_icon, (x2, y2))
        if not music_playing: # indicates toggle
                pygame.draw.polygon(self.screen, (255,0,0), [(x-30,y+30),(x+60-30,y-60+30),(x+69-30,y-59+30),(x+3-30,y+3+30)])

    def display_piece_count(self): 
        """
        The display piece count function displays the piece count on the screen.
        """
        # position of piece count
        x = 715
        y_r = 625
        y_w = 650

        # font size
        font_size = pygame.font.Font(None, 22)

        # text formatting
        text = f"RED Pieces Left: {self.board.red_left}"
        text2 = f"WHITE Pieces Left: {self.board.white_left}"
        text_surface = font_size.render(text, True, self.text_color)
        text_surface2 = font_size.render(text2, True, self.text_color)

        # render here
        self.screen.blit(text_surface, (x, y_r))
        self.screen.blit(text_surface2, (x, y_w))

    def display_player_names(self, player1, player2): 
        """
        The display player names function displays the player names on the screen.
        """
        # position of player display
        x = 715
        y_r = 50
        y_w = 75

        # font size
        font_size = pygame.font.Font(None, 22)

        # text formatting
        text = f"Player 1 (Red): {player1}"
        text2 = f"Player 2 (White): {player2}"
        text_surface = font_size.render(text, True, self.text_color)
        text_surface2 = font_size.render(text2, True, self.text_color)

        # render here
        self.screen.blit(text_surface, (x, y_r))
        self.screen.blit(text_surface2, (x, y_w))

    def update(self): 
        """
        The update function updates the board to show the current board and features.
        """
        self.board.draw(self.win)
        self.show_available_moves(self.valid_moves)
        self.check_turn_timeout()
        self.display_turn()
        self.display_piece_count()
        self.display_player_names(self.player1, self.player2)
        self.display_music_toggle()
        pygame.display.update()
        
    def winner(self): 
        """
        The winner function checks if a winner has been found by calling the board winner function and returns the winner if one has been found.
        """
        return self.board.winner()

    def select(self, row, col): 
        """
        The select function selects a piece and shows the available moves for the piece.
        """
        if self.selected:
            result = self.move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        try:
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.valid_moves = self.board.get_valid_moves(piece)
                return True
        except:
            return None
            
        return False

    def move(self, row, col):
        """
        The move function moves a piece to a given row and column and changes the turn.
        """
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves.get((row, col))
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
            self.turn_start_time = pygame.time.get_ticks()  # Reset the turn timer
            return True

        return False

    def show_available_moves(self, moves): 
        """
        The show available moves function shows the available moves for the selected piece.
        """
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, YELLOW, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self): 
        """
        The change turn function changes the turn to the other player/color and resets the turn timer.
        """
        self.valid_moves = {}
        self.turn_start_time = pygame.time.get_ticks()  # Reset the turn timer
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def get_board(self): 
        """
        The get board function returns the current board.
        """
        return self.board

    def ai_move(self, board): 
        """
        The ai move function moves the AI piece in a player vs computer game.
        """
        self.board = board
        self.change_turn()
    
    def draw_rect(self, text_surface, color, x, y):
        """
        This draws a (given colored) rectangle around an item.
        """
        pad_x, pad_y = 8, 4
        box_x, box_y = x - pad_x, y - pad_y
        box_w = text_surface.get_width() + pad_x * 2
        box_h = text_surface.get_height() + pad_y * 2
        pygame.draw.rect(self.screen, color, (box_x, box_y, box_w, box_h))
    
    def draw_timer_circle(self, timer_num, color, center_x, center_y):
        """
        Draws a filled circle with the given number centered inside.
        """
        circle_radius = 30
        
        # Draw circle
        pygame.draw.circle(self.screen, color, (center_x, center_y), circle_radius)
        
        # get the number of timer seconds remaining
        num_surface = self.font.render(str(timer_num), True, WHITE)
        
        # place number in circle's center
        num_x = center_x - num_surface.get_width() // 2
        num_y = center_y - num_surface.get_height() // 2
        
        # render here
        self.screen.blit(num_surface, (num_x, num_y))