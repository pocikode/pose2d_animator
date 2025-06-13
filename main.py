from tkinter import Tk, filedialog

from modules.animator import AvatarAnimator
from modules.avatar_loader import AvatarLoader


def select_avatar_folder():
    root = Tk()
    root.withdraw()  # Hide the root window
    folder_path = filedialog.askdirectory(title="Select Avatar Folder")
    root.destroy()  # Close the root window
    return folder_path


def main():
    # Step 1: Select avatar folder
    avatar_folder = select_avatar_folder()
    if not avatar_folder:
        print("No avatar folder selected. Exiting.")
        return

    avatar_data = AvatarLoader(avatar_folder)

    # TODO: Step 2: Get video source (from file or webcam)
    # TODO: Step 3: Initialize pose estimator

    # Step 4: Initialize animator with avatar data
    animator = AvatarAnimator(avatar_data)
    animator.render(None)


if __name__ == "__main__":
    main()
