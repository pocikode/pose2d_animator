import pygame

from modules.avatar_loader import AvatarLoader


class AvatarAnimator:
    def __init__(self, avatar_loader: AvatarLoader):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("2D Pose Animator")

        self.avatar_parts = {
            part: img.convert_alpha()
            for part, img in avatar_loader.get_all_parts().items()
        }

    def render(self, pose_landmarks):
        self.screen.fill((255, 255, 255))

        # TODO: draw parts here based on pose_landmarks
        # Example: just blitting torso at center for testing
        torso = self.avatar_parts.get("torso")
        if torso:
            rect = torso.get_rect(
                center=(self.screen_width // 2, self.screen_height // 2)
            )
            self.screen.blit(torso, rect)

        pygame.display.update()
        return self.screen.copy()
