import concurrent.futures
import configparser
import functools
from os import path

import cv2 as cv
from numpy import array
from PIL import ImageGrab
from utils.global_variables import get_image_recognition_images, COLOR_WAGES


NOTICE, NOTHING = get_image_recognition_images()

async def image_recognition_result(ctx, x, y, width, height):
    REEL_COLOR = ctx["config"]["colors"]["green"]
    WAIT_COLOR_BROWN = ctx["config"]["colors"]["brown"]
    WAIT_COLOR_RED = ctx["config"]["colors"]["red"]

    region = (x, y, x + width, y + height)
    img = None
    with concurrent.futures.ThreadPoolExecutor() as pool:  # Wrap PIL garbage
        img_foo = await ctx["loop"].run_in_executor(
            pool, functools.partial(ImageGrab.grab, bbox=region)
        )

        if ctx["config"]["log_lvl"] == "DEBUG":  # Save Scanned Image Locally For Review
            await ctx["loop"].run_in_executor(pool, img_foo.save, "scanned_image.png")

        img = array(img_foo)
    if len(img) <= 0:
        raise Exception("Error, image could not be captured?")

    with concurrent.futures.ThreadPoolExecutor() as pool:  # Wrap OpenCV garbage
        img_bw = await ctx["loop"].run_in_executor(pool, cv.cvtColor, img, cv.COLOR_RGB2GRAY)
        res = await ctx["loop"].run_in_executor(
            pool, cv.matchTemplate, img_bw, NOTICE, cv.TM_CCOEFF_NORMED
        )
        if (res >= 0.65).any():
            return "1"
        res = await ctx["loop"].run_in_executor(
            pool, cv.matchTemplate, img_bw, NOTHING, cv.TM_CCOEFF_NORMED
        )
        if (res >= 0.7).any():
            return "0"
    if await pixel_match(img, REEL_COLOR):
        return "2"
    if await pixel_match(img, WAIT_COLOR_BROWN):
        return "3"
    if await pixel_match(img, WAIT_COLOR_RED):
        return "4"
    return "5"


async def pixel_match(img, matcher):
    lower, upper = (
        [matcher[0] - COLOR_WAGES, matcher[1] - COLOR_WAGES, matcher[2] - COLOR_WAGES],
        [matcher[0] + COLOR_WAGES, matcher[1] + COLOR_WAGES, matcher[2] + COLOR_WAGES],
    )
    color_lower = array(lower)
    color_upper = array(upper)

    mask = cv.inRange(img, color_lower, color_upper)
    if mask.any():
        return True
    return False
