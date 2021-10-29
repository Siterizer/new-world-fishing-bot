import concurrent.futures
from asyncio import sleep

import win32api
import win32con


async def click_mouse_with_coordinates(ctx, x, y):
    with concurrent.futures.ThreadPoolExecutor() as pool:
        await ctx["loop"].run_in_executor(pool, win32api.SetCursorPos, (x, y))
        await sleep(0.1)
        await ctx["loop"].run_in_executor(
            pool, win32api.mouse_event, win32con.MOUSEEVENTF_LEFTDOWN, 0, 0
        )
        await sleep(0.1)
        await ctx["loop"].run_in_executor(
            pool, win32api.mouse_event, win32con.MOUSEEVENTF_LEFTUP, 0, 0
        )


VK_CODE = {
    "tab": 0x09,
    "a": 0x41,
    "b": 0x42,
    "d": 0x44,
    "e": 0x45,
    "r": 0x52,
    "F3": 0x72,
}


async def press_key(ctx, key):
    with concurrent.futures.ThreadPoolExecutor() as pool:
        await ctx["loop"].run_in_executor(pool, win32api.keybd_event, VK_CODE[key], 0, 0, 0)
        await sleep(0.05)


async def release_key(ctx, key):
    with concurrent.futures.ThreadPoolExecutor() as pool:
        await ctx["loop"].run_in_executor(
            pool, win32api.keybd_event, VK_CODE[key], 0, win32con.KEYEVENTF_KEYUP, 0
        )


async def press_mouse_key(ctx):
    with concurrent.futures.ThreadPoolExecutor() as pool:
        await ctx["loop"].run_in_executor(
            pool, win32api.mouse_event, win32con.MOUSEEVENTF_LEFTDOWN, 0, 0
        )


async def release_mouse_key(ctx):
    with concurrent.futures.ThreadPoolExecutor() as pool:
        await ctx["loop"].run_in_executor(
            pool, win32api.mouse_event, win32con.MOUSEEVENTF_LEFTUP, 0, 0
        )
