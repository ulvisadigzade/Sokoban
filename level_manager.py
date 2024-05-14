def get_level():
    import pygame
    # Initialize Pygame
    pygame.init()
    pygame.font.init()
    # Set up the screen
    screen_width, screen_height = 400, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Level")


    # Define font
    font = pygame.font.SysFont("Comic Sans MS", 36)

    # Function to create a button
    def draw_button(x, y, width, height, color, text, action):
        pygame.draw.rect(screen, color, (x, y, width, height))
        text_surface = font.render(text, True, "BLACK")
        text_rect = text_surface.get_rect(center=(x + width/2, y + height/2))
        screen.blit(text_surface, text_rect)
        # Return button rect and action
        return pygame.Rect(x, y, width, height), action

    # Define actions for each button
    BUTTON_1_ACTION = 1
    BUTTON_2_ACTION = 2

    # Main loop
    a = None  # Variable to store button clicked
    button1_rect = None
    button2_rect = None
    running = True
    while running:
        screen.fill("#d69327")
        for event in pygame.event.get():                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    # Check if button 1 is clicked
                    if button1_rect.collidepoint(mouse_pos):
                        a = BUTTON_1_ACTION
                        return a
                    # Check if button 2 is clicked
                    elif button2_rect.collidepoint(mouse_pos):
                        a = BUTTON_2_ACTION
                        return a
            elif event.type == pygame.QUIT:
                running=False
        # Draw buttons and get button rectangles
        text_surface = font.render("Sokoban", True, "BLACK")
        screen.blit(text_surface,(125,200,400,200))
        button1_rect, _ = draw_button(100, 300, 200, 50, "GRAY", "First level", BUTTON_1_ACTION)
        button2_rect, _ = draw_button(100, 400, 200, 50, "GRAY", "Second level", BUTTON_2_ACTION)

        pygame.display.flip()

    return a
    # Quit Pygame
