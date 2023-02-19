import random
import pychromecast

lofi_video_id = "5yx6BWlEVcY"

# Set up Chromecast
services, browser = pychromecast.discovery.discover_chromecasts()
print(services)
print(browser)
pychromecast.discovery.stop_discovery(browser)

chromecasts = pychromecast.get_chromecasts()
if not chromecasts:
    print("No Chromecasts found on the network.")
    exit()
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=['SHIELD'])
print([cc.device.friendly_name for cc in chromecasts])
chromecasts = [c for c in chromecasts if c != []]
chromecast = chromecasts[0] # Choose the first Chromecast found

chromecast.wait()
print(f"Casting to {chromecast.device.friendly_name}")

# Cast the YouTube video to the Chromecast
mc = chromecast.media_controller
mc.play_media(f"https://www.youtube.com/watch?v={lofi_video_id}", "video/mp4")
mc.block_until_active()
mc.play()
