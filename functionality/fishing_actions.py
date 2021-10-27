from utils.config import random_timeout

# from utils.utils import frange
from asyncio import sleep
from wrappers.win32api_wrapper import (
    press_mouse_key,
    release_mouse_key,
    release_key,
    press_key,
    click_mouse_with_coordinates,
)
from wrappers.logging_wrapper import debug


# def sleep_wrapper(sleep_time):
#     if sleep_time > 0.2:
#         for _ in frange(0, sleep_time, 0.01):
#             sleep(0.01)
#             return
#     sleep(sleep_time)


async def fish_notice(ctx):
    notice_timeout = await random_timeout(ctx["config"]["fishing"]["timeouts"]["notice"])
    debug(f"Press mouse key for: {notice_timeout} s")
    await press_mouse_key(ctx)
    await sleep(notice_timeout)
    await release_mouse_key(ctx)


async def reel_fish(ctx):
    reel_timeout = await random_timeout(ctx["config"]["fishing"]["timeouts"]["reeling"])
    debug(f"Press mouse key for: {reel_timeout} s")
    await press_mouse_key(ctx)
    await sleep(reel_timeout)
    await release_mouse_key(ctx)


async def pause(ctx):
    pause_timeout = await random_timeout(ctx["config"]["fishing"]["timeouts"]["pause"])
    debug(f"Pause for: {pause_timeout} s")
    await sleep(pause_timeout)


async def cast(ctx):
    cast_timeout = await random_timeout(ctx["config"]["fishing"]["timeouts"]["cast"])
    debug("Pause for: 6 s")
    await sleep(6)
    debug("release b")
    await release_key(ctx, "b")
    debug("Pause for: 1 s")
    await sleep(1)
    debug(f"Pause for: {cast_timeout} s")
    await press_mouse_key(ctx)
    await sleep(cast_timeout)
    await release_mouse_key(ctx)
    debug("Pause for: 4 s")
    await sleep(4)
    debug("press b")
    await press_key(ctx, "b")


async def repairing(ctx):
    await release_key(ctx, "b")
    arm_disarm_timeout = await random_timeout(ctx["config"]["repairing"]["timeouts"]["arm_disarm"])
    debug(f"Disarm fishing rod. Total time: {arm_disarm_timeout} s")
    await arm_disarm_fishing_rod(ctx, arm_disarm_timeout)

    inventory_timeout = await random_timeout(ctx["config"]["repairing"]["timeouts"]["inventory"])
    debug(f"Open inventory. Total time: {inventory_timeout} s")
    await open_close_inventory(ctx, inventory_timeout)

    repair_timeout = await random_timeout(ctx["config"]["repairing"]["timeouts"]["repair"])
    debug(f"Repair fishing rod. Total time: {repair_timeout} s")
    await repair(ctx, repair_timeout)

    confirm_timeout = await random_timeout(ctx["config"]["repairing"]["timeouts"]["confirm"])
    debug(f"Confirm repair. Total time: {confirm_timeout} s")
    await confirm_repair(ctx, confirm_timeout)

    debug(f"Close inventory. Total time: {inventory_timeout} s")
    await open_close_inventory(ctx, inventory_timeout)

    debug(f"Arm fishing rod. Total time: {arm_disarm_timeout} s")
    await arm_disarm_fishing_rod(ctx, arm_disarm_timeout)

    # move_around = await random_timeout(ctx["config"]["repairing"]["timeouts"]["move_around"])
    # debug(f"Move to prevent AFK kick. Total time:  {move_around} s")
    # await move_left_right(move_around)


async def arm_disarm_fishing_rod(ctx, timeout):
    await sleep(timeout)
    await press_key(ctx, "F3")
    await release_key(ctx, "F3")
    await sleep(timeout)


async def open_close_inventory(ctx, timeout):
    await sleep(timeout)
    await press_key(ctx, "tab")
    await release_key(ctx, "tab")
    await sleep(timeout)


async def repair(ctx, timeout):
    await sleep(timeout)
    await press_key(ctx, "r")
    await sleep(0.2)
    await click_mouse_with_coordinates(ctx, ctx["config"]["repairing"]["x"], ctx["config"]["repairing"]["y"])
    await sleep(0.2)
    await release_key(ctx, "r")
    await sleep(timeout)


async def confirm_repair(ctx, timeout):
    await sleep(timeout)
    await press_key(ctx, "e")
    await sleep(0.2)
    await release_key(ctx, "e")
    await sleep(timeout)


async def move_left_right(ctx, timeout):
    await press_key(ctx, "a")
    await sleep(timeout)
    await release_key(ctx, "a")
    await sleep(1.0)
    await press_key(ctx, "d")
    await sleep(timeout)
    await release_key(ctx, "d")


async def select_bait(ctx):
    await release_key(ctx, "b")

    debug("Bait selection.")
    await press_key(ctx, "r")
    await sleep(0.1)
    await release_key(ctx, "r")

    bait_select_timeout = await random_timeout(ctx["config"]["bait"]["timeouts"]["select"])
    debug(f"Bait select. Total time: {bait_select_timeout} s")
    await press_on_bait(ctx, bait_select_timeout)

    confirm_timeout = await random_timeout(ctx["config"]["bait"]["timeouts"]["confirm"])
    debug(f"Confirm bait selection. Total time: {confirm_timeout} s")
    await press_equip_bait(ctx, confirm_timeout)


async def press_on_bait(ctx, timeout):
    await sleep(timeout)
    await click_mouse_with_coordinates(ctx, ctx["config"]["bait"]["bait_x"], ctx["config"]["bait"]["bait_y"])
    await sleep(timeout)


async def press_equip_bait(ctx, timeout):
    await sleep(timeout)
    await click_mouse_with_coordinates(
        ctx, ctx["config"]["bait"]["equip_button_x"], ctx["config"]["bait"]["equip_button_y"]
    )
    await sleep(timeout)
    # waiting for animation to finish
    await sleep(1)
