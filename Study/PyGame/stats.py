class Stats():
    """tracking statistics"""

    def __init__(self):
        """statistics initialization"""
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """statistics that change during the game"""
        self.guns_left = 2
        self.score = 0
