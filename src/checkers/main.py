"""
Main.py
The main file holds menu operations for the game including sound, settings, leaderboard, tutorial, and board customization.

"""
from checkers.utils.reddit_manager import RedditManager
from checkers.types.reddit import RedditResponse
import pygame
from checkers.ui.second_menu import SecondMenu
from checkers.core.constants import BLUE, YELLOW, RED, GREEN
from checkers.utils.score_manager import ScoreManager
from checkers.ui.second_menu import SecondMenu

pygame.init()
pygame.mixer.init() # initialize pygame mixer for music

# set up the drawing window
Width, Height = 1000, 700 # updated size
screen = pygame.display.set_mode([Width, Height])
#title of the game for screen 
pygame.display.set_caption("Checkers+")

# background music
tracks = ["./assets/music/Track1.mp3", "./assets/music/Track2.mp3", "./assets/music/Track3.mp3", "./assets/music/Track4.mp3", "./assets/music/Track5.mp3", "./assets/music/Track6.mp3", "./assets/music/Track7.mp3", "./assets/music/Track8.mp3"] # can add more or delete tracks if we do not like them
current_track = 0
SONG_END = pygame.USEREVENT + 1
second_menu = SecondMenu(tracks)


def music_loop():
    """
    The music loop function loops through the music tracks in the tracks list.
    """
    global current_track
    pygame.mixer.music.load(tracks[current_track])
    pygame.mixer.music.set_volume(0.1) # 0.1-1.0
    pygame.mixer.music.play()
    current_track = (current_track + 1) % len(tracks)

music_loop()
pygame.mixer.music.set_endevent(SONG_END) # create event for song ending/looping

# title for display
game_title = "Checkers+"
message = "Checkers with a twist! For all ages and skill levels!"
credits1 = "Developed by Wander Cerda-Torres, Barry Lin,"
credits2 = "Nathan McCourt, Jonathan Stanczak, and Geonhee Yu"
background_image = pygame.image.load("./assets/images/checkers.jpg")
background_image = pygame.transform.scale(background_image, (Width, Height))  
title_font = pygame.font.Font(None, 64)
message_font = pygame.font.Font(None, 32)
credits_font = pygame.font.Font(None, 25)

