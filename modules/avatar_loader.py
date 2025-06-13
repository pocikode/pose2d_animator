import json
import os

import pygame


class AvatarLoader:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.config = self._load_config()
        self.parts = self._load_parts()

    def _load_config(self):
        config_path = f"{self.folder_path}/config.json"
        if not os.path.isfile(config_path):
            raise FileNotFoundError(f"Missing config.json in {self.folder_path}")
        with open(config_path, "r") as file:
            return json.load(file)

    def _load_parts(self):
        parts = {}
        bones = self.config.get("bones", {})
        for part, filename in bones.items():
            file_path = os.path.join(self.folder_path, filename)
            if not os.path.isfile(file_path):
                raise FileNotFoundError(
                    f"Missing file for part {part} in {self.folder_path}"
                )

            parts[part] = pygame.image.load(file_path)

        return parts

    def get_part(self, part_name):
        if part_name not in self.parts:
            raise ValueError(f"Part {part_name} not found in avatar parts")
        return self.parts[part_name]

    def get_all_parts(self):
        return self.parts

    def get_config(self):
        return self.config
