import pyautogui


def get_targets():
    list_of_targets = []
    objects = pyautogui.locateAllOnScreen("LittleRat1.png", region=(285, 200, 1350, 680), grayscale=True, confidence=0.7)
    if objects:
        for cords in objects:
            list_of_targets.append((cords.left, cords.top))
    else:
        print("unable to locate objects")
    print(f"found {list_of_targets}")
    return list_of_targets


def get_drops():
    list_of_drops = []
    objects = pyautogui.locateAllOnScreen("LittleTooth.png", region=(415, 300, 1090, 480), confidence=0.6)
    if objects:
        for cords in objects:
            list_of_drops.append((cords.left, cords.top))

    objects1 = pyautogui.locateAllOnScreen("OldRope1.png", region=(415, 300, 1090, 480), confidence=0.6)
    if objects1:
        for cords1 in objects1:
            list_of_drops.append((cords1.left, cords1.top))

    objects2 = pyautogui.locateAllOnScreen("BrokenBones.png", region=(415, 300, 1090, 480), confidence=0.6)
    if objects2:
        for cords2 in objects2:
            list_of_drops.append((cords2.left, cords2.top))
    else:
        print("unable to locate objects")

    print(f"found {list_of_drops}")
    return list_of_drops
# Box(left=550, top=504, width=52, height=14)