# Title text
title_text = title_font.render(game_title, True, (255, 255, 255))
title_rect = title_text.get_rect(center=(Width // 2, 22))
# Under title text
message_text = message_font.render(message, True, (255, 255, 255))
message_rect = message_text.get_rect(center=(Width // 2, 55))
# Credits text
credits_text1 = credits_font.render(credits1, True, (255, 255, 255))
credits_rect1 = credits_text1.get_rect(center=(Width // 2, 650))
credits_text2 = credits_font.render(credits2, True, (255, 255, 255))
credits_rect2 = credits_text2.get_rect(center=(Width // 2, 670))

second_menu_instance = SecondMenu(tracks)
def main():
    """
    The main function is the main menu of the game. It displays the title, message, and credits, and holds user interaction with buttons. 
    If a user hovers over a button, the button will change color to indicate that it has been clicked. If the user clicks on a button,
    the corresponding function will be called.
    """
    running = True

    reddit_manager = RedditManager(r"./data/r_slash_temple.json")
    reddit_posts = reddit_manager.get_data();

    print(reddit_posts.data.children[0].data.title) # title of 1st post
    print(reddit_posts.data.children[0].data.selftext) # Text of 1st post

    buttons = menu_buttons()
    
    while running:
        # did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttons[0].collidepoint(event.pos): # If Start Game button is clicked, show the second menu
                   second_menu_instance.start_game_menu()
                if buttons[2].collidepoint(event.pos): # if mouse is clicked on tutorial button
                    tutorial()
                elif buttons[1].collidepoint(event.pos): # if mouse is clicked on settings button
                    settings()
                elif buttons[4].collidepoint(event.pos): # if mouse is clicked on leaderboard button (not yet implemented)
                    board_customization()
                # Check if the current song has finished, loop to next song
            elif event.type == SONG_END:
                music_loop()

        #image of the background
        screen.blit(background_image, (0, 0))
        # display title information and credits
        screen.blit(title_text, title_rect)
        screen.blit(message_text, message_rect)
        screen.blit(credits_text1, credits_rect1)
        screen.blit(credits_text2, credits_rect2)
        
        menu_buttons()
        pygame.display.flip()

    # done! time to quit
    pygame.quit()

def menu_buttons():
    """
    The menu buttons function creates the buttons on the main menu. It returns the button rectangles for each button so that they can be used in the main function.
    """
    # Used for buttons w/ images
    icon_size = (45, 45)  # Adjust the size of the icon as needed
    button_height = 50
    spacing = 10

    # Start Game Button
    startgame_icon = pygame.image.load('./assets/images/start_icon.png')
    # Draw the icon next to the text with the specified size
    startgame_icon_resized = pygame.transform.scale(startgame_icon, icon_size)
    startgame_icon_rect = startgame_icon_resized.get_rect(topleft=(Width // 2 - 150 + 10, Height // 3 + (button_height - icon_size[1] - 50) // 2))

    color = (128, 128, 128) # grey
    cursor_color = (100, 100, 100) # darker grey
    position = (Width // 2 - 150, Height // 3-25)
    size = (300, 50)  # width, height
        
    button_font = pygame.font.Font(None, 32)
    button_text = button_font.render("Start Game", True, (255, 255, 255)) # Button text and color
    button_text_rect = button_text.get_rect(center=(Width // 2, Height // 3))
    
    # Create button on screen using position and size parameters
    pygame.draw.rect(screen, color, pygame.Rect(position, size))
    screen.blit(startgame_icon_resized, startgame_icon_rect.topleft)
    screen.blit(button_text, button_text_rect)
    
    # Used to indicate if cursor is hovering over button. If so, button will be darker
    mouse = pygame.mouse.get_pos()
    button_rect = pygame.Rect(position, size)
    if button_rect.collidepoint(mouse):
        pygame.draw.rect(screen, cursor_color, button_rect)  # Change color when cursor hovered over
    else:
        pygame.draw.rect(screen, color, button_rect) # stay original color if cursor not hovering over

    screen.blit(button_text, button_text_rect)
    screen.blit(startgame_icon_resized, startgame_icon_rect.topleft)  # Draw the icon after drawing the button

    # Settings Button    
    settings_icon = pygame.image.load('./assets/images/settings_icon.png')

    position = (Width // 2 - 150, Height // 3 + button_height + spacing)
    size = (300, button_height)  # width, height

    button_text = button_font.render("Settings", True, (255, 255, 255))  # Button text and color
    button_text_rect = button_text.get_rect(center=(Width // 2, Height // 3 + button_height + spacing + button_height // 2))

    # Draw the icon next to the text with the specified size
    settings_icon_resized = pygame.transform.scale(settings_icon, icon_size)
    settings_icon_rect = settings_icon_resized.get_rect(topleft=(Width // 2 - 150 + 10, Height // 3 + button_height + spacing + (button_height - icon_size[1]) // 2))

    # Create button on screen using position and size parameters
    pygame.draw.rect(screen, color, pygame.Rect(position, size))
    screen.blit(settings_icon_resized, settings_icon_rect.topleft)  # Draw the icon after drawing the button
    screen.blit(button_text, button_text_rect)

    # Used to indicate if the cursor is hovering over the button. If so, the button will be darker
    mouse = pygame.mouse.get_pos()
    button_rect_2 = pygame.Rect(position, size)
    if button_rect_2.collidepoint(mouse):
        pygame.draw.rect(screen, cursor_color, button_rect_2)  # Change color when cursor hovered over
    else:
        pygame.draw.rect(screen, color, button_rect_2)  # Stay the original color if the cursor is not hovering over

    screen.blit(settings_icon_resized, settings_icon_rect.topleft)  # Draw the icon after drawing the button
    screen.blit(button_text, button_text_rect)

    # Tutorial button
    tutorial_icon = pygame.image.load('./assets/images/tutorial_icon.png')

    color = (128, 128, 128) # grey
    cursor_color = (100, 100, 100) # darker grey
    position = (Width // 2 - 150, Height // 3 + 135)
    size = (300, 50)  # width, height

    button_font = pygame.font.Font(None, 32)
    button_text = button_font.render("Tutorial", True, (255, 255, 255)) # Button text and color
    button_text_rect = button_text.get_rect(center=(Width // 2, Height // 3+160))
    pygame.draw.rect(screen, color, pygame.Rect(position, size))
    screen.blit(button_text, button_text_rect)

    # Draw the icon next to the text with the specified size
    tutorial_icon_resized = pygame.transform.scale(tutorial_icon, icon_size)
    tutorial_icon_rect = tutorial_icon_resized.get_rect(topleft=(Width // 2 - 150 + 10, Height // 3 + 135 + (button_height - icon_size[1]) // 2))

    pygame.draw.rect(screen, color, pygame.Rect(position, size))
    screen.blit(button_text, button_text_rect)
    
    # Used to indicate if cursor is hovering over button. If so, button will be darker
    mouse = pygame.mouse.get_pos()
    button_rect_3 = pygame.Rect(position, size)
    if button_rect_3.collidepoint(mouse):
        pygame.draw.rect(screen, cursor_color, button_rect_3)  # Change color when cursor hovered over
    else:
        pygame.draw.rect(screen, color, button_rect_3) # stay original color if cursor not hovering over

    screen.blit(tutorial_icon_resized, tutorial_icon_rect.topleft)  # Draw the icon after drawing the button
    screen.blit(button_text, button_text_rect)
    
    # Leaderboard button
    leaderboard_icon = pygame.image.load('./assets/images/leaderboard_icon.png')

    color = (128, 128, 128) # grey
    cursor_color = (100, 100, 100) # darker grey
    position = (Width // 2 - 150, Height // 3 + 210)  # Adjust the vertical position as needed
    size = (300, 50)  # width, height

    button_font = pygame.font.Font(None, 32)
    button_text = button_font.render("View Rankings", True, (255, 255, 255)) # Button text and color
    button_text_rect = button_text.get_rect(center=(Width // 2, Height // 3 + 235))  # Adjust the vertical position as needed
    pygame.draw.rect(screen, color, pygame.Rect(position, size))
    screen.blit(button_text, button_text_rect)

    # Draw the icon next to the text with the specified size
    leaderboard_icon_resized = pygame.transform.scale(leaderboard_icon, icon_size)
    leaderboard_icon_rect = leaderboard_icon_resized.get_rect(
    topleft=(Width // 2 - 150 + 10, Height // 3 + 210 + (button_height - icon_size[1]) // 2))

    pygame.draw.rect(screen, color, pygame.Rect(position, size))
    screen.blit(button_text, button_text_rect)
    
    # Used to indicate if cursor is hovering over button. If so, button will be darker
    mouse = pygame.mouse.get_pos()
    button_rect_4 = pygame.Rect(position, size)
    if button_rect_4.collidepoint(mouse):
        pygame.draw.rect(screen, cursor_color, button_rect_4)  # Change color when cursor hovered over
        if pygame.mouse.get_pressed()[0]:  # Check if left mouse button is clicked
            show_leaderboard()  # Call the function to display the leaderboard
    else:
        pygame.draw.rect(screen, color, button_rect_4) # stay original color if cursor not hovering over

    screen.blit(leaderboard_icon_resized, leaderboard_icon_rect.topleft)  # Draw the icon after drawing the button
    screen.blit(button_text, button_text_rect)

    # Customize Board button
    board_icon = pygame.image.load('./assets/images/colorwheel_icon.png')

    color = (128, 128, 128) # grey
    cursor_color = (100, 100, 100) # darker grey
    position = (Width // 2 - 150, Height // 3 + 285)  # Adjust the vertical position as needed
    size = (300, 50)  # width, height

    button_font = pygame.font.Font(None, 32)
    button_text = button_font.render("Customize Board", True, (255, 255, 255)) # Button text and color
    button_text_rect = button_text.get_rect(center=(Width // 2, Height // 3 + 310))  # Adjust the vertical position as needed
    pygame.draw.rect(screen, color, pygame.Rect(position, size))
    screen.blit(button_text, button_text_rect)

    # Draw the icon next to the text with the specified size
    board_icon_resized = pygame.transform.scale(board_icon, icon_size)
    board_icon_rect = board_icon_resized.get_rect(topleft=(Width // 2 - 150 + 10, Height // 3 + 285 + (button_height - icon_size[1]) // 2))

    pygame.draw.rect(screen, color, pygame.Rect(position, size))
    screen.blit(button_text, button_text_rect)
    
    # Used to indicate if cursor is hovering over button. If so, button will be darker
    mouse = pygame.mouse.get_pos()
    button_rect_5 = pygame.Rect(position, size)
    if button_rect_5.collidepoint(mouse):
        pygame.draw.rect(screen, cursor_color, button_rect_5)  # Change color when cursor hovered over
    else:
        pygame.draw.rect(screen, color, button_rect_5) # stay original color if cursor not hovering over

    screen.blit(board_icon_resized, board_icon_rect.topleft)  # Draw the icon after drawing the button
    screen.blit(button_text, button_text_rect)

    return button_rect, button_rect_2, button_rect_3, button_rect_4, button_rect_5

def tutorial(): 
    """
    The tutorial function displays the tutorial screen. It displays the tutorial text and image, and allows the user to exit the tutorial after clicking the exit button.
    The tutorial informs the user on how to use the application and what features are available to them.
    """
    
    # load image used in tutorial
    checkers_icon = pygame.image.load('./assets/images/checkersguy_icon.png')
    tutorial_screen = pygame.display.set_mode([Width, Height])
    tutorial_screen.fill((128, 128, 128))

    # First message
    tutorial_font = pygame.font.Font(None, 64)
    tutorial_text = tutorial_font.render("Welcome to Checkers+!", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 50))
    tutorial_screen.blit(tutorial_text, tutorial_rect)

    # Second message
    tutorial_font = pygame.font.Font(None, 32)
    tutorial_text = tutorial_font.render("This tutorial should provide you with instructions on how to play and use Checkers+.", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 105))
    tutorial_screen.blit(tutorial_text, tutorial_rect)

    # First paragraph
    tutorial_font = pygame.font.Font(None, 25)
    tutorial_text = tutorial_font.render("There are many features accessible from the Checkers+ menu. You can start a player versus player game, a player", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 145))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("versus computer game, and access features like the settings, leaderboard, board customization, and this tutorial!", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 170))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("The settings will allow you to turn music on or off. You cannot change this once this game starts.", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 195))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("The rankings will show how many points you have as a player, so make sure the name you enter is correct!", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 220))
    tutorial_screen.blit(tutorial_text, tutorial_rect)

    # Create icon
    icon_size = (100, 100)
    button_height = 50
    spacing = 10
    color = (128, 128, 128)
    cursor_color = (100, 100, 100)
    checkers_icon_resized = pygame.transform.scale(checkers_icon, icon_size)
    checkers_icon_rect = checkers_icon_resized.get_rect(topleft=(Width // 2 - 150 + 95, Height // 3+30 + (button_height - icon_size[1]) // 2))
    screen.blit(checkers_icon_resized, checkers_icon_rect.topleft) 

    # Second paragraph
    tutorial_text = tutorial_font.render("To play Checkers+, standard checkers rules are applied...with a twist!", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 365))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("You only have 5 seconds to make a move, so act fast! If you do not make a move within 5 seconds, ", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 390))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("you will lose your turn. Clicking on a piece will display available moves for that piece.", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 415))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("Like standard checkers, once a piece reaches the opposing player's last row, that piece will become a king.", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 440))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("This is indicated by a crown symbol that will display on the piece. Remember, you can move this piece backwards now!", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 465))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("When the game starts, you will be asked to enter the names of the players (or player, if playing against the computer).", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 490))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("Doing this will allow your name(s) and score(s) to be updated on your local leaderboard. 50 points for a win, and", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 515))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("-50 points for a loss. However, your first loss of the day will not affect your score, so don't quit if you're off to a bad start!", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 540))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("By now, you should have a basic understanding of what Checkers+ has to offer. Go give it a try!", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 565))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    # Developer note
    tutorial_text = tutorial_font.render("Note - Currently there is no button to exit a checkers game early. If you would like to quit,", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 590))
    tutorial_screen.blit(tutorial_text, tutorial_rect)
    tutorial_text = tutorial_font.render("simply close the window by clicking the X in the top right corner. This should return you to the main menu.", True, (255, 255, 255))
    tutorial_rect = tutorial_text.get_rect(center=(Width // 2, 615))
    tutorial_screen.blit(tutorial_text, tutorial_rect)

    # Exit button to return back to menu
    exit_button_font = pygame.font.Font(None, 32)
    exit_button_text = exit_button_font.render("Exit Tutorial", True, (255, 255, 255))
    exit_button_rect = exit_button_text.get_rect(center=(Width // 2, Height - 50))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button_rect.collidepoint(event.pos):  # if exit tutorial button is clicked
                    return  # exit tutorial and return to menu
            elif event.type == SONG_END:
                music_loop()

        mouse = pygame.mouse.get_pos()
        button_rect_5 = pygame.Rect(exit_button_rect.x - 10, exit_button_rect.y - 5, exit_button_rect.width + 20, exit_button_rect.height + 10)
        button_color_exit = cursor_color if button_rect_5.collidepoint(mouse) else color
        pygame.draw.rect(tutorial_screen, button_color_exit, button_rect_5)
        tutorial_screen.blit(exit_button_text, exit_button_rect)
        pygame.display.flip()

def settings():
    """
    The settings function displays the settings screen. It displays the music button that allows the user to stop and play the music. It allows the user to exit 
    the settings after clicking the exit button.
    """
    music_playing = True
    icon_size = (45, 45)
    button_height = 50
    spacing = 10
    settings_screen = pygame.display.set_mode([Width, Height])
    color = (128, 128, 128)
    cursor_color = (100, 100, 100)
    button_font = pygame.font.Font(None, 32)
    exit_button_font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()

    # Music button layout/text/icon
    music_icon = pygame.image.load('./assets/images/music_icon.png')
    music_position = (Width // 2 - 150, Height // 3 + button_height + spacing)
    music_size = (300, button_height)
    button_text = button_font.render("Music (On/Off)", True, (255, 255, 255))
    button_music_setting = button_font.render("Music is currently ON", True, (255, 255, 255))
    button_text_rect = button_text.get_rect(center=(Width // 2, Height // 3 + button_height + spacing + button_height // 2))
    button_music_setting_rect = button_music_setting.get_rect(center=(Width // 2, Height // 3 + button_height + spacing + button_height + 30))
    music_icon_resized = pygame.transform.scale(music_icon, icon_size)
    music_icon_rect = music_icon_resized.get_rect(
        topleft=(Width // 2 - 150 + 10, Height // 3 + button_height + spacing + (button_height - icon_size[1]) // 2)
    )
    button_rect_6 = pygame.Rect(music_position, music_size)
    # Exit button layout/text
    exit_button_text = exit_button_font.render("Exit Settings", True, (255, 255, 255))
    exit_button_rect = exit_button_text.get_rect(center=(Width // 2, Height - 100))
    button_rect_7 = pygame.Rect(exit_button_rect.x - 10, exit_button_rect.y - 5, exit_button_rect.width + 20, exit_button_rect.height + 10)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button_rect.collidepoint(event.pos):  # if exit settings button is clicked
                    return  # exit settings and return to menu
                if button_rect_6.collidepoint(event.pos):  # if music button is clicked
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.stop()  # Stop the music
                        music_playing = False
                    else:
                        music_loop()  # Start the music from next song in tracklist
                        music_playing = True
            elif event.type == SONG_END and music_playing == True:
                music_loop()
        if(music_playing):
            button_music_setting = button_font.render("Music is currently ON", True, (255, 255, 255))
        else:
            button_music_setting = button_font.render("Music is currently OFF", True, (255, 255, 255))
        # Redraw every frame so hover states update while mouse moves.
        settings_screen.blit(background_image, (0, 0))
        settings_screen.blit(title_text, title_rect)
        settings_screen.blit(message_text, message_rect)
        settings_screen.blit(credits_text1, credits_rect1)
        settings_screen.blit(credits_text2, credits_rect2)

        mouse = pygame.mouse.get_pos()
        button_color = cursor_color if button_rect_6.collidepoint(mouse) else color
        pygame.draw.rect(settings_screen, button_color, button_rect_6)
        settings_screen.blit(music_icon_resized, music_icon_rect.topleft)
        settings_screen.blit(button_text, button_text_rect)
        pygame.draw.rect(settings_screen, color, button_music_setting_rect.inflate(30,5))
        settings_screen.blit(button_music_setting, button_music_setting_rect)
        button_color_exit = cursor_color if button_rect_7.collidepoint(mouse) else color
        pygame.draw.rect(settings_screen, button_color_exit, button_rect_7)
        settings_screen.blit(exit_button_text, exit_button_rect)

        pygame.display.flip()
def show_leaderboard():
    """
    The show leaderboard function displays the leaderboard screen. It displays the top ten players and their scores. It allows the user to exit the leaderboard after clicking the
    exit button.
    """

    color = (128, 128, 128)
    cursor_color = (100, 100, 100)
    leaderboard_screen = pygame.display.set_mode((1000, 700))
    screen.fill((128, 128, 128))
    # Leaderboard header
    header_font = pygame.font.Font(None, 36)
    header_text = header_font.render("Leaderboard", True, (255, 255, 255))
    header_rect = header_text.get_rect(center=(500, 40))
    leaderboard_screen.blit(header_text, header_rect)
    
    score_manager = ScoreManager("./data/user_data.json")
    # Load scores from the JSON file
    score_manager.load_scores()

    # Sort players based on their scores in descending order
    sorted_players = sorted(score_manager.user_scores.items(), key=lambda x: x[1], reverse=True)

    # Extract the top ten players or all players if less than ten
    top_ten_players = sorted_players[:10]

    leaderboard_font = pygame.font.Font(None, 45)
    leaderboard_y = 80  # Adjust the vertical position as needed

    # Display the leaderboard in the new window
    for i, (username, score) in enumerate(top_ten_players):
        leaderboard_text = leaderboard_font.render(f"{i + 1}. {username}: {score} points", True, (255, 255, 255))
        leaderboard_text_rect = leaderboard_text.get_rect(center=(200, leaderboard_y + i * 30))
        leaderboard_text_rect.center = (500, leaderboard_y + i * 30)  # Adjust the horizontal position as needed
        leaderboard_screen.blit(leaderboard_text, leaderboard_text_rect)
        
    pygame.display.flip()

    # Exit button to return back to menu
    exit_button_font = pygame.font.Font(None, 32)
    exit_button_text = exit_button_font.render("Return to Main Menu", True, (255, 255, 255))
    exit_button_rect = exit_button_text.get_rect(center=(Width // 2, Height - 50))
    button_rect_8 = pygame.Rect(exit_button_rect.x - 10, exit_button_rect.y - 5, exit_button_rect.width + 20, exit_button_rect.height + 10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button_rect.collidepoint(event.pos):  # if exit tutorial button is clicked
                    return  # exit tutorial and return to menu
            elif event.type == SONG_END:
                music_loop()

        mouse = pygame.mouse.get_pos()
        button_color = cursor_color if button_rect_8.collidepoint(mouse) else color
        pygame.draw.rect(screen, button_color, button_rect_8)
        screen.blit(exit_button_text, exit_button_rect)

        pygame.display.flip()

# def board_customization(): 
#     """
#     The board customization function displays the board customization screen. It allows the user to change the color of the board to red, blue, yellow, or green. 
#     It allows the user to exit the board customization after clicking the exit button.
#     """
#     color = (128, 128, 128)
#     cursor_color = (100, 100, 100)
#     board_customization_screen = pygame.display.set_mode([Width, Height])
#     background_image = pygame.image.load("./assets/images/checkers.jpg")
#     background_image = pygame.transform.scale(background_image, (Width, Height))
#     # image of the background
#     board_customization_screen.blit(background_image, (0, 0))
#     board_customization_screen.blit(title_text, title_rect)
#     board_customization_screen.blit(message_text, message_rect)
#     board_customization_screen.blit(credits_text1, credits_rect1)
#     board_customization_screen.blit(credits_text2, credits_rect2)
#     # Exit button to return back to menu
#     exit_button_font = pygame.font.Font(None, 32)
#     exit_button_text = exit_button_font.render("Exit Board Customization", True, (255, 255, 255))
#     exit_button_rect = exit_button_text.get_rect(center=(Width // 2, Height - 100))
#     pygame.draw.rect(board_customization_screen, (128, 128, 128), exit_button_rect.inflate(20, 10))
#     board_customization_screen.blit(exit_button_text, exit_button_rect)

#     # Board Color Text
#     board_color_font = pygame.font.Font(None, 32)
#     board_color_text = board_color_font.render("Board Color", True, (255, 255, 255))
#     text_rect = board_color_text.get_rect(center=(Width // 2 - 200, Height // 3 + 80))
#     # Enlarge the box behind the text
#     box_width = text_rect.width + 40  # Increase width
#     box_height = text_rect.height + 20  # Increase height
#     box_rect = pygame.Rect(text_rect.left - 20, text_rect.top - 10, box_width, box_height)
#     # Draw the enlarged box behind the text
#     pygame.draw.rect(board_customization_screen, (128, 128, 128), box_rect)
#     board_customization_screen.blit(board_color_text, text_rect)
        
#     square_side = 50  # Size of the square
#     red_square_rect = pygame.Rect(text_rect.right + 50, text_rect.centery - square_side // 2, square_side, square_side)
#     pygame.draw.rect(board_customization_screen, RED, red_square_rect)  # Red square
#     blue_square_rect = pygame.Rect(red_square_rect.right + 20, red_square_rect.top, square_side, square_side)
#     pygame.draw.rect(board_customization_screen, BLUE, blue_square_rect)  # Blue square
#     yellow_square_rect = pygame.Rect(blue_square_rect.right + 20, blue_square_rect.top, square_side, square_side)
#     pygame.draw.rect(board_customization_screen, YELLOW, yellow_square_rect)  # Yellow square
#     green_square_rect = pygame.Rect(yellow_square_rect.right + 20, yellow_square_rect.top, square_side, square_side)
#     pygame.draw.rect(board_customization_screen, GREEN, green_square_rect)  # Green square

#     pygame.display.flip()
#     button_rect_9 = pygame.Rect(exit_button_rect.x - 10, exit_button_rect.y - 5, exit_button_rect.width + 20, exit_button_rect.height + 10)
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 return
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 if exit_button_rect.collidepoint(event.pos):  # if exit settings button is clicked
#                     return
#                 if red_square_rect.collidepoint(event.pos): # make board red
#                     second_menu_instance.color = RED
#                 if blue_square_rect.collidepoint(event.pos): # make board blue
#                     second_menu_instance.color = BLUE
#                 if yellow_square_rect.collidepoint(event.pos): # make board yellow
#                     second_menu_instance.color = YELLOW
#                 if green_square_rect.collidepoint(event.pos): # make board green
#                     second_menu_instance.color = GREEN
#             elif event.type == SONG_END:
#                 music_loop()

#         mouse = pygame.mouse.get_pos()
#         button_color = cursor_color if button_rect_9.collidepoint(mouse) else color
#         pygame.draw.rect(screen, button_color, button_rect_9)
#         screen.blit(exit_button_text, exit_button_rect)

#         pygame.display.flip()

# main()

def board_customization():
    """
    The board customization function displays the board customization screen. It allows the user to change the color of the board to red, blue, yellow, or green. 
    It allows the user to exit the board customization after clicking the exit button.
    """
    btn_color = (128, 128, 128)
    btn_hover = (100, 100, 100)
    panel_bg = (30,30,30,200)
    WHITE_COL = (255, 255, 255)
    SUCCESS_GREEN = (50, 200, 100)
    DARK_OVERLAY = (20,20,20)

    title_font = pygame.font.Font(None, 56)
    sub_font = pygame.font.Font(None, 30)
    label_font = pygame.font.Font(None, 28)
    btn_font = pygame.font.Font(None, 32)
    sucess_font = pygame.font.Font(None, 36)

    #color options
    color_options = [
        {"name": "Red", "color": RED, 
         "dark": (180, 0, 0)},
        {"name": "Blue", "color": BLUE,
        "dark": (0, 0, 180)},
        {"name": "Yellow", "color": YELLOW,
        "dark": (180, 180, 0)},
        {"name": "Green", "color": GREEN,
        "dark": (0, 90, 0)}
    ]
    #swatch layout
    swatch_w, swatch_h = 160, 160
    swatch_gap = 30
    total_w = len(color_options) * swatch_w + (len(color_options) - 1) * swatch_gap
    start_x = (Width - total_w) // 2
    swatch_y = 260
    swatch_rects = []
    for i in range(len(color_options)):
        x = start_x + i * (swatch_w + swatch_gap)
        swatch_rects.append(pygame.Rect(x, swatch_y, swatch_w, swatch_h))
    # back/exit button
    back_text = btn_font.render("Return to Main Menu", True, WHITE_COL)
    back_rect = back_text.get_rect(center=(Width // 2, Height - 120))
    back_btn = pygame.Rect(back_rect.x - 14, back_rect.y - 8, back_rect.width + 28, back_rect.height + 16)

    #state 
    selected_index = None
    success_msg = ""
    success_timer = 0
    SUCCESS_DURATION = 2500 #time to show success message in ms

    #pre-determine which swatch matches the current board color
    for i, opt in enumerate(color_options):
        if opt["color"] == second_menu_instance.color:
            selected_index = i
            break

    cust_screen = pygame.display.set_mode((Width, Height))
    bg_image = pygame.image.load("./assets/images/checkers.jpg")
    bg_image = pygame.transform.scale(bg_image, (Width, Height))
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(60) #limit to 60 fps
        now = pygame.time.get_ticks()
        mouse_pos = pygame.mouse.get_pos()

        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn.collidepoint(event.pos):
                    return
                for i, rect in enumerate(swatch_rects):
                    if rect.inflate(8, 8).collidepoint(event.pos):
                        selected_index = i
                        second_menu_instance.color = color_options[i]["color"]
                        success_msg = f"Board color changed to {color_options[i]['name']}!"
                        success_timer = now
            elif event.type == SONG_END:
                music_loop()

        #draw background
        cust_screen.blit(bg_image, (0, 0))
        #dark overlay
        overlay = pygame.Surface((Width, Height), pygame.SRCALPHA)
        overlay.fill((0,0,0,140))
        cust_screen.blit(overlay, (0, 0))

        #title 
        hdr = title_font.render("Customize Board", True, WHITE_COL)
        cust_screen.blit(hdr, hdr.get_rect(center=(Width // 2, 80)))
        sub = sub_font.render("Select a color theme for your checkers board:", True, WHITE_COL)
        cust_screen.blit(sub, sub.get_rect(center=(Width // 2, 130)))

        #divider line
        pygame.draw.line(cust_screen, WHITE_COL, (Width // 2 - 200, 160), (Width // 2 + 200, 160), 2)
        #current selection label
        if selected_index is not None:
            cur_label = sub_font.render(
               f"Current selection:  {color_options[selected_index]['name']}",
               True, (220, 220, 220)
            )
        else:
            cur_label = sub_font.render("No color selected yet", True, (180, 180, 180))
        cust_screen.blit(cur_label, cur_label.get_rect(center=(Width // 2, 200)))
        # draw swatches
        for i, (rect, opt) in enumerate(zip(swatch_rects, color_options)):
            is_selected = (i == selected_index)
            is_hovered = rect.collidepoint(mouse_pos)
            #shadow
            shadow = rect.move(4, 4)
            pygame.draw.rect(cust_screen, (10,10,10), shadow, border_radius=14)
            #swatch fill - brighten on hover
            fill_col = opt["color"] if not is_hovered else tuple(min(c+30, 255) for c in opt["color"])
            pygame.draw.rect(cust_screen, fill_col, rect, border_radius=14)

            #white border, thicker if selected
            if is_selected:
                pygame.draw.rect(cust_screen, WHITE_COL, rect.inflate(10, 10), border_radius=16, width=4)
            elif is_hovered:
                pygame.draw.rect(cust_screen, (200,200,200), rect.inflate(4, 4), border_radius=16, width=2)
            
# checkmark on selected swatch
            if is_selected:
                check_font = pygame.font.Font(None, 64)
                check = check_font.render("✓", True, WHITE_COL)
                cust_screen.blit(check, check.get_rect(center=rect.center))

            # color name label below swatch
            lbl = label_font.render(opt["name"], True, WHITE_COL)
            lbl_rect = lbl.get_rect(center=(rect.centerx, rect.bottom + 22))
            cust_screen.blit(lbl, lbl_rect)

        # success banner
        if success_msg and (now - success_timer) < SUCCESS_DURATION:
            alpha = 255
            fade_start = SUCCESS_DURATION - 600
            elapsed = now - success_timer
            if elapsed > fade_start:
                alpha = int(255 * (1 - (elapsed - fade_start) / 600))
            banner_surf = pygame.Surface((480, 52), pygame.SRCALPHA)
            banner_color = color_options[selected_index]["dark"] + (min(alpha, 210),)
            banner_surf.fill(banner_color)
            banner_rect = banner_surf.get_rect(center=(Width // 2, swatch_y + swatch_h + 90))
            cust_screen.blit(banner_surf, banner_rect)

            suc_text = sucess_font.render(success_msg, True, (255, 255, 255))
            suc_text.set_alpha(alpha)
            cust_screen.blit(suc_text, suc_text.get_rect(center=banner_rect.center))

        # back button
        back_col = btn_hover if back_btn.collidepoint(mouse_pos) else btn_color
        pygame.draw.rect(cust_screen, back_col, back_btn, border_radius=8)
        cust_screen.blit(back_text, back_rect)

        # credits
        cust_screen.blit(credits_text1, credits_rect1)
        cust_screen.blit(credits_text2, credits_rect2)
        pygame.display.flip()

main()

