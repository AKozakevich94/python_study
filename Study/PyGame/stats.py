class Stats():
    """tracking statistics"""

    def __init__(self):
        """statistics initialization"""
        self.reset_stats()

    def reset_stats(self):
        """statistics that change during the game"""
        self.guns_left = 2
